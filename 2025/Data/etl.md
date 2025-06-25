## ETL
Extract -> Transform -> Load is a data integration process that involoes:
extracing data from various sources, transforming it into a usable format, and loading it into a target system like a data warehouse. 
It's a fundamental process for data warehousing, data science, and buiness intelliegence. 

## What are the differences between AWS glue, EMR, AWS Hadoop and Spark. 

Let’s break down the differences between **AWS Glue**, **Amazon EMR**, **Apache Hadoop**, and **Apache Spark** — since they often overlap in function but serve different needs.


#### 🧠 TL;DR Summary

| Feature         | AWS Glue                       | Amazon EMR                     | Apache Hadoop             | Apache Spark                   |
| --------------- | ------------------------------ | ------------------------------ | ------------------------- | ------------------------------ |
| **Type**        | Managed ETL service            | Managed big data platform      | Open-source framework     | Open-source engine             |
| **Use Case**    | ETL/ELT jobs (no cluster mgmt) | Flexible big data processing   | Batch data processing     | Fast in-memory data processing |
| **Who Manages** | AWS (serverless)               | You (on EC2 or EKS)            | You (self-hosted)         | You (self-hosted or on EMR)    |
| **Languages**   | PySpark, Scala, SQL            | Hive, Spark, Hadoop, Presto... | Java, Pig, Hive           | Scala, Python, Java, R         |
| **Cost Model**  | Pay per job or DPU-hour        | Pay per EC2 usage              | Infra + setup + mgmt cost | Infra + setup + mgmt cost      |
| **Infra setup** | No cluster, just jobs          | You configure nodes/clusters   | You manage hardware       | You manage hardware            |


#### 🔍 Detailed Comparison

##### 1. **AWS Glue**

* **Fully managed**, **serverless** ETL service.
* Focused on **data preparation, cataloging, and transformation**.
* **Built on top of Apache Spark**.
* No need to manage infrastructure.
* You define **jobs in PySpark or Glue Studio (GUI)**.
* Includes **Data Catalog** to track metadata.
* Supports **event-based or scheduled jobs**.

💡 Best for:

* Automated ETL pipelines
* Data lakes (especially S3 → Glue → Redshift)
* Users who want no infrastructure to manage


##### 2. **Amazon EMR (Elastic MapReduce)**

* **Managed cluster platform** for **big data frameworks**.
* You can run **Apache Hadoop, Apache Spark, Hive, Presto, HBase, etc.** on **EC2, EKS, or Fargate**.
* Fully configurable: choose instance types, autoscaling, spot pricing.
* Supports **batch, interactive, and streaming jobs**.
* Can integrate with **S3, HDFS, RDS, DynamoDB**.

💡 Best for:

* Custom big data pipelines
* Complex Spark/Hive workflows
* Companies wanting cluster control

##### 3. **Apache Hadoop**

* **Open-source big data framework**.
* Based on **MapReduce** + **HDFS** (distributed file system).
* Batch-oriented; slower compared to Spark.
* Spark can run **on top of Hadoop YARN** (resource manager).
* Requires **manual cluster setup, monitoring, etc.**

💡 Best for:

* Legacy systems or very large-scale batch jobs
* When storage-distributed processing is needed

##### 4. **Apache Spark**

* **In-memory distributed computing engine**.
* **Much faster** than Hadoop MapReduce for many use cases.
* Supports batch, streaming, ML (via MLlib), and SQL (via Spark SQL).
* Runs standalone or on YARN, Kubernetes, or Mesos.
* Used by both Glue and EMR.

💡 Best for:

* Fast data transformation, ML jobs
* Stream + batch hybrid workflows

#### 🔗 Relationship Flow (example)

```text
        You Write PySpark Code
                ↓
        ┌──────────────┐
        │ Apache Spark │  ← open-source engine
        └─────┬────────┘
              ↓
 ┌────────────┴─────────────┐
 │ Glue (no cluster)        │ ← Managed Spark jobs
 │ EMR (you manage cluster) │ ← Clustered Spark jobs
 └──────────────────────────┘
```

#### 🧭 When to Use What?

| You want to...                            | Best Option                       |
| ----------------------------------------- | --------------------------------- |
| Run simple ETL without managing infra     | **AWS Glue**                      |
| Run large-scale Spark jobs with tuning    | **EMR**                           |
| Use classic Hadoop stack (MapReduce, Pig) | **EMR or Hadoop**                 |
| Build fast analytics or ML on big data    | **Spark on EMR or Glue**          |
| Do everything yourself, open-source only  | **Hadoop + Spark** (self-managed) |

