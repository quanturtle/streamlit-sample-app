```
# install OpenSSL
sudo apt install openssl

# create new directory inside nginx
cd /etc/nginx && sudo mkdir ssl

# create self-signed certificate
sudo openssl req -batch -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/server.key
-out /etc/nginx/ssl/server.crt
```

add this to server block configuration
```
cd /etc/nginx/sites-enabled/
sudo vi <server_block>
```

`<server_block>`
```
server {
    listen <port:80>;
    listen <port:443> ssl;
    ssl on;
    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    server_name <ip_addr or domain_name>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

restart `nginx` daemon
```
sudo service nginx restart
```
