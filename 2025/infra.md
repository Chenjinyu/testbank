## Kubernetes

Kubernetes YAML files are used to declare and manage different resource types, each representing a piece of infrastructure or behavior in your cluster. Here’s a guide to the most common kinds (kind:) you’ll encounter, grouped by category and purpose:

#### 1. Workload Resources (Pod & Abstractions)
| Kind            | Description                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **Pod**         | The smallest deployable unit. Usually created indirectly via higher-level objects like Deployments. |
| **Deployment**  | Manages stateless apps; handles rolling updates, scaling, etc.                                      |
| **StatefulSet** | For stateful apps that need stable identities (e.g., DBs, Kafka).                                   |
| **DaemonSet**   | Ensures one pod per node (e.g., log shippers like Fluent Bit).                                      |
| **Job**         | One-off or batch jobs that run to completion.                                                       |
| **CronJob**     | Schedules Jobs like a cron task (e.g., run every hour).                                             |
| **ReplicaSet**  | Low-level controller for managing a set of identical Pods (used by Deployment under the hood).      |

#### 2.Service Discovery & Networking
| Kind              | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| **Service**       | Exposes a set of Pods as a network service (ClusterIP, NodePort, LoadBalancer).      |
| **Ingress**       | HTTP(S) reverse proxy that routes requests to services (often via NGINX or Traefik). |
| **IngressClass**  | Defines the controller handling a particular ingress (e.g., nginx, istio).           |
| **Endpoint**      | Low-level object listing IPs for a Service. Usually auto-generated.                  |
| **NetworkPolicy** | Controls traffic flow between pods for security.                                     |

#### 3. Configuration & Secrets
| Kind                            | Description                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| **ConfigMap**                   | Stores non-sensitive key-value pairs (e.g., ENV vars, config files). |
| **Secret**                      | Stores sensitive data (e.g., passwords, tokens), base64-encoded.     |
| **ServiceAccount**              | Identity for pods to access the Kubernetes API securely.             |
| **PersistentVolume** (PV)       | A storage resource in the cluster.                                   |
| **PersistentVolumeClaim** (PVC) | A request for storage by a pod.                                      |


#### 4. Access Control
| Kind                   | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| **Role**               | Defines access to resources within a namespace.          |
| **ClusterRole**        | Same as Role but cluster-wide.                           |
| **RoleBinding**        | Grants Role permissions to a user/group/service account. |
| **ClusterRoleBinding** | Same as RoleBinding but cluster-wide.                    |


#### 5. Observability / Monitoring
| Kind                   | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| **ServiceMonitor**     | (Used by Prometheus Operator) Defines which services to scrape for metrics. |
| **PodMonitor**         | (Also Prometheus) Defines scraping rules based on pods.                     |
| **AlertmanagerConfig** | Configures Prometheus alerts (when using Prometheus Operator).              |


#### 6. ArgoCD / Helm / GitOps Specific
| Kind                     | Description                                    |
| ------------------------ | ---------------------------------------------- |
| **Application** (ArgoCD) | Defines a Git-based app deployment             |
| **HelmRelease** (FluxCD) | Declarative Helm chart deployment              |
| **HelmChart**            | Defines a Helm chart source in some CRDs       |
| **Kustomization**        | Used with Kustomize/Flux for manifest overlays |



## Helm in Kubernetes
[helm Doc](https://helm.sh/docs/chart_template_guide/getting_started/)
```sh
helm create app_name 
# to create project which has folder structure like
# app_name
#   - charts
#   - templates
#     - deployment.yaml
#     - hpa.yaml
#     - ingress.yaml
#     - etc.
#   - .helmignore
#   - .Chart.yaml
#   - values.yaml
```

```sh
helm install --debug --dry-run randon_name ./order_services/
# which render the template for you 
```