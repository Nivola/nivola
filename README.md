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
* [beehive3-cli](https://github.com/Nivola/beehive3-cli)


## Installing Cloud Management Platform (CMP)

### Prerequisites
- You must have already downloaded the projects beecell, beedrones, beehive.
- You must have the CLI already installed
- You must have "minikube" installed
- Install a MySql/MariaDB database (MySql version > 5.7, MariaDB version > 10.5)
- Install Elasticsearch server where write logs.
- CMP deployment using the Kubernetes command-line tool, kubectl.
- Install Docker for building images.
- Move to folder nivola/deploy/k8s

### Minikube start
Start your minikube with the docker driver, replacing <WORKSPACE> with folder where you downloaded projects
We suggest that minikube process starts in a docker network "nivolanet" for being reachable from CLI and Nginx.
```
$ minikube start --driver=docker --cpus=4 --mount=true --mount-string="<WORKSPACE>:/pkgs" --network nivolanet
```

To obtail minikube IP launch:
```
$ minikube ip
```


### Nginx installation and update CLI configuration


### Core components creation
Creation of namespace and api exposure services of the components of the cmp
In nivola/deploy/k8s/core/mylab/beehive-volume.yml look at "hostPath".
If you start minikube with --driver=none replace <WORKSPACE> with your project folder
otherwise mount your workspace passing to minikube '--mount=true --mount-string="<WORKSPACE>:/pkgs" '

Launch:
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
In deploy directory __beehive3_cli/deploy__ you find dockerfiles.
Build docker image "nivola/nivola-uwsgi":
```
docker image build --tag nivola/nivola-uwsgi -f nivola/deploy/k8s/Dockerfile.uwsgi-py3 .
```

Build docker image "nivola/cmp" that start from image "nivola/nivola-uwsgi"
or downloading projects into image and passing git user/password

```
docker image build --build-arg GITUSER=<USER> --build-arg GITPWD=<PASSWORD> --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
```

or copying projects into image (in this case you have to go to folder where you downloaded projects)

```
docker image build --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
```

NOTE: image "nivola/cmp" is referenced in k8s files used below
If you start minikube with --driver=docker
you can upload image to a docker registry and update references in kubernates files auth/mylab.yml...
or save your image in a file and then load it in minikube docker:
```
docker save nivola/cmp:latest > $HOME/nivola_cmp_latest.tar
eval $(minikube docker-env)
docker load < $HOME/nivola_cmp_latest.tar
docker images
```
In both cases, check also imagePullPolicy


### Auth component creation
Auth is the fundamental component that implements all the authentication and authorization api and makes available the endpoint catalogs of all the api. It is a central component that is used from other components and external users.

Schema and user creation on db
To continue, the cli must be installed.
```
beehive3 platform mysql dbs add auth 
beehive3 platform mysql dbusers add auth auth 
beehive3 platform mysql dbusers grant auth auth 
```

Data population on the database and registration of permissions on some entities
```
# to create Auth tables
beehive3 platform cmp subsystems create auth pkgs/beehive-ansible/beehive_ansible/subsystems/auth.yml
```

Starting deployment.app on the k8s cluster
Update in auth/mylab/mylab.yml the following properties with reference to your hosts:
- ELASTIC_NODES
- MYSQL_URI
- OAUTH2_ENDPOINT
```
kubectl create -f auth/mylab
```

Test deployment.app on the k8s cluster
```
kubectl get pod -n beehive-mylab -o wide
kubectl describe pod ... -n beehive-mylab
kubectl logs ... -n beehive-mylab -f
```

Console api test
```
beehive3 auth users get
beehive3 auth users get -id admin@local
beehive3 auth roles get
beehive3 catalogs get
```

Perform some customize
- copy nivola/deploy/customization/oauth2.yml /tmp

```
beehive3 auth roles add test-role -desc desc-test-role
beehive3 auth users add -email name.surname@domain.com -password xxxxxxxxx name.surname@domain.it

# oauth2 client
beehive3 platform cmp customize run oauth2 
```

Assign the ApiSuperAdmin role to the oauth2 client that you use for server to server communication.
```
beehive3 auth users add-role client-beehive@local ApiSuperAdmin
```

Update the customization files for the various modules by setting the client uuid and the secret. Client data can be obtained with the command:
```
beehive3 auth oauth2-clients get -id client-beehive
```



### Event component creation

Schema and user creation on db
```
beehive3 platform mysql dbs add event 
beehive3 platform mysql dbusers add event event 
beehive3 platform mysql dbusers grant event event 
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create event pkgs/nivola/deploy/customization/event.yml
```

Starting deployment.app on the k8s cluster
Update in auth/mylab/mylab.yml the following properties with reference to your hosts:
- ELASTIC_NODES
- MYSQL_URI
- OAUTH2_ENDPOINT
```
kubectl create -f event/mylab
```

Test deployment.app on the k8s cluster
```
kubectl get pod -n beehive-mylab -o wide
kubectl describe pod ... -n beehive-mylab
kubectl logs ... -n beehive-mylab -f
```

Console api test
```
beehive3 auth tokens delete all -y
beehive3 auth users get
beehive3 platform cmp logs api
beehive3 platform cmp logs api-engine auth 
beehive3 platform cmp logs worker-engine auth
beehive3 platform scheduler tasks test auth 
beehive3 platform scheduler tasks get auth
beehive3 platform scheduler tasks trace auth <task id>
beehive3 platform scheduler tasks log auth <task id> 
```



### SSH component creation
Schema and user creation on db
```
beehive3 platform mysql dbs add ssh
beehive3 platform mysql dbusers add ssh ssh
beehive3 platform mysql dbusers grant ssh ssh
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create ssh pkgs/nivola/deploy/customization/ssh.yml
```

Starting deployment.app on the k8s cluster
Update in ssh/mylab/mylab.yml the following properties with reference to your hosts:
- ELASTIC_NODES
- MYSQL_URI
- OAUTH2_ENDPOINT
```
kubectl create -f ssh/mylab
```

Test deployment.app on the k8s cluster
```
kubectl get pod -n beehive-mylab -o wide
kubectl describe pod ... -n beehive-mylab 
kubectl logs ... -n beehive-mylab -f
```

Console api test
```
beehive3 ssh node-groups get 
beehive3 ssh nodes get
beehive3 ssh node-users get 
beehive3 ssh keys get
```



### Resource component creation
Schema and user creation on db
```
beehive3 platform mysql dbs add resource 
beehive3 platform mysql dbusers add resource resource
beehive3 platform mysql dbusers grant resource resource 
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create resource pkgs/nivola/deploy/customization/resource.yml
```

Starting deployment.app on the k8s cluster
```
kubectl create -f resource/mylab
```

Test deployment.app on the k8s cluster
```
kubectl get pod -n beehive-mylab -o wide
kubectl describe pod ... -n beehive-mylab 
kubectl logs ... -n beehive-mylab -f
```

Perform some customize
```
beehive3 auth tokens delete all -y
beehive3 platform cmp customize run test/resource/tag
```

Console api test
```
beehive3 res entities get
beehive3 platform scheduler tasks test resource 
```



### Service component creation
Schema and user creation on db
```
beehive3 platform mysql dbs add service
beehive3 platform mysql dbusers add service service 
beehive3 platform mysql dbusers grant service service 
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create service pkgs/nivola/deploy/customization/service.yml
```

Starting deployment.app on the k8s cluster
```
kubectl create -f service/mylab
```

Test deployment.app on the k8s cluster
```
kubectl get pod -n beehive-labx -o wide
kubectl describe pod ... -n beehive-mylab
kubectl logs ... -n beehive-mylab  -f
```

Console api test
```
beehive3 auth tokens delete all -y
beehive3 bu orgs get
beehive3 bu divs get
beehive3 bu accounts get
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
