for disabling `ssh` password authentication
```
cd /etc/ssh/
vi sshd_config
```
change the following lines
```
#Port 22
PasswordAuthentication yes
PermitRootLogin yes
```

```
Port 69
PasswordAuthentication no
PermitRootLogin no
```

restart ssh daemon
```
systemctl restart sshd
```
