FROM python:3.6-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
RUN pipenv install

CMD bash