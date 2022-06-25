# Basic Streamlit app, dockerized with nginx reverse-proxy

Install `nginx`
```
sudo apt install nginx
```

Build container
```
sudo docker build -t streamlit .
```

Run container
```
sudo docker run -p 127.0.0.1:420:420 streamlit
```
