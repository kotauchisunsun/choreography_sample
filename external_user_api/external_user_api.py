from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
import dataclasses
import uuid
import json
import pika
import os
import time

MQ_HOST = os.environ['MQ_HOST']
EXCHANGE = os.environ['EXCHANGE']

class UserInput(BaseModel):
    name: str
    email: EmailStr

app = FastAPI()

params = pika.ConnectionParameters(
            host=MQ_HOST,
            heartbeat=600,
            blocked_connection_timeout=300,
            connection_attempts=5,
            retry_delay=3
)


connection = pika.BlockingConnection(
    params
)
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')

@app.post("/external_users/")
async def create_user(user_input: UserInput) -> None:
    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key="create_user",
        body=user_input.json()
    )

@app.delete("/external_users/{user_id}")
async def delete_user(user_id: str) -> None:
    channel.basic_publish(
        exchange=EXCHANGE,
        routing_key="delete_user",
        body=json.dumps({"user_id": user_id})
    )