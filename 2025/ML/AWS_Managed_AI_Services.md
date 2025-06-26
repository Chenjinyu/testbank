- AWS AI services are pre-trained ML services for your use case
- Responsiveness and Availability
- Redundancy and Regional Coverage: Deployed access multiple avaiable zones and aws regions
- Performance: specialized CPU and GPUs for specific use-cases for cost saving
- Token-based pricing: pay for what you use
- Provisioned throughtput: for predictable workloads, cost saving and predictable performance


## SageMaker JumpStart
### 🚀 What is **Amazon SageMaker JumpStart**?

**SageMaker JumpStart** is a feature in Amazon SageMaker Studio that provides **pre-built ML solutions**, **models**, and **notebooks** so you can start machine learning projects quickly—without having to build everything from scratch.

It's like an **ML app store** for:

* Pre-trained models (e.g., image classification, text summarization)
* Example notebooks
* Fully-built ML solutions (fraud detection, churn prediction, etc.)
* Foundation models (e.g., Falcon, Claude, Mistral, etc.) you can deploy with a few clicks

#### 🎯 Key Benefits

| Benefit                         | Description                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| ✅ **No ML expertise needed**    | Start with ready-made solutions for common business problems              |
| ⚙️ **Pre-built & customizable** | Modify code, hyperparameters, or data as needed                           |
| ⚡ **Fast prototyping**          | Go from idea → deployed model/API in minutes                              |
| 📚 **Learning resource**        | Great for learning best practices (preprocessing, deployment, evaluation) |
| 🧠 **Foundation models**        | Easily deploy HuggingFace, Falcon, LLaMA, Claude, etc.                    |
| 🔌 **Integration ready**        | Works out of the box with SageMaker Pipelines, Feature Store, and Studio  |
| 💰 **Cost-effective**           | Pay only for compute/storage you use — the JumpStart UI itself is free    |

#### 🔍 What Can You Do With JumpStart?

##### 🧠 1. Use Pre-trained Models

* **Text classification**
* **Object detection**
* **Sentiment analysis**
* **Text generation**
* **Image segmentation**
* **Embedding models** for search and vector DBs

➡️ Models from **Hugging Face**, **TensorFlow Hub**, **PyTorch Hub**, and **SageMaker built-ins**.

##### 💡 2. Launch End-to-End Solutions

With just a few clicks, you can deploy:

* **Churn prediction**
* **Fraud detection**
* **Credit risk scoring**
* **Anomaly detection**
* **Customer segmentation**
* **Document summarization**

These solutions include:

* Notebook + sample data
* Preprocessing logic
* Model training + evaluation
* Inference endpoint

##### 🌐 3. Access to Foundation Models (FMs)

JumpStart lets you easily **deploy FMs** from Amazon Bedrock or Hugging Face for:

* Text generation (Falcon, Mistral, Claude)
* Embedding generation
* Chatbot integration


#### 🧪 Example Use Case: Churn Prediction

You can launch the "Customer Churn Prediction" solution in SageMaker JumpStart:

1. Modify the notebook with your data
2. Run training with built-in XGBoost
3. Deploy model to endpoint
4. Call endpoint via API to predict churn

🧠 No need to write model logic or infrastructure.


#### ✅ Summary

| Feature                | SageMaker JumpStart                    |
| ---------------------- | -------------------------------------- |
| Use case templates     | ✅ Yes                                  |
| Pre-trained models     | ✅ Yes                                  |
| Foundation models      | ✅ Yes                                  |
| Requires coding skills | ❌ Not required                         |
| Customizable           | ✅ Yes                                  |
| Cost                   | Free to browse, pay for resources used |

---

## 🌐 What is **Amazon Bedrock**?

**Amazon Bedrock** is a fully managed service by AWS that lets you **build and scale generative AI applications** using **foundation models (FMs)** from leading AI companies—**without managing any infrastructure** or training your own models.

> Think of it as **“GPT-as-a-Service”**, but with multiple model providers.

#### 🧠 What Can You Do With Bedrock?

* Access and use **pre-trained foundation models** (FMs) via API (no fine-tuning or GPU required).
* Build apps like:

  * Text generation / summarization
  * Q\&A and chatbots (RAG)
  * Image generation
  * Code generation
  * Embedding and vector search

#### 🔥 Foundation Models Available in Bedrock

| Provider         | Models                               |
| ---------------- | ------------------------------------ |
| **Anthropic**    | Claude 2, Claude 3 (Q\&A, reasoning) |
| **Meta**         | LLaMA 2, LLaMA 3                     |
| **Cohere**       | Embed & Generate models              |
| **Mistral**      | Mistral 7B, Mixtral                  |
| **Amazon**       | Titan Text, Titan Embeddings         |
| **Stability AI** | Stable Diffusion (image generation)  |

#### ✅ Key Benefits of Amazon Bedrock

| Benefit                          | Description                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------- |
| 🧠 **Model flexibility**         | Access models from **multiple providers** via one API                        |
| ⚙️ **Fully managed**             | No need to provision or scale GPUs/servers                                   |
| 🔐 **Enterprise-grade security** | Integrated with IAM, VPC, CloudWatch, KMS                                    |
| 🧱 **Integrates with AWS stack** | Works with S3, Lambda, SageMaker, API Gateway, etc.                          |
| 🧩 **Supports RAG**              | Built-in tools to use **embeddings + vector DBs**                            |
| 📦 **No fine-tuning needed**     | Use models as-is or perform simple **prompt engineering**                    |
| 🧰 **Agent capabilities**        | Build workflows with memory, tools, APIs, etc. (similar to LangChain agents) |

#### 🧪 Example Use Case

##### 🤖 Chatbot with RAG:

1. Store internal documents in Amazon S3
2. Use **Titan Embeddings** via Bedrock to generate vector embeddings
3. Store in Amazon OpenSearch or Pinecone
4. Use **Claude 3** or **LLaMA 3** via Bedrock to answer queries using relevant documents

##### 🖼️ Image Generator:

* Use **Stable Diffusion** from Bedrock for image generation via prompt like:

  ```
  "A futuristic city skyline in sunset, digital art"
  ```

#### 💰 Pricing

* You **only pay for what you use** (tokens in, tokens out).
* No upfront model cost, no GPU management.
* Separate pricing for each model (e.g., Claude vs Titan vs Mistral).

#### ✅ Summary

| Feature                 | Amazon Bedrock                  |
| ----------------------- | ------------------------------- |
| Multi-model access      | ✅ (Claude, LLaMA, Titan, etc.)  |
| Fully managed           | ✅                               |
| Serverless              | ✅                               |
| Security and compliance | ✅ IAM, KMS, VPC                 |
| Training required?      | ❌ No                            |
| Fine-tuning supported   | 🔜 Coming soon (not all models) |
| Use in RAG pipelines    | ✅ Yes                           |

## Here’s a complete **Python example** that uses **Amazon Bedrock** to:

1. Generate **text** from a prompt using **Claude 3**
2. (Optional) Create **embeddings** using **Titan Embeddings**
3. Integrate into a basic **RAG (Retrieval-Augmented Generation)** pipeline

#### ✅ Prerequisites

1. AWS CLI configured (`aws configure`)
2. Python 3.9+
3. Install SDK:

```bash
pip install boto3
```

4. Make sure Bedrock is enabled in your account and region (e.g., `us-east-1`)

#### 🔹 Step 1: Text Generation with Claude 3

```python
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": "Explain what is Retrieval-Augmented Generation (RAG) in simple terms."}
        ]
    })
)

output = json.loads(response['body'].read())
print("Claude says:\n", output['content'][0]['text'])
```

#### 🔹 Step 2: Generate Embeddings (for RAG)

```python
embedder = boto3.client('bedrock-runtime', region_name='us-east-1')

embed_response = embedder.invoke_model(
    modelId="amazon.titan-embed-text-v1",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({"inputText": "How does SageMaker JumpStart help beginners?"})
)

embedding = json.loads(embed_response["body"].read())["embedding"]
print("Vector size:", len(embedding))
```

You can store this embedding in **Amazon OpenSearch**, **Pinecone**, **Faiss**, etc.

#### 🔹 Step 3: Simulated RAG: Search + Prompt Inject

```python
# Simulated document chunks
docs = [
    "SageMaker JumpStart provides pretrained models and solution templates.",
    "It helps users start with machine learning quickly and with minimal code.",
    "You can use models for text, vision, tabular, and more."
]

query = "How does JumpStart help new ML users?"

# Generate embedding for the query
query_embedding = json.loads(embedder.invoke_model(
    modelId="amazon.titan-embed-text-v1",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({"inputText": query})
)["body"].read())["embedding"]

# Simulate similarity scoring (dot product or cosine)
from numpy import dot
from numpy.linalg import norm
import numpy as np

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

# Simulate retrieving top-k documents
similarities = [cosine_similarity(query_embedding, json.loads(embedder.invoke_model(
    modelId="amazon.titan-embed-text-v1",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({"inputText": doc})
)["body"].read())["embedding"]) for doc in docs]

# Get most relevant doc
top_doc = docs[np.argmax(similarities)]

# Inject into Claude
response = bedrock.invoke_model(
    modelId='anthropic.claude-3-sonnet-20240229-v1:0',
    contentType='application/json',
    accept='application/json',
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "content": f"Using the following document:\n\n{top_doc}\n\nAnswer this: {query}"}
        ]
    })
)

output = json.loads(response['body'].read())
print("\nRAG-based answer:\n", output['content'][0]['text'])
```

#### ✅ Summary

| Task                   | Tool/Model                      |
| ---------------------- | ------------------------------- |
| Text generation        | `Claude 3 Sonnet` (Anthropic)   |
| Embedding generation   | `Amazon Titan Embedding`        |
| RAG document retrieval | Your vector DB (simulated here) |

---

## Bedrock RAG API
```py
# app.py - Flask RAG API using Amazon Bedrock

from flask import Flask, request, jsonify
import boto3
import json
import numpy as np
from numpy.linalg import norm

app = Flask(__name__)

REGION = "us-east-1"
EMBED_MODEL = "amazon.titan-embed-text-v1"
GEN_MODEL = "anthropic.claude-3-sonnet-20240229-v1:0"

bedrock = boto3.client("bedrock-runtime", region_name=REGION)

doc_chunks = [
    "SageMaker JumpStart provides pretrained models and solution templates.",
    "It helps users start with machine learning quickly and with minimal code.",
    "You can use models for text, vision, tabular, and more."
]

def get_embedding(text):
    response = bedrock.invoke_model(
        modelId=EMBED_MODEL,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({"inputText": text})
    )
    return json.loads(response["body"].read())["embedding"]

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (norm(a) * norm(b)))

@app.route("/rag", methods=["POST"])
def rag():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "Missing 'query' field"}), 400

    query_embed = get_embedding(query)
    
    scores = [cosine_similarity(query_embed, get_embedding(doc)) for doc in doc_chunks]
    best_doc = doc_chunks[np.argmax(scores)]

    prompt = f"Using the following document:\n\n{best_doc}\n\nAnswer this: {query}"
    response = bedrock.invoke_model(
        modelId=GEN_MODEL,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 300,
            "temperature": 0.7,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        })
    )
    result = json.loads(response['body'].read())
    return jsonify({"response": result['content'][0]['text']})

if __name__ == "__main__":
    app.run(debug=True)

```


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
