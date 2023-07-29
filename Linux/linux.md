# Linux

## How to show package versions available


```
thor@jump_host ~$ sudo yum --showduplicates list ansible
Loaded plugins: fastestmirror, ovl
Repodata is over 2 weeks old. Install yum-cron? Or run: yum makecache fast
Loading mirror speeds from cached hostfile
 * base: ftpmirror.your.org
 * epel: ord.mirror.rackspace.com
 * extras: mirror.genesisadaptive.com
 * updates: mirror.usi.edu
Available Packages
ansible.noarch                                                                       2.9.17-1.el7   
```


This command will show if any other ansible package version is available in case you want to download and install a previous version of ansible


