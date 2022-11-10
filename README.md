# Nivola
Nivola is a platform that simplifies the use of the cloud service by the public administration.
The Nivola platform is created by CSI Piemonte and provides computing, storage and network resources.

To have a more detailed view of the platform go to:
- [institutional link](https://www.nivolapiemonte.it/)
- [user guide](https://nivola-userguide.readthedocs.io/it/latest/)

## Product and Components
This project contains the Product **nivola**.
The product contains some components, you can find a description of each component within its README file:

* beecell 
[GitHub](https://github.com/Nivola/beecell)
* beedrones 
[GitHub](https://github.com/Nivola/beedrones)
* beehive 
[GitHub](https://github.com/Nivola/beehive)
* beehive-oauth2 
[GitHub](https://github.com/Nivola/beehive-oauth2)
* beehive-resource 
[GitHub](https://github.com/Nivola/beehive-resource)
* beehive-service
[GitHub](https://github.com/Nivola/beehive-service)
* beehive-service-netaas
[GitHub](https://github.com/Nivola/beehive-service-netaas )
* beehive-ssh 
[GitHub](https://github.com/Nivola/beehive-ssh)
* beehive3-cli 
[GitHub](https://github.com/Nivola/beehive3-cli)


## Installing Cloud Management Platform (CMP)
Overview of the parts you are going to create:
- Nivola shell console (CLI)
- Cloud Management Platform (CMP) the integration and automation platform that exposes all business services through API (Application programming Interface) that can be called up by the user, which includes accounting, profiling, security services
- Nginx, a proxy server that allows the CLI to call the various components of the CMP in https
- Mysql database where some schema will be created

### Prerequisites
- You must have already downloaded this project __nivola__ and to start the projects beecell, beedrones, beehive in a "workspace" folder
- Install Docker for building images.
- You must have the Nivola CLI (shell console) already installed. 
See __beehive3-cli__ project [GitHub](https://github.com/Nivola/beehive3-cli)
- You must have "minikube" installed (a tool that lets you run a single-node Kubernetes cluster on your personal computer)
- CMP deployment using the Kubernetes command-line tool, kubectl.
- Install a MySql/MariaDB database (MySql version > 5.7, MariaDB version > 10.5).
We suggest to use a Mysql Docker. See instructions in __beehive3-cli__ project.
- Install Elasticsearch server where write logs.


### Minikube start
Start your minikube with the docker driver, replacing the following placeholder <WORKSPACE> with folder where you downloaded projects.
We suggest that minikube process starts in a docker network "nivolanet" for being reachable from CLI and Nginx.
```
$ minikube start --driver=docker --cpus=4 --mount=true --mount-string="<WORKSPACE>:/pkgs" --network nivolanet
```

To obtail minikube IP launch (you will need it to configure Nginx)
```
$ minikube ip
```

### Nginx installation and update CLI configuration
You need a Nginx correctly configured to call in https CMP components.
In deploy directory __beehive3-cli/deploy/nginx__ you find dockerfile.
In configuration file __beehive3-cli/deploy/nginx/nginx-files/beehive-ssl-api.mylab.conf__ update all occurrences of "<MINIKUBE_IP>"

Build Nginx image "nivola/https-nginx"
Launch the following command from folder __beehive3-cli/deploy/nginx__
```
docker image build --tag nivola/https-nginx -f Dockerfile.https.nginx .
```

We suggest that Nginx process starts in a docker network "nivolanet"
```
docker run --network nivolanet --name tmp-nginx-container -d nivola/https-nginx
```

Find docker Nginx IP address, for update CLI configuration endpoints
```
docker ps | grep tmp-nginx-container
docker inspect tmp-nginx-container | grep "IPAddress"
```

Test nginx configuration using CLI or open "https://<NGINX_IP>:443" in your browser
```
curl -k https://<NGINX_IP>:443
    ...check if you see "<title>Welcome to nginx!</title>"
```

See Nginx error log in case of problem calling Nginx
```
docker exec -it tmp-nginx-container tail -f /var/log/nginx/beehive.api.test.error.log
```

See Nginx access log to see complete information about test call
```
docker exec -it tmp-nginx-container tail -f /var/log/nginx/beehive.api.test.access.log
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
Move to folder __nivola/deploy/k8s__.
In core/mylab/beehive-volume.yml look at "hostPath" parameter.
If you start minikube with --driver=none replace <WORKSPACE> with your project folder
otherwise mount your workspace passing to minikube '--mount=true --mount-string="<WORKSPACE>:/pkgs" '

Launch:
```
$ kubectl create -k core/mylab
```


### Creation of engines used by cmp
Creation of engines such as redis, rabbitmq, proxysql.
Always from __nivola/deploy/k8s__ folder, launch:
```
$ kubectl create -k engine/mylab
```


### Build CMP Docker image
To create the complete CMP Docker image you have also to download the projects:
* beehive-oauth2 
* beehive-resource 
* beehive-service 
* beehive-service-netaas 
* beehive-ssh  

In deploy directory __nivola/deploy/k8s__ you find dockerfiles.
Build docker image "nivola/nivola-uwsgi" from your workspace folder:
```
docker image build --tag nivola/nivola-uwsgi -f nivola/deploy/k8s/Dockerfile.uwsgi-py3 .
```

Build docker image "nivola/cmp" that start from image "nivola/nivola-uwsgi" from your workspace folder.
You can do this or copying projects into image (in this case you have to go to folder where you downloaded projects)

```
docker image build --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
```

or downloading projects into image and passing git user/password.
Look at dockerfile and comment/uncomment relative sections.

```
docker image build --build-arg GITUSER=<USER> --build-arg GITPWD=<PASSWORD> --tag nivola/cmp -f nivola/deploy/k8s/Dockerfile.cmp .
```

NOTE: image "nivola/cmp" is referenced in k8s files used below.

If you start minikube with --driver=docker
you can upload image to a docker registry and update references in kubernates files auth/mylab.yml...  
or save your image in a file and then load it in minikube docker:
```
docker save nivola/cmp:latest > $HOME/nivola_cmp_latest.tar
eval $(minikube docker-env)
docker load < $HOME/nivola_cmp_latest.tar
docker images
```
In both cases, check also "imagePullPolicy" parameter in mylab.yml files of the following components.


### Auth component creation
Auth is the fundamental component that implements all the authentication and authorization api and makes available the endpoint catalogs of all the api. It is a central component that is used from other components and external users.

Schema and user creation on db
To continue, the cli must be installed.
```
beehive3 platform mysql dbs add auth
beehive3 platform mysql dbusers add auth auth
beehive3 platform mysql dbusers grant auth -db auth
```

Data population on the database and registration of permissions on some entities
Perform some customize
- copy nivola/deploy/customization/auth.yml /tmp
```
# to create Auth tables
beehive3 platform cmp subsystems create auth pkgs/nivola/deploy/customization/auth.yml
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
This component exposes ability to capture and manipulate events

Schema and user creation on db
```
beehive3 platform mysql dbs add event 
beehive3 platform mysql dbusers add event event 
beehive3 platform mysql dbusers grant event -db event 
```

Data population on the database and registration of permissions on some entities
```
beehive3 platform cmp subsystems create event pkgs/nivola/deploy/customization/event.yml
```

Starting deployment.app on the k8s cluster
Update in event/mylab/mylab.yml the following properties with reference to your hosts:
- ELASTIC_NODES
- MYSQL_URI
- OAUTH2_ENDPOINT (link to Nginx)
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
This component exposes host connection check and logging capabilities

Schema and user creation on db
```
beehive3 platform mysql dbs add ssh
beehive3 platform mysql dbusers add ssh ssh
beehive3 platform mysql dbusers grant ssh -db ssh
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
This component expose all the technological and low level orchestration capabilities. Interact with all the virtualization, cloud orchestration, backup, monitoring, logging infrastructure platforms. Expose synchronous and asynchronous capabilities using python celery framework

Schema and user creation on db
```
beehive3 platform mysql dbs add resource 
beehive3 platform mysql dbusers add resource resource
beehive3 platform mysql dbusers grant resource -db resource 
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
This component exposes all the business and high user level orchestration capabilities.  
Interact with the resource subsystem.  
Expose synchronous and asynchronous capabilities using business process

Schema and user creation on db
```
beehive3 platform mysql dbs add service
beehive3 platform mysql dbusers add service service 
beehive3 platform mysql dbusers grant service -db service 
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

Current version is: 1.9.0

## Authors
See the list of contributors who participated in this project in the file AUTHORS.md contained in each specific project.

## Copyright
CSI Piemonte - 2018-2022

Regione Piemonte - 2020-2022

## License
See the LICENSE.txt file contained in each specific project for details.

## Community site (Optional)
At https://www.nivolapiemonte.it/ could find all the informations about the project.
