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

## Below are the AWS CloudFormation template to expose the SageMaker endpoint through API Gateway using a Lambda functon, it:
* Accepts POST requests at `/predict`
* Uses Lambda to call the SageMaker endpoint
* Requires only your endpoint name as a parameter

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Expose SageMaker endpoint via API Gateway and Lambda

Parameters:
  SageMakerEndpointName:
    Type: String
    Description: Name of the deployed SageMaker endpoint

Resources:
  SageMakerInvokeLambdaRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: SageMakerInvokeLambdaRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: SageMakerInvokePolicy
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - sagemaker:InvokeEndpoint
                Resource: '*'
              - Effect: Allow
                Action:
                  - logs:CreateLogGroup
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                Resource: '*'

  SageMakerInvokeLambda:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: SageMakerInvokeLambda
      Runtime: python3.11
      Role: !GetAtt SageMakerInvokeLambdaRole.Arn
      Handler: index.lambda_handler
      Timeout: 30
      Code:
        ZipFile: |
          import boto3
          import json

          def lambda_handler(event, context):
              runtime = boto3.client('sagemaker-runtime')
              payload = event.get('body', '')
              response = runtime.invoke_endpoint(
                  EndpointName='{{resolve:ssm:/sagemaker/endpoint/name}}',  # or replace with actual name
                  ContentType='text/csv',
                  Body=payload
              )
              result = response['Body'].read().decode()
              return {
                  'statusCode': 200,
                  'headers': {"Content-Type": "application/json"},
                  'body': json.dumps({'prediction': result})
              }

  SageMakerAPI:
    Type: AWS::ApiGatewayV2::Api
    Properties:
      Name: SageMakerInferenceAPI
      ProtocolType: HTTP

  SageMakerAPIRoute:
    Type: AWS::ApiGatewayV2::Route
    Properties:
      ApiId: !Ref SageMakerAPI
      RouteKey: "POST /predict"
      Target: !Join
        - /
        - - integrations
          - !Ref SageMakerAPIIntegration

  SageMakerAPIIntegration:
    Type: AWS::ApiGatewayV2::Integration
    Properties:
      ApiId: !Ref SageMakerAPI
      IntegrationType: AWS_PROXY
      IntegrationUri: !Sub
        arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${SageMakerInvokeLambda.Arn}/invocations
      PayloadFormatVersion: '2.0'

  SageMakerAPIDeployment:
    Type: AWS::ApiGatewayV2::Deployment
    DependsOn:
      - SageMakerAPIRoute
    Properties:
      ApiId: !Ref SageMakerAPI

  SageMakerAPIStage:
    Type: AWS::ApiGatewayV2::Stage
    Properties:
      ApiId: !Ref SageMakerAPI
      DeploymentId: !Ref SageMakerAPIDeployment
      StageName: prod

  LambdaInvokePermission:
    Type: AWS::Lambda::Permission
    Properties:
      FunctionName: !Ref SageMakerInvokeLambda
      Action: lambda:InvokeFunction
      Principal: apigateway.amazonaws.com
      SourceArn: !Sub arn:aws:execute-api:${AWS::Region}:${AWS::AccountId}:${SageMakerAPI}/*/*

```
## Below are the Terraform template to expose a SageMaker endpoint via API Gateway and Lambda, with CORS and environment variable configuration.
To finish setup:
- Zip your index.py Lambda function (same logic as before) into lambda.zip.
- Run terraform apply -var='sagemaker_endpoint_name=YourEndpointName'.
```tf
# Terraform version of CloudFormation for exposing SageMaker endpoint via API Gateway + Lambda

provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

variable "sagemaker_endpoint_name" {
  description = "Name of the SageMaker endpoint"
  type        = string
}

resource "aws_iam_role" "lambda_exec_role" {
  name = "SageMakerInvokeLambdaRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "lambda.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })

  inline_policy {
    name = "InvokeSageMaker"
    policy = jsonencode({
      Version = "2012-10-17",
      Statement = [
        {
          Effect   = "Allow",
          Action   = ["sagemaker:InvokeEndpoint"],
          Resource = "*"
        },
        {
          Effect = "Allow",
          Action = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
          Resource = "*"
        }
      ]
    })
  }
}

resource "aws_lambda_function" "invoke_sagemaker" {
  function_name = "SageMakerInvokeLambda"
  role          = aws_iam_role.lambda_exec_role.arn
  runtime       = "python3.11"
  handler       = "index.lambda_handler"

  filename         = "lambda.zip" # You need to zip and upload the Python handler
  source_code_hash = filebase64sha256("lambda.zip")
  timeout          = 30

  environment {
    variables = {
      SAGEMAKER_ENDPOINT = var.sagemaker_endpoint_name
    }
  }
}

resource "aws_apigatewayv2_api" "sagemaker_api" {
  name          = "SageMakerInferenceAPI"
  protocol_type = "HTTP"
  cors_configuration {
    allow_headers = ["Content-Type", "X-API-Key"]
    allow_methods = ["OPTIONS", "POST"]
    allow_origins = ["*"]
  }
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.invoke_sagemaker.arn
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.sagemaker_api.execution_arn}/*/*"
}

resource "aws_apigatewayv2_integration" "sagemaker_integration" {
  api_id           = aws_apigatewayv2_api.sagemaker_api.id
  integration_type = "AWS_PROXY"
  integration_uri  = aws_lambda_function.invoke_sagemaker.invoke_arn
  integration_method = "POST"
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "sagemaker_route" {
  api_id    = aws_apigatewayv2_api.sagemaker_api.id
  route_key = "POST /predict"
  target    = "integrations/${aws_apigatewayv2_integration.sagemaker_integration.id}"
}

resource "aws_apigatewayv2_stage" "prod" {
  api_id      = aws_apigatewayv2_api.sagemaker_api.id
  name        = "prod"
  auto_deploy = true
}

resource "aws_apigatewayv2_api_mapping" "usage_plan" {
  api_id      = aws_apigatewayv2_api.sagemaker_api.id
  stage       = aws_apigatewayv2_stage.prod.id
}

output "api_url" {
  value = "${aws_apigatewayv2_api.sagemaker_api.api_endpoint}/predict"
}

```

## index.py Lambda to handle the script
Here is the `index.py` Lambda handler script that wraps your SageMaker endpoint:
```py
import boto3
import json
import os

runtime = boto3.client('sagemaker-runtime')
endpoint_name = os.environ['SAGEMAKER_ENDPOINT']

def lambda_handler(event, context):
    # Support both test event and real API Gateway input
    body = event.get("body", "")
    if isinstance(body, dict):
        payload = json.dumps(body)
    else:
        payload = body

    try:
        response = runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='text/csv',  # Adjust to 'application/json' if your model expects JSON
            Body=payload
        )

        result = response['Body'].read().decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST",
                "Access-Control-Allow-Headers": "Content-Type,X-API-Key"
            },
            "body": json.dumps({"prediction": result})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

```

#### 📦 Instructions to Package and Deploy

1. Save the code above as `index.py`.
2. Run the following to package it:

```bash
zip lambda.zip index.py
```

3. Place `lambda.zip` in the same directory as your Terraform file, then run:

```bash
terraform apply -var='sagemaker_endpoint_name=YourEndpointName'
```
