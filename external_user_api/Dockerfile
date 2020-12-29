FROM python:3.6-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

COPY external_user_api/external_user_api.py .
CMD pipenv run uvicorn external_user_api:app --port 8080 --host 0.0.0.0
