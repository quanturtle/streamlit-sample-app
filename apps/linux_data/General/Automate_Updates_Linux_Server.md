```
# install packages
sudo apt install unattended-upgrades apt-listchanges bsd-mailx

> select Internet Connection

sudo dpkg-reconfigure -plow unattended-upgrades

sudo vi /etc/apt/apt.conf.d/50unattended-upgrades
```

change line so that server sends an email when updating
```
#Unattended-Upgrade::Mail "";
#Unattended-Upgrade::Automatic-Reboot "false";
#Unattended-Upgrade::Automatic-Reboot-Time "2:00";
```

```
Unattended-Upgrade::Mail "<email>"
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "5:00";
```

test
```
sudo unattended-upgrades --dry-run
```
