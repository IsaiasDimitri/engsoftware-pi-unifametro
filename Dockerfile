FROM python:3.8.6-slim-buster

ARG DJANGO_ENV

ENV DJANGO_ENV=${DJANGO_ENV} \
    # python
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random

# system deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for building python deps
    build-essential \
    # cleaning cache
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x '/docker-entrypoint.sh'

CMD ["/docker-entrypoint.sh"]