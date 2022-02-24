FROM python:3.10-alpine

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
VOLUME [ "/app" ]

CMD ["python", "src/coinbase/main.py"]