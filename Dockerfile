FROM python:3.11

ENV TZ=America/Sao_Paulo

WORKDIR /app

COPY . .
COPY cron-file /etc/cron.d/cron-file

RUN apt-get update && apt-get -y install cron

RUN chmod +x extracao_to_bucket.sh && \
    chmod 0644 /etc/cron.d/cron-file && \
    crontab /etc/cron.d/cron-file

RUN mkdir -p out/log && \
    chmod 777 install-pyodbc.sh && \
    bash /app/install-pyodbc.sh

RUN pip install --no-cache-dir -r requirements.txt

CMD cron -f