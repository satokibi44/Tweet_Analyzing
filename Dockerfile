FROM python:3.9.10-buster

WORKDIR /src

COPY src /src

RUN apt-get update && \
    python -m pip install --upgrade pip && \
    pip install -r requirements.lock

CMD ["python", "bot/main.py"]