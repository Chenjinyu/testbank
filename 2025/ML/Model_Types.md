## Transformer Model (LLM)
Example: Google BERT, OpenAI ChatGPT.
(ChatGPT = Chat Generative Pretrained Transformer)
## Diffusion Model 

## Multi-Modal Models (ex: GPT-4o)




## ML Term You May Encounter in the Exam
- GPT (Generative Pre-trained Transformer) - generate human text or computer code based on input prompts
- BERT (Bidirectional Encoder Representations form Transformer) - similar intent to GPT, but reads the text in two directions. 
- RNN (Recurrent Neural Network) - meant for sequential data such as time-series or text, useful in speech recognition, time-series prediction
- ResNet(Residual Network) - Deep Convolutional Neural Network (CNN) used for image recognition tasks, object detection, facial recognition
- SVM (Support Vector Machine) - ML algorithm for classficiation and regiression
- WaveNet - model to generate raw audio waveform, used in speech Synthesis
- GAN (Generative Adversarial Network) - models used to generate synthetic data such as image, videos or sounds that resemble the traiming data. Helpful for data augmentation
-  XGBoost(eXtreme Gradient Boosting) - an implemntation of gradient boosting 


## ✅ What is **XGBoost**?

**XGBoost** (e**X**treme **G**radient **Boost**ing) is a **high-performance machine learning algorithm** used primarily for:

* **Classification** (e.g., spam detection, churn prediction)
* **Regression** (e.g., price prediction)
* **Ranking** (e.g., search engine results)

It’s one of the most popular algorithms in data science competitions (like Kaggle) because it's:

* **Fast**
* **Accurate**
* **Efficient** (handles missing values, works well with tabular data)

> XGBoost is based on **gradient boosting**, which builds decision trees **sequentially**, each trying to correct errors from the previous one.

#### 🎯 What Is XGBoost Used For?

| Use Case                   | Example                                     |
| -------------------------- | ------------------------------------------- |
| Binary Classification      | Will this customer buy or not? (`0` or `1`) |
| Multi-class Classification | What product category will a user click?    |
| Regression                 | Predict house prices, stock value, etc.     |
| Ranking                    | Rank search results, recommend top products |
| Tabular Data Modeling      | Any structured data (CSV, SQL, etc.)        |

#### 📦 What Does `xgb.deploy()` Do?

When you run this:

```python
predictor = xgb.deploy(initial_instance_count=1, instance_type="ml.m5.large")
```

It does **ALL of this for you**:

| Step                                  | Explanation                                                        |
| ------------------------------------- | ------------------------------------------------------------------ |
| 1️⃣ Create a **Model Artifact**       | Packages your trained model                                        |
| 2️⃣ Spin up an **Inference Endpoint** | Launches an HTTPS API hosted in **SageMaker**                      |
| 3️⃣ Launch a **Server (container)**   | A container (using the XGBoost image) runs on an EC2-like instance |
| 4️⃣ Returns a `predictor` object      | You can now call `predictor.predict()` with your data              |

> The **endpoint is hosted in SageMaker**, and you can call it from other apps via REST API or SDK.

#### 💡 What’s Under the Hood?

Behind this line:

```python
predictor = xgb.deploy(...)
```

SageMaker:

* Uploads your model to **S3**
* Creates a **Model** in SageMaker
* Launches an **EndpointConfig**
* Creates a **real-time HTTPS endpoint** backed by EC2 instance(s)
* Manages **auto-scaling, health checks, SSL, etc.**

#### 🔐 Accessing the Endpoint

Once deployed, it’s accessible via:

* Python SDK (`predictor.predict(...)`)
* HTTPS REST call (via API Gateway or directly)
* Other apps (Java, JS, etc.)

#### 🧹 Don’t Forget to Delete

After you're done, to stop paying for the instance:

```python
predictor.delete_endpoint()
```

#### ✅ Summary

| Term           | Meaning                                                                    |
| -------------- | -------------------------------------------------------------------------- |
| **XGBoost**    | Fast ML algorithm for classification/regression on structured/tabular data |
| **Used for**   | Predicting categories, values, and rankings                                |
| **`deploy()`** | Creates a live **SageMaker-hosted API endpoint** for real-time inference   |


## Here's how you can invoke a **SageMaker real-time inference endpoint** (created via `xgb.deploy(...)`) **from outside SageMaker**, such as with `curl`, Postman, or from a web app using API Gateway.

#### 🎯 Goal

You want to:

1. Access the SageMaker endpoint securely from the internet or external apps
2. Authorize requests using AWS credentials or API Gateway
3. Call the endpoint using `curl` or HTTP

###### ✅ Option 1: Directly Call SageMaker Endpoint Using `boto3` (from any machine with AWS credentials)

```python
import boto3
import json

client = boto3.client("sagemaker-runtime")

response = client.invoke_endpoint(
    EndpointName="your-endpoint-name",
    Body="30,60000,Female",  # comma-separated input
    ContentType="text/csv"
)

result = response['Body'].read().decode()
print("Prediction:", result)
```

✅ You need:

* AWS credentials (e.g., via `~/.aws/credentials`)
* Permissions for `sagemaker:InvokeEndpoint`

#### ❌ You **cannot** call the endpoint directly over HTTP from the internet unless you go through **Amazon API Gateway** or another secure interface.

#### ✅ Option 2: Expose the Endpoint via **API Gateway**

##### 🔧 Step-by-step:

###### 1. Create a Lambda Wrapper Function

```python
import boto3

def lambda_handler(event, context):
    client = boto3.client("sagemaker-runtime")
    payload = event["body"]  # expects raw CSV string

    response = client.invoke_endpoint(
        EndpointName="your-endpoint-name",
        Body=payload,
        ContentType="text/csv"
    )

    result = response['Body'].read().decode()
    return {
        "statusCode": 200,
        "body": result
    }
```
###### 2. Create API Gateway (HTTP API or REST API)

* Trigger the Lambda via HTTP POST
* Enable **CORS** if calling from a browser
* Set **authentication** (IAM, JWT, or public for testing only)

###### 3. Deploy and Test

You’ll get a public endpoint like:

```
https://abc123.execute-api.us-east-1.amazonaws.com/predict
```

Then use `curl`:

```bash
curl -X POST https://abc123.execute-api.us-east-1.amazonaws.com/predict \
     -H "Content-Type: text/csv" \
     -d "30,60000,Female"
```

Or use Postman, Python requests, frontend app, etc.

#### ✅ Summary Table

| Method                       | Publicly Accessible? | Secure? | Best Use Case                         |
| ---------------------------- | -------------------- | ------- | ------------------------------------- |
| `boto3` SDK                  | ❌ No                 | ✅ Yes   | From EC2, Lambda, or AWS environments |
| Direct HTTPS to endpoint URL | ❌ No                 | ✅ Yes   | For internal AWS use                  |
| API Gateway + Lambda         | ✅ Yes                | ✅ Yes   | For public or cross-app access        |

