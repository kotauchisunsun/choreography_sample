FROM python:3.6-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

WORKDIR /root
COPY delete_user_consumer/delete_user_consumer.py .
COPY client/openapi_client openapi_client
CMD pipenv run python delete_user_consumer.py