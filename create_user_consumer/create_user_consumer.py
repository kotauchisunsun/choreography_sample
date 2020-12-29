import pika
import time
import os
import json

MQ_HOST = os.environ['MQ_HOST']
EXCHANGE = os.environ['EXCHANGE']
QUEUE_NAME = os.environ['QUEUE_NAME']
API_HOST = os.environ['API_HOST']

print("start create_user_consumer")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=MQ_HOST,
        connection_attempts=5,
        retry_delay=3
    )
)
channel = connection.channel()

queue_name = QUEUE_NAME
print(queue_name)

channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
result = channel.queue_declare(queue=queue_name,durable=True)

channel.queue_bind(
    exchange=EXCHANGE, 
    queue=queue_name, 
    routing_key="create_user"
)



import openapi_client
from pprint import pprint
from openapi_client.api import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.user_input import UserInput

configuration = openapi_client.Configuration(
    host = API_HOST
)

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    data = json.loads(body)

    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = default_api.DefaultApi(api_client)
        user_input = UserInput(
            name=data["name"],
            email=data["email"],
        ) # UserInput | 

        try:
            # Create User
            api_response = api_instance.create_user_users_post(user_input)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling DefaultApi->create_user_users_post: %s\n" % e)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()