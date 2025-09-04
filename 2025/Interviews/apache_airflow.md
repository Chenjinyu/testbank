# My resume content described the apache airflow experience. 
## The Description
**Designed and built a scalable Apache Airflow platform supporting CI/CD-based onboarding for internal users.**
- Deployed Apache Airflow to Amazon ECS with a custom Docker image and ECS Service autoscaling, ensuring elastic capacity for webserver/scheduler/workers.
- Built an event-driven DAG onboarding pipeline: repositories opt in by declaring the dag-job-onboarding gear in user's Bogiefile. Once PR merged, Jenkins triggers the AWS Lambda that copies DAGs from the repo to a shared Amazon EFS mount consumed by Airflow.
- Wired Airflow to the EFS DAG directory so the UI refreshes automatically and new DAGs appear within seconds—no manual redeploys.
- Developed custom Airflow plugins (operators/hooks) and authored end-to-end onboarding docs & walkthroughs, cutting time-to-first-DAG and support load. 


## what are the solution I built in C1
- The best practice on ECS is one airlfow base image and separate ECS services/tasks that run different commands(webserver, scheduler, trigger, worker, broker and flower)
- I chose CeleryExecutor(most commom on ECS, easiest to autoscale)
- Required components
  - Metadata DB: Postgres (Amazon RDS/Aurora)
  - Webserver: 1–2 tasks (behind an ALB)
  - Scheduler: 1–2 tasks (Airflow 2.x supports HA—only one is leader)
  - Triggerer: 1–2 tasks (needed for deferrable operators)
  - Broker: Redis (ElastiCache) or RabbitMQ (Amazon MQ)
  - Workers: N tasks (autoscale these)
  - Optional: Flower UI for Celery

>> Small prod starting point: RDS + Redis, Webserver ×2, Scheduler ×2, Triggerer ×1–2, Workers ×2 (autoscale on queue depth), ALB, EFS for DAGs/plugins, S3 for logs.

## One image, different commands per ECS service
1. Build one Airflow image.
2. In each ECS service/task, override the container command:
  - Webserver → ["airflow","webserver"]
  - Scheduler → ["airflow","scheduler"]
  - Triggerer → ["airflow","triggerer"]
  - Worker (Celery) → ["airflow","celery","worker","--concurrency","8"]
  - Flower (Celery UI) → ["airflow","celery","flower"]

#### Single Dockerfile (base for all roles)
```dockerfile
# Dockerfile
FROM apache/airflow:2.9.2-python3.11

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates build-essential \
  && rm -rf /var/lib/apt/lists/*
USER airflow

# Python deps (adjust to your stack)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: plugins/ and include/ (DAGs will come from EFS at runtime)
COPY plugins/ /opt/airflow/plugins/
COPY include/  /opt/airflow/include/

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

# Healthcheck is handy for webserver; harmless elsewhere
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=5 \
  CMD curl -fsS http://localhost:8080/health || exit 1

# No CMD here — ECS will set the role-specific command per service

```
>>In ECS task definitions, just set a different command for each service using this one image.

OR 

#### One Base image, and with different server images
##### 1) Base Image(build once)
```dockerfile
# Dockerfile.base
FROM apache/airflow:2.9.2-python3.11

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates build-essential \
  && rm -rf /var/lib/apt/lists/*
USER airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY plugins/ /opt/airflow/plugins/
COPY include/  /opt/airflow/include/

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
```

##### Build and Push to artifactory
```sh
docker build -f Dockerfile.base -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2

```

##### 2) Role Images (One file per role)

###### Webserver
```dockerfile
# Dockerfile.webserver
FROM <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2
# Optional: keep a healthcheck for ECS
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=5 \
  CMD curl -fsS http://localhost:8080/health || exit 1
CMD ["airflow","webserver"]

```

###### Scheduler
```dockerfile
# Dockerfile.scheduler
FROM <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2
CMD ["airflow","scheduler"]

```
###### Trigger (Needed for deferrable Operators)
```dockerfile
# Dockerfile.triggerer
FROM <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2
CMD ["airflow","triggerer"]

```

###### Worker (Celery Executor)
```dockerfile
# Dockerfile.worker
FROM <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2
# Tune concurrency to your CPU/mem
CMD ["airflow","celery","worker","--concurrency","8","--hostname","worker@%h"]

```

###### Flower (Celery monitoring UI)
```dockerfile
# Dockerfile.flower
FROM <acct>.dkr.ecr.<region>.amazonaws.com/airflow-base:2.9.2
CMD ["airflow","celery","flower","--port","5555"]

```

###### build and push each:
```sh
docker build -f Dockerfile.webserver -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-web:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-web:2.9.2

docker build -f Dockerfile.scheduler -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-scheduler:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-scheduler:2.9.2

docker build -f Dockerfile.triggerer -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-triggerer:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-triggerer:2.9.2

docker build -f Dockerfile.worker -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-worker:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-worker:2.9.2

docker build -f Dockerfile.flower -t <acct>.dkr.ecr.<region>.amazonaws.com/airflow-flower:2.9.2 .
docker push <acct>.dkr.ecr.<region>.amazonaws.com/airflow-flower:2.9.2

```

#### ECS Tips
- Env/Secrets: set `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`, `AIRFLOW__CELERY__BROKER_URL`, etc., via ECS task environment or Secrets Manager.
- Volumes: mount EFS at /opt/airflow/dags (your Lambda copies DAGs here).
- Logs: set S3 remote logging or use CloudWatch logs.
- Autoscaling: scale workers on CPU or Celery queue depth; keep webserver/scheduler/triggerer at fixed small counts (add HA where needed).
- Health checks: for webserver, hit /health; for others, rely on process health/CPU/memory and logs.


#### What is "The Broker"
In Airflow with CeleryExecutor, the message broker is the queueing system (e.g. Redis or RabitMQA) that sites between the scheuder and the workers. think of it as a shared to-do list.
1. scheulder puts "run this task instance" message onto the broker
2. Workers pull messages, execute the task then ack/finish.
without a borker, the scheulder has no scalable way to hand work to many workers living on differnet ECS tasks/instances.

##### Why you need it (with CeleryExecutor)
- Decoupling & scale-out: scheduler and workers scale independently; add/remove workers without touching the scheduler.
- Reliability: tasks persist in a queue; if a worker dies pre-ack, the task is re-queued for another worker.
- Autoscaling signal: queue depth (and age) are clean metrics to scale your ECS worker service up/down.
- Backpressure: if workers are full, messages pile up in the broker instead of overloading your scheduler.

##### When you do not need a broker
- **LocalExecutor**: tasks run in the scheduler process (good for dev/POC; not horizontally scalable).
- **KubernetesExecutor**: tasks become Pods; the Kubernetes control plane is effectively the dispatcher (no Celery broker).

##### Managed options on AWS
- Redis → Amazon ElastiCache for Redis (common choice, simple, fast).
- RabbitMQ → Amazon MQ (RabbitMQ engine) (richer features, exchanges/queues).