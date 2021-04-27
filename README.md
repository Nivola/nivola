# Nivola
Nivola is a platform that semplify the use of cloud service from public administration.
Nivola Platform is realized from CSI Piemonte and provides computational, storage and network resources.

## Product and Components
This project contains the Product **nivola**.
The product contains some components:
* [beecell](https://github.com/Nivola/beecell)
* [beedrones](https://github.com/Nivola/beedrones)
* [beehive](https://github.com/Nivola/beehive)
* beehive-oauth2
* beehive-resource
* beehive-service
* beehive-ssh
* beehive3-cli
* beehive-mgmt


## Installing Cloud Management Platform (CMP)

### Prerequisites
Have installed a MySql database and a Elasticsearch server.
CMP deployment using the Kubernetes command-line tool, kubectl.
Move to folder nivola/deploy/k8s

### Core components creation
Creation of namespace and api exposure services of the components of the cmp
Replace <WORKSPACE> in nivola/deploy/k8s/core/mylab/beehive-volume.yml 
launch:
```
$ kubectl create -k core/mylab
```

### Creation of engines used by cmp
Creation of engines such as redis, rabbitmq, proxysql
launch:
```
$ kubectl create -k engine/mylab
```

### Build CMP Docker image
docker image build --tag nivola/nivola-uwsgi -f nivola/deploy/k8s/Dockerfile.uwsgi-py3 .

docker image build --build-arg GITUSER=<USER> --build-arg GITPWD=<PASSWORD> --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .



### Auth component creation
Auth is the fundamental component that implements all the authentication and authorization api and makes available the endpoint catalogs of all the api. It is a central component that is used from other components and external users.

#### Schema and user creation on mariadb
To continue, the cli must be installed.
```
beehive3 platform mysql dbs add auth 
beehive3 platform mysql dbusers add auth auth 
beehive3 platform mysql dbusers grant auth auth 
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create auth pkgs/beehive-ansible/beehive_ansible/subsystems/auth.yml

beehive3 platform cmp subsystems create auth pkgs/nivola/deploy/k8s/subsystems/auth.yml
```



## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use Semantic Versioning for versioning. (https://semver.org)

Current version is: 1.8.2

## Authors
See the list of contributors who participated in this project in the file AUTHORS.md contained in each specific project.

## Copyright
CSI Piemonte - 2018-2019

CSI Piemonte - 2019-2020

CSI Piemonte - 2020-2021

## License
See the LICENSE.txt file contained in each specific project for details.

## Community site (Optional)
At https://www.nivolapiemonte.it/ could find all the informations about the project.
