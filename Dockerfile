FROM python:3

WORKDIR /crm_service

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
