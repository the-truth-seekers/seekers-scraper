FROM python:3.11-slim

ENV TZ=America/Sao_Paulo

WORKDIR /app

COPY . .
# COPY cron-file /etc/cron.d/cron-file

RUN apt-get update && apt-get -y install cron

RUN chmod +x extracao_to_bucket.sh
# RUN chmod 0644 /etc/cron.d/cron-file
# RUN crontab /etc/cron.d/cron-file

RUN mkdir -p /app/out/log

RUN apt-get update -y && apt-get install -y curl gnupg gnupg1 gnupg2 wget apt-transport-https

RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN echo "deb [arch=amd64] https://packages.microsoft.com/debian/11/prod bullseye main" > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -y
RUN apt-get install -y unixodbc-dev libgssapi-krb5-2

ENV PATH="$PATH:/opt/mssql-tools18/bin"

RUN apt-get update -y
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT bash -c ./extracao_to_bucket.sh
# CMD cron -f