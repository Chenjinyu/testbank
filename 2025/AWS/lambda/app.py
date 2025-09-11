import os

import requests
from requests import Response

from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.idempotency import DynamoDBPersistenceLayer, IdempotencyConfig, idempotent_function
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.utilities.parser import BaseModel, Field
from aws_lambda_powertools.utilities.typing import LambdaContext


logger = Logger(service="items")
tracer = Tracer(service="items")
metrics = Metrics(namespace="ItemsService", service="items")
app = APIGatewayRestResolver()

idempotency_storage = DynamoDBPersistenceLayer(table_name=os.environ["IDEMPOTENCY_TABLE_NAME"])
idempotency_config = IdempotencyConfig(
    event_key_jmespath="body",
    use_local_cache=True,
    expires_after_seconds=300,
)   

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=500)
    price: float = Field(..., gt=0)
    tax: float = Field(..., gt=0)
    

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/items")
@tracer.capture_method
def post_items():
    item: Item = Item(**app.current_event.json_body)
    # custom fields to every log entry makes it easier to search and filter in CloudWatch
    logger.append_keys(item_name=item.name)
    
    return {
        "item": item.model_dump(),
        "message": "Item received successfully"
    }

@idempotent_function(data_keyword_argument="item", config=idempotency_config, persistence_store=idempotency_storage)
def create_item(item: Item):
    logger.info("Creating item in the database (simulated)")
    API_KEY = parameters.get_secret(name="item-api-key", max_age=300)    
    
    new_item: Response = requests.post("", data=item.dict(), headers={"x-api-key": API_KEY})
    # it uses the request libray, and it is part of the Response object,
    # it checks the HTTP status code of the response, and if it is 4xx or 5xx,
    # it raises an HTTPError exception.
    # 200-398 are considered successful responses.
    # client error 4xx, server side error 5xx raise HTTPError.
    new_item.raise_for_status()
    
    logger.info(" Item created successfully (simulated)")
    metrics.add_metric(name="ItemCreated", unit=MetricUnit.Count, value=1)
    
    return item.json()


@metrics.log_metrics(capture_cold_start_metric=True)
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_method
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)