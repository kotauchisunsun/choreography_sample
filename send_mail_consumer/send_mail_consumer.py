import pika
import time
import smtplib
from email.mime.text import MIMEText
import json
import os

MQ_HOST = os.environ['MQ_HOST']
EXCHANGE = os.environ['EXCHANGE']
MAIL_HOST = os.environ['MAIL_HOST']
MAIL_PORT = int(os.environ['MAIL_PORT'])
QUEUE_NAME = os.environ['QUEUE_NAME']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=MQ_HOST,
        connection_attempts=5,
        retry_delay=3
    )
)
channel = connection.channel()

server = smtplib.SMTP(MAIL_HOST,1025)

queue_name = QUEUE_NAME
print(queue_name)

channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
result = channel.queue_declare(queue=queue_name,durable=True)

channel.queue_bind(
    exchange=EXCHANGE,
    queue=queue_name,
    routing_key="create_user"
)

def callback(ch, method, properties, body):
    # 送受信先
    to_email = "user@email.com"
    from_email = "admin@service.com"

    data = json.loads(body)
    
    # MIMETextを作成
    message = f"User: {data['name']} is Created."
    msg = MIMEText(message, "html")
    msg["Subject"] = "Subject"
    msg["To"] = data['email']
    msg["From"] = from_email


    server.send_message(msg)
    print("SendMail[x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
