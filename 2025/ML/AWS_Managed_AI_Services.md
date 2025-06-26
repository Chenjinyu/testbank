- AWS AI services are pre-trained ML services for your use case
- Responsiveness and Availability
- Redundancy and Regional Coverage: Deployed access multiple avaiable zones and aws regions
- Performance: specialized CPU and GPUs for specific use-cases for cost saving
- Token-based pricing: pay for what you use
- Provisioned throughtput: for predictable workloads, cost saving and predictable performance


## SageMaker JumpStart
SageMaker JumpStart is AWS's machine learning hub that provides:

- Pre-built ML solutions: Ready-to-use models and algorithms for common use cases like computer vision, natural language processing, and time series forecasting
- Foundation models: Access to popular large language models (LLMs) and other foundation models from providers like Hugging Face, Stability AI, and AI21 Labs
- One-click deployment: Deploy models to SageMaker endpoints with minimal configuration
- Example notebooks: Jupyter notebooks with sample code and tutorials to get started quickly
- Custom training: Ability to fine-tune pre-trained models on your own data
- Model catalog: Browse and discover models by use case, framework, or provider

It's essentially a marketplace and launching pad for ML models that accelerates the development process by providing pre-trained models and example implementations, fitting well with your document's theme of AWS managed AI services that offer "pay for what you use" pricing and specialized performance optimization.

## Amazon Bedrock
Foundation Model Access: Provides API access to leading foundation models from AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI, and Amazon

- Serverless: No infrastructure to manage - just call APIs to use models
- Model Customization: Fine-tune models with your own data using techniques like continued pre-training and fine-tuning
- Knowledge Bases: Build RAG (Retrieval-Augmented Generation) applications by connecting models to your data sources
- Agents: Create AI agents that can reason, plan, and execute tasks using your APIs and knowledge bases
- Security & Privacy: Your data stays private and isn't used to train the underlying models
- Pay-per-use: Token-based pricing aligned with your document's pricing model
- Guardrails: Built-in content filtering and safety controls for responsible AI deployment

Bedrock essentially democratizes access to powerful AI models without requiring deep ML expertise, making it easy to build generative AI applications like chatbots, content generation, and document analysis tools.
## Amazon Q Business

## Amazon Q Developer


## Text and Documnets
### Amazon Comprehend
### Amazon Translate
### Aamazon Textract

## Vision
### Amazon Rekognition

## Search
### Amazon Kendra

## Chatbots
### Amazon Lex

## Speech
### Amazon Polly
### Amazon Transcribe

## Recommendations
### Amazon Personalize

---

## 📦 What is **Amazon SageMaker**?

**Amazon SageMaker** is a **fully managed machine learning (ML) platform** by AWS that helps developers and data scientists **build, train, tune, and deploy ML models at scale** — without managing the underlying infrastructure.

#### 🚀 Key Features

| Feature                 | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| **Studio**              | A web-based IDE for ML (like Jupyter + GitHub + ML tools in one place) |
| **Notebooks**           | Managed Jupyter notebooks with scalable compute                        |
| **Training Jobs**       | Run distributed model training with auto-scaling and spot instances    |
| **Inference/Endpoints** | Deploy real-time or batch prediction services (APIs)                   |
| **AutoML (Autopilot)**  | Automatically build, train, and tune models                            |
| **Pipelines**           | CI/CD workflows for ML (data → training → model → deploy)              |
| **Data Wrangler**       | GUI for cleaning and preparing data                                    |
| **Feature Store**       | Centralized storage for ML features                                    |
| **Model Monitor**       | Track drift or bias in deployed models                                 |
| **JumpStart**           | Pre-trained models and solutions (vision, text, etc.)                  |


#### 🔧 Example Workflow

1. **Prepare data**: Ingest and clean data from S3, Athena, Redshift, etc.
2. **Build models**: Use Jupyter notebooks (Python, TensorFlow, PyTorch, etc.)
3. **Train**: Use built-in or custom algorithms at scale (on EC2 or GPU-backed instances)
4. **Tune (optional)**: Hyperparameter optimization with SageMaker Tuning
5. **Deploy**: Host the model with one click (auto-scaled endpoints)
6. **Monitor**: Track performance, latency, and drift

#### 🎯 When to Use SageMaker?

Use SageMaker when you:

* Want a **fully managed ML environment** (less DevOps).
* Need **scalable and distributed training** on large datasets.
* Want to go from **data → model → API** efficiently.
* Need **production-grade MLOps tools** (monitoring, CI/CD, model registry).
* Are doing **deep learning**, **tabular ML**, or **custom ML workflows**.

#### 💰 Is SageMaker Free?

* SageMaker offers a **free tier** (250 hours/month of t2.micro notebooks for 2 months).
* After that, **you pay for:**

  * **Notebook instance hours**
  * **Training time (by instance type)**
  * **Inference endpoints**
  * **Storage (EFS/EBS/S3)**
  * **Extra services** (e.g., Data Wrangler, Model Monitor)

#### 🧪 Example: Create a Model and Deploy

```python
from sagemaker import LinearLearner
from sagemaker import Session

# Load data
sagemaker_session = Session()
train_data = sagemaker_session.upload_data('train.csv', key_prefix='data')

# Train model
linear = LinearLearner(role='SageMakerRole',
                       train_instance_count=1,
                       train_instance_type='ml.m4.xlarge',
                       predictor_type='binary_classifier')
linear.fit({'train': train_data})

# Deploy model
predictor = linear.deploy(initial_instance_count=1, instance_type='ml.t2.medium')
```
