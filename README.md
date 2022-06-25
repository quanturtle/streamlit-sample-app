# Basic Streamlit app, dockerized with nginx reverse-proxy

Install `nginx` and copy config file
```
sudo apt install nginx
sudo cp streamlit_nginx.conf /etc/nginx/sites-enabled/
sudo service nginx restart
```

Build container
```
sudo docker build -t streamlit .
```

Run container
```
sudo docker run -p 127.0.0.1:420:420 streamlit
```

## Notes

There were issues related to websockets not functioning properly. Specifically, this [issue (#2)](https://docs.streamlit.io/knowledge-base/deploy/remote-start). **Solved**: upgrade `nginx`, `http` headers were being stripped.
