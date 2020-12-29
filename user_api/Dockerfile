FROM python:3.6-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

COPY user_api/user_api.py .
CMD pipenv run uvicorn user_api:app --port 8080 --host 0.0.0.0
