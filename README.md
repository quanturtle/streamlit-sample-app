# Basic Streamlit app, with Docker and Nginx reverse-proxy

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
sudo docker run -d -p 127.0.0.1:420:420 streamlit
```

## Notes
There were issues related to websockets not functioning properly. Specifically, this [issue (#2)](https://docs.streamlit.io/knowledge-base/deploy/remote-start). **Solved**: upgrade `nginx`, `http` headers were being stripped.

If you want to add SSL (you should), install `certbot`
```
sudo apt-get install python3-certbot-nginx
sudo certbot --nginx <-d:domain> <domain_name> 
```  
Issues may arise, check `CORS` protection and `XSRF` protection in case of errores with certificates
