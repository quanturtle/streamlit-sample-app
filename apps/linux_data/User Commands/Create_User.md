```
# create user
sudo useradd <username>

# add password
sudo passwd <username>

# create a non root user with sudo priv, home folder and bash terminal
sudo useradd -G sudo -m <username> -s /bin/bash
```