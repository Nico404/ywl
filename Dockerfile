FROM --platform=linux/amd64 python:3.10.6-buster

WORKDIR /prod

# First, pip install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --upgrade pip
RUN pip install .

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
