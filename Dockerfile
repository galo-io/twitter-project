FROM python:3.10-slim-bullseye

COPY requirements.txt .
COPY paulocamaraflix ./paulocamaraflix
COPY .env .

RUN pip install -r requirements.txt

CMD ["python3", "./paulocamaraflix/main.py"]