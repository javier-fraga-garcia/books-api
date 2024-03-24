FROM python:3.9.19-slim-bullseye

RUN apt-get update && \
    apt-get upgrade && \
    python3 -m pip install --upgrade pip && \
    apt-get -y install libpq-dev gcc 

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV DB_URL=postgresql://user:password@host:port/db
ENV PORT=8000

EXPOSE ${PORT}

CMD uvicorn main:app --host=0.0.0.0 --port="$PORT"