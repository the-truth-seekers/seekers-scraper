FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY install-pyodbc.sh .

RUN mkdir -p out/log && \
    chmod 777 install-pyodbc.sh && \
    bash /app/install-pyodbc.sh

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT extracao_to_bucket.sh
# CMD ["scrapy", "crawl", "news_text"]