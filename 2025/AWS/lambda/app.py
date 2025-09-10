import os

import requests
from requests import Response

from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utitlies.idempotency import DynamoDBPersistenceLayer, IdempotencyConfig, idempotent_function
from aws_lambda_powertools.utilities.parser import BaseModel, Field
from aws_lambda_powertools.utilities.typing import LambdaContext


logger = Logger(service="items")
tracer = Tracer(service="items")
metrics = Metrics(namespace="ItemsService", service="items")
app = APIGatewayRestResolver()

idempotency_storage = DynamoDBPersistenceLayer(table_name=os.getenv("IDEMPOTENCY_TABLE_NAME"))
idempotency_config = IdempotencyConfig(
    event_key_jmespath="body",
    persistence_store=idempotency_storage,
    use_local_cache=True,
    expiration_seconds=300,
)   

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    tax: float = Field(..., gt=0)
    

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/items")
@tracer.capture_method
def post_items():
    item: Item = Item(**app.current_event.json_body)
    logger.append_keys(item_name=item.name)
    
    return {
        "item": item.model_dump(),
        "message": "Item received successfully"
    }


@metrics.log_metrics(capture_cold_start_metric=True)
@logger.inject_lambda_context(correlation_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_method
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)