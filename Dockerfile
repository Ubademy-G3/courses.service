# pull official base image
FROM python:3.8

# set work directory
WORKDIR /app/

# Actualizar repositorios de apt
RUN apt update

# Copy Datadog configuration
COPY monitoring/ /etc/datadog-agent/

# Install GPG dependencies
RUN apt-get install -y gpg apt-transport-https gpg-agent curl ca-certificates

# Add Datadog repository and signing keys
ENV DATADOG_APT_KEYRING="/usr/share/keyrings/datadog-archive-keyring.gpg"
ENV DATADOG_APT_KEYS_URL="https://keys.datadoghq.com"
RUN sh -c "echo 'deb [signed-by=${DATADOG_APT_KEYRING}] https://apt.datadoghq.com/ stable 7' > /etc/apt/sources.list.d/datadog.list"
RUN touch ${DATADOG_APT_KEYRING}
RUN curl -o /tmp/DATADOG_APT_KEY_CURRENT.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_CURRENT.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_CURRENT.public
RUN curl -o /tmp/DATADOG_APT_KEY_F14F620E.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_F14F620E.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_F14F620E.public
RUN curl -o /tmp/DATADOG_APT_KEY_382E94DE.public "${DATADOG_APT_KEYS_URL}/DATADOG_APT_KEY_382E94DE.public" && \
    gpg --ignore-time-conflict --no-default-keyring --keyring ${DATADOG_APT_KEYRING} --import /tmp/DATADOG_APT_KEY_382E94DE.public

# Install the Datadog Agent
RUN apt-get update && apt-get -y --force-yes install --reinstall datadog-agent

# Expose DogStatsD and trace-agent ports
EXPOSE 8125/udp 8126/tcp
ENV DD_APM_ENABLED=true

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt /app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
        postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /app/

# Ejecutar el script entrypoint.sh
CMD ["sh", "/app/docker-entrypoint-prod.sh"]
