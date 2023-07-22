FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip

# Install build dependencies for building Python extensions
RUN apt-get update && \
    apt-get install -y gcc

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]
