```
# download let's encrypt client
sudo apt-get install certbot python3-certbot-nginx

# obtain SSL/TLS certificate
sudo certbot --nginx -d <domain_name>

# file in /etc/nginx/conf.d/<domain_name>.conf should have changed
```

```
# automatically renew certificates
crontab -e
```

inside `crontab`
```
0 0 * * * /usr/bin/certbot renew --quiet
```
