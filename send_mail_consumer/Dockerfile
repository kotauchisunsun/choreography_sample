FROM python:3.6-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

COPY send_mail_consumer/send_mail_consumer.py .
CMD pipenv run python send_mail_consumer.py