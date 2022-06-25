FROM python:3.8-slim-buster

RUN pip install --upgrade pip
RUN apt-get update -y

COPY . /app
WORKDIR /app

EXPOSE 420

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port", "420", "--server.address", "0.0.0.0"]
