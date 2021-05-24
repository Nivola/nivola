# Nivola
Nivola is a platform that simplifies the use of the cloud service by the public administration.
The Nivola platform is created by CSI Piemonte and provides computing, storage and network resources.

## Product and Components
This project contains the Product **nivola**.
The product contains some components:

* beecell 
[GitHub](https://github.com/Nivola/beecell) - 
[GitLab](https://gitlab.csi.it/nivola/cmp3/beecell/tree/devel)
* beedrones 
[GitHub](https://github.com/Nivola/beedrones) - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beedrones/tree/devel)
* beehive 
[GitHub](https://github.com/Nivola/beehive) - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beehive/tree/devel)
* beehive-oauth2 
[GitHub]() - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beehive-oauth2/tree/devel)
* beehive-resource 
[GitHub]() - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beehive-resource/tree/devel)
* beehive-service 
[GitHub]() - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beehive-service/tree/devel)
* beehive-service-netaas 
[GitHub]() - 
[GitLab](https://gitlab.csi.it/nivola/cmp3/beehive-service-netaas/tree/devel)
* beehive-ssh 
[GitHub]() - 
[GitLab](https://gitlab.csi.it/nivola/cmp2/beehive-ssh/tree/devel)
* beehive3-cli 
[GitHub](https://github.com/Nivola/beehive3-cli) - 
[GitLab](https://gitlab.csi.it/nivola/cmp3/beehive3-cli/tree/devel)


## Installing Cloud Management Platform (CMP)

### Prerequisites
- You must have already downloaded the projects beecell, beedrones, beehive.
- You must have the Nivola CLI (shell console) already installed. 
See __beehive3-cli__ project [GitHub](https://github.com/Nivola/beehive3-cli) - [GitLab](https://gitlab.csi.it/nivola/cmp3/beehive3-cli/tree/devel)
- You must have "minikube" installed
- Install a MySql/MariaDB database (MySql version > 5.7, MariaDB version > 10.5)
- Install Elasticsearch server where write logs.
- CMP deployment using the Kubernetes command-line tool, kubectl.
- Install Docker for building images.
- Move to folder nivola/deploy/k8s

### Minikube start
Start your minikube with the docker driver, replacing replacing placeholder <WORKSPACE> with folder where you downloaded projects.
We suggest that minikube process starts in a docker network "nivolanet" for being reachable from CLI and Nginx.
```
$ minikube start --driver=docker --cpus=4 --mount=true --mount-string="<WORKSPACE>:/pkgs" --network nivolanet
```

To obtail minikube IP launch (you will need it to configure nginx)
```
$ minikube ip
```

### Nginx installation and update CLI configuration
You need a Nginx correctly configured to call in https CMP components.
In deploy directory __beehive3-cli/deploy/nginx__ you find dockerfile.
In configuration file __beehive3-cli/deploy/nginx/nginx-files/beehive-ssl-api.lab1.conf__ update "minikube ip"

Build Nginx image "nivola/https-nginx"
```
docker image build --tag nivola/https-nginx -f Dockerfile.https.nginx .
```

We suggest that Nginx process starts in a docker network "nivolanet"
```
docker run --network nivolanet --name tmp-nginx-container -d nivola/https-nginx
```

See Nginx log
```
docker exec -it tmp-nginx-container tail -f /var/log/nginx/beehive.api.test.access.log
docker exec -it tmp-nginx-container tail -f /var/log/nginx/beehive.api.test.error.log
```

Find docker Nginx IP address, for update CLI configuration endpoints
```
docker ps | grep tmp-nginx-container
docker inspect tmp-nginx-container | grep "IPAddress"
```

Test nginx configuration using CLI
```
curl -k https://<NGINX_IP>:443
    ...<title>Welcome to nginx!</title>
```

Update CLI endpoints in file /config/env/mylab.yml and restart CLI
```
cmp:
    endpoints:
        # https connection through nginx
        auth: https://<NGINX_IP>:443
        event: https://<NGINX_IP>:443
        ssh: https://<NGINX_IP>:443
        resource: https://<NGINX_IP>:443
        service: https://<NGINX_IP>:443
```


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
To create the complete CMP Docker image 
you have also to download the projects:
* beehive-oauth2 
* beehive-resource 
* beehive-service 
* beehive-service-netaas 
* beehive-ssh  

In deploy directory __nivola/deploy/k8s__ you find dockerfiles.
Build docker image "nivola/nivola-uwsgi":
```
docker image build --tag nivola/nivola-uwsgi -f nivola/deploy/k8s/Dockerfile.uwsgi-py3 .
```

Build docker image "nivola/cmp" that start from image "nivola/nivola-uwsgi"
You can do this or copying projects into image (in this case you have to go to folder where you downloaded projects)

```
docker image build --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
```

or downloading projects into image and passing git user/password.
Look at dockerfile and comment/uncomment relative sections.

```
docker image build --build-arg GITUSER=<USER> --build-arg GITPWD=<PASSWORD> --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
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
In both cases, check also imagePullPolicy in mylab.yml files.


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

You can verify deployment of Auth components calling in your browser:
```
http://<MINIKUBE_IP>:30000/v1.0/server/ping
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
# oauth2 client
beehive3 platform cmp customize run oauth2

# example tests
beehive3 auth roles add test-role -desc desc-test-role
beehive3 auth users add -email name1@local -password xxxxxxxxx name1@local
```

Assign the ApiSuperAdmin role to the oauth2 client that you use for server to server communication.
```
beehive3 auth users add-role client-beehive@local ApiSuperAdmin
```

Update the customization files for the various modules by setting the client uuid and the secret.
Look in files /deploy/k8s/<COMPONENT>/mylab/mylab.yml at property API_OAUTH2_CLIENT, 
that you have to set with "UUID : SECRET".
Client data can be obtained with the command:
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

[comment]: <> (### Come registrare gli orchestratori - TODO)
[comment]: <> (### Inizializzazione resource - TODO)
[comment]: <> (### Authoring servizi - TODO)


## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use Semantic Versioning for versioning. (https://semver.org)

Current version is: 1.8.2

## Authors
See the list of contributors who participated in this project in the file AUTHORS.md contained in each specific project.

## Copyright
CSI Piemonte - 2018-2021

Regione Piemonte - 2019-2021

## License
See the LICENSE.txt file contained in each specific project for details.

## Community site (Optional)
At https://www.nivolapiemonte.it/ could find all the informations about the project.
