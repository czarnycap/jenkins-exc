##09-Nov-22
create first fastapi(python app)
you could run it by using uvicorn python web server
```~/.local/bin/uvicorn myfirstapi:app --reload --host 0.0.0.0```
you could access it here -> http://192.168.16.154:8000/my-first-api?name=adam

trying to run build node.js application from wardviaene/docker-demo github (udemy course on jenkins)

modified compose to have 2nd postgres for sonarqube and sonarqube
changed system settings to allow start of sonarqube 
```sysctl -w vm.max_map_count=262144```
```echo "vm.max_map_count=262144" >> /etc/sysctl.conf``` 
created volume for atrifactory 
```docker volume create --name=artifactory_data```
fixed issue with port jdbc (just a typo) so sonarqube could connect to postregss
fixed issue with connection to postgres (typo in env name)

##08-Nov-22 (tuesday)
[python continuos integration tutorial](https://realpython.com/python-continuous-integration/)
[markdown](https://www.geeksforgeeks.org/introduction-to-markdown/)

##07-Nov-22 (Monday)
#ansible
cloned VMs (xubuntu, centos)
changed hostnames via hostnamesctl
added ansible user via usermod -a -G
used visudo to allow ansible user to change into root without password
wrote first playbook to install "emacs" via apt or yum (respectively of the version of OS)
changed .ssh/config files to allow for easier ssh connection
deployed id_rsa.pub keys to remote machines to allow connections without password
wrote playbook_remove_emacs 
wrote playbok_hostname with debug input from hostname command

#jenkins
installed jenkins
set pw/user
created and compiled simple ansi c app (
```gcc -o calc.app calculator.c -lm```
installed postgress (docker compose) with new docker volume


[ansible examples](https://www.toptechskills.com/ansible-tutorials-courses/ansible-yum-module-tutorial-examples/)