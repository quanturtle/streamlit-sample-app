```
# install nginx
sudo apt install nginx

# create new server block
cd /etc/nginx/sites-enabled/

sudo vi <server_block_name>
```

inside the file `server_block_name`, add
```
server {
    listen <port>;
    server_name <ip_addr or domain_name>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

```
# check nginx syntax is ok
sudo nginx -t

# restart nginx service
sudo service nginx restart
```
