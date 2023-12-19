# Changelog

## Version  1.15.1
* Fixed
  * Correzione bug vari
* Added
  * Audit Log CMP
  * Tracciatura degli accessi alle vm CMP dalle CLI in esecuzione sulle console di amministrazione
  * Revisione load balancer


## Version  1.15.0
* Fixed
* Added
  * Nuovi servizi di definizione soglie ed alert (as-a-service)
  * Gestione eventi - log
    * Tracciamento user agent nelle chiamate alle API per distinguere chiamate dalla CLI (con versione utilizzata), batch schedulati, Service Portal
    * Configurazione su Kibana: creato space Csi.nivola.event per visualizzare dati chiamate alle API CMP
  * Compute Service
    * Service Importazione di volumi presenti a livello resource ma assenti a livello business, per maggiori dettagli: $ beehive bu cpaas volumes load -h
  * Monitoring service:
    * Rilascio servizio per la gestione degli alert [BETA]
    * Monitoring service: Dashboard “Template” di Grafana importate in resource per evitare modifiche al layout non intenzionali, per successiva copia
  * Network Service
    * Creazione, import e cancellazione load balancer in ambiente private
    * Abilitazione quote load balancer
  * Resource
    * Importazione dei project volume openstack mancanti e collegamento con project server: $ beehive res-openstack server-patch -h
    * Importazione di compute volume e creazione dei link tra compute volume e project volume e collegamento tra compute instance e compute volume: $ beehive res-provider instance-patch
    * Extend di un ComputeVolume agganciato a una ComputeInstance: $ beehive res-openstack server-patch -h
    * In vsphere il comando funziona senza dover spegnere la vm, su openstack è necessario preventivamente spegnere la vm; nel caso sia accesa e si lancia il comando la cli lo segnala.


## Version  1.14.1
* Fixed
  *	High	Bug	NPC-986	Durante la creazione degli account i ruoli creati mancano dei permessi su ApiMethod
  * High	Improvement	NPC-988	Max 2 core_per_socket in vm vsphere
  * Medium	Bug	NPC-985	Errore in calcellazione vm vmware quando le vm hanno volumi con ext _id posizionale e non con object id univoco vmwareo
  * Medium	Bug	NPC-987	Nei log della cmp compaiono informazioni riservate
* Added

## Version  1.14.0
* Fixed
* Added
  * Network Service - Load Balancer
  * Network Service - SSH gateway
  * modificare impostazioni di sicurezza in modo che sia possibile accedere alle console
  * apertura delle console delle vm da internet
  * aggiunta di 2 nodi al mariadb galera cluster sul podto1
  * Compute Service - Compute instance - gestione backup server vsphere
  * API Service	Unassigned	RESOLVED
  * Creazione sessione con un subset dei permessi disponibili all'utente (un ruolo)
  * Automazione installazione zabbix agent su vm Windows
    * Gestione dei permessi per singolo metodo
  * Gestione Sessione
    * Possibilità di ridurre  i permessi della sessione attiva ad un sottoinsieme dei permessi dell’utente.
    * Possibilità di ridurre i permessi della sessione attiva  ai soli permessi di un ruolo
  * Funzioni di business
    * Gestione sessione
      * Possibilità di ridurre i permessi della sessione attiva ai soli permessi necessari ad amministrare un Account
      * Possibilità di ridurre i permessi della sessione attiva ai soli permessi necessari a vedere un Account
      * Possibilità di ridurre i permessi della sessione attiva ai soli permessi necessari ad operare su di un Account
  * Monitoring Service
    * Automazione installazione zabbix agent su vm Windows
  * Network Service
    * Import load balancer
    * Creazione, cancellazione, “attivazione” ssh gateway configuration
  * Compute Service
    * Ottimizzazione in termini di tempo nell’ottenere la lista delle vm per account
  * Funzioni di orchestrazione
  * Backup
    * Integrazione con Veeam
  * VsphereServerHardware Supporto di 64 volumi per bus scsi se nella vm è preinstallato virtual hardware di una versione superiore alla 14. Nel caso di virtual hardware inferiore alla 14 quando si aggancia il sedicesimo volume dice che non può montare il volume e suggerisce di aggiornare manualmente virtual hardware
  * VsphereServerHardware Spegnimento a freddo; ora il sistema operativo chiudere i processi e smonta i dischi prima della terminazione delle vm
  * VsphereServerHardware Possibilità di estendere volumi vsphere da cli attraverso comando res-provider


## Version 1.13.1R

* Fixed
  * 	Bug	NPC-964	la modifica di una imagine non supporta il parametro customization_spec_name	DORIA Gianni 72386	CLOSED
  * 	Bug	NPC-973	Errore in creazione Oracle 12EE	SACCHETTO Davide 2162	CLOSED
  * 	Bug	NPC-974	Consumi da Sanare	VALLERO Filippo 73338	CLOSED
  * 	Bug	NPC-976	modifica delle configurazione di risorse e servizi forza i valori a stringa	Unassigned	CLOSED
* Added
  *	Improvement	NPC-972	Creazione di volumi su vm Vsphere oltre il 16esimo fino al 64esimo.	PILOLLI Pietro 74008	CLOSED

## Version 1.13.0
* Fixed
  *	Revision of Openstack snapshot without usinig Volume Group
  * Some errors while creating dbaas postgres 12.4



## Version 1.12.0
* Fixed
  * fixed problem new elastic library
  * move from library dicttoxml to dict2xml
  * fixed problem deleting vm
  * fixed problem on dbinstance: check change type

## Version 1.11.0 (oct 21, 2022)

* Added ...
    * now compute instance support static ip passed from api
    * add compute instance host_group openstack: bck and nobck
    * add field nvl_HostGroup in DescribeInstancesV20 api
    * add LoggingServiceAPI, MonitoringSpaceServiceAPI, MonitoringInstanceServiceAPI,
    * add ApiMonitoringService, ApiMonitoringSpace, ApiMonitoringInstance
* Fixed
    * fixed problem with default name of logging space
    * fixed problem with icmp rule in security group
    * fixed problem with instance host_group when show flavor
* Integrated ...
* Various bugfixes
* Internal Packages updated
  * beecell
  * beedrones
  * beehive
  * beehive-oauth2
  * beehive-resource
  * beehive-service
  * beehive-service-netaas
  * beehive-ssh
  * beehive-ansible
  * beehive3-cli

## Version 1.10.0 (feb 11, 2022)

* Added ...
    * modified now return 404 if core service is not present when getting or modifying account's attributes
    * add method v2.0/nws/accounts/.../definitions to get which definition are available for the account
    * add AccountServiceDefinition. Now the Account knows which definition can instantiate
    * add DatabaseInstanceV2 create method params Nvl_Options.Postgresql_GeoExtension to manage database options
    * add DatabaseInstanceV2 import api from stack sql v2
    * add InstanceV2 api with porting of the old v1.0 apis
    * add InstanceV2 api get console
    * add VolumeV2 api to manage volume type api update
    * add ComputeInstanceBackupAPI api to manage backup job, restore points and restore [beta]
    * add ComputeVolume pre_import method
    * add ComputeShare label management to get custom svm
    * extend ComputeShare to support ontap share
    * add LoggingServiceAPI, LoggingSpaceServiceAPI, LoggingInstanceServiceAPI,
    * add ApiLoggingService, ApiLoggingSpace, ApiLoggingInstance
    * add database instance mailx configuration and haproxy registration based on definition config
    * add model method get_service_definition_by_config
* Fixed
    * fixed bug in SecurityGroup set_service_info. It Does not manage icmp sub protocol field
    * fixed api /v2.0/nws/computeservices/instance/describeinstancetypes to support new account service catalog.
      Now required filter by account
    * fixed api /v2.0/nws/databaseservices/instance/describedbinstancetypes to support new account service catalog
      Now required filter by account
    * fixed api /v2.0/nws/databaseservices/instance/enginetypes to support new account service catalog
      Now required filter by account
    * fixed type check in db instance and compute instance
    * volume volumetype is read directly from resource
    * update DBInstanceClass param in api GET. Value is get from resource
    * update instanceType param in api GET. Value is get from resource
    * update Share size param in api GET. Value is get from resource
    * correct bug that blocks old sql stack delete
* Integrated ...
    * add ComputeVolume check when delete api is invoked. If volume is in-use error is returned
    * update capabilities and account capabilities to support account definitions
* Various bugfixes

## Version 1.9.0 (Jun 11, 2021)

* Added ...
    * add service instance set config api
	* add ComputeInstance import
	* add ComputeInstance create from existing volume
	* add ComputeInstance api to add/delete/change password to internal user
	* add ComputeCustomization
    * add ComputeInstance api rebootinstances
	* add ComputeInstance api monitorinstances
	* add ComputeInstance api forwardloginstances
	* add DatabaseInstance db api describedbinstancedb, createdbinstancedb, deletedbinstancedb
	* add DatabaseInstance user api describedbinstanceuser, createdbinstanceuser, deletedbinstanceuser,
	  changedbinstanceuserpassword, grantdbinstanceuserprivileges, revokedbinstanceuserprivileges
	* add filter by account in ComputeTag api
* Fixed
* Integrated ...
	* add propagation of task error from resource to service
	* add task field in some api view schemas
	* add check of subnet type in db instance create. If subnet is public an error was returned
	* add some check in compute volume attach and detach
	* add account apis v2.0 with new delete api. Now when delete you can specify if delete all child services
* Various bugfixes
* Internal Packages
  * beecell 1.8.0
  * beedrones 1.6.0
  * beehive 1.10.0
  * beehive-oauth2 1.2.2
  * beehive-resource 1.11.0
  * beehive-service 1.9.0
  * beehive-service-netaas 1.1.0
  * beehive-ssh 1.5.0
  * beehive-ansible 1.3.0
  * beehive3-cli 1.8.0

## Version 1.8.2 (Feb 05, 2021)

* Added ...
  * add new api ping (with sql check), capabilities and version to /v1.0/nas, /v1.0/nes, /v1.0/nws, /v1.0/nrs, /v1.0/gas
  * add service instance check api
  * add service instance name validation
  * add owner propagation from keypair to ssh key
* Fixed
  * removed error propagation that block dbaas instance query
  * fixed implementation of share delete
* Integrated ...
* Various bugfixes
* Internal Packages
  * beecell 1.7.1
  * beedrones 1.5.1
  * beehive 1.9.0
  * beehive-oauth2 1.2.2
  * beehive-resource 1.10.0
  * beehive-service 1.8.0
  * beehive-service-netaas 1.0.0
  * beehive-ssh 1.4.0
  * beehive-ansible 1.3.0
  * beehive3-cli 1.6.0

## Version 1.8.1 (Dec 31, 2020)

* Added ...
* Fixed
* Integrated ...
* Various bugfixes
* Internal Packages
  * beecell 1.7.0
  * beedrones 1.5.0
  * beehive 1.8.0
  * beehive-oauth2 1.2.2
  * beehive-resource 1.9.0
  * beehive-service 1.7.0
  * beehive-service-netaas 1.0.0
  * beehive-ssh 1.3.0
  * beehive-ansible 1.2.0
  * beehive3-cli 1.4.0

## Version 1.8 (Oct 23, 2020)

* Added ...
    * add sql_stack_v2 with sql stack based on stack_v2
    * added dbaas api v2.0. Class ApiDatabaseServiceInstance was replaced with ApiDatabaseServiceInstanceV2
        * engine supported: mysql, postgresql, oracle, sqlserver
    * added ComputeCustomization and AppliedComputeCustomization to run ansible playbook on ComputeInstance
    * added ApiComputeInstance action to add/remove security group
    * added ApiComputeInstance action to add/remove/revert snapshots
    * added ApiServiceDefinition field config in update api
    * add resource entity api to clean cache
* Fixed
	* some minor fixed in schema fields definitions in order to get better swagger descriptions
	* api oid field declaration for post services with {oid} in path
* Integrated ...
    * added ApiStorageEFS api param PerformanceMode used to manage share based on netapp and new share base on local
      openstack server
* Various bugfixes
    * apply patch to method ApiComputeSecurityGroup.get_rule_info_params
	* fixed error generating swagger specification
* Internal Packages
  * beecell 1.6.1
  * beedrones 1.4.2
  * beehive 1.7.2
  * beehive-oauth2 1.2.2
  * beehive-resource 1.9.0
  * beehive-service 1.7.0
  * beehive-service-netaas 1.0.0
  * beehive-ssh 1.3.0
  * beehive-ansible 1.2.0
  * beehive3-cli 1.4.0

## Version 1.7 (Jun 21, 2020)

* Added
  * Architectural change
    * Porting of code to python 3.7.x
    * beehive shell console was rewritten in python 3.7.x using cement 3 and included in package beehive3_cli
    * nivola platform is now deployed using k8s
    * nivola platform sql database was moved from mysql innodb cluster 5.7 to mariadb galerea cluster 10.4
  * New functions
    * async task was been entirely rewritten using a single celery task
    * vpc now support private and shared type. Shared is the default old type. Private is the new type used to generate
      private networks that are completely isolated from different accounts
    * Private Network Gateway (base creation of beehive resource)
    * Virtual machine scheduled start e stop
    * Volume management from business service
  * New package
    * package beehive-mgmt was replaced by beehive-ansible
* Fixed
  * Revisione of openapi schema after python requirements update
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.6.1
  * beedrones 1.4.0
  * beehive 1.7.0
  * beehive-oauth2 1.2.2
  * beehive-resource 1.8.0
  * beehive-service 1.6.0
  * beehive-ssh 1.3.0
  * beehive-ansible 1.0.0
  * beehive3-cli 1.0.0

## Version 1.6 (Dec 24, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.6.0
  * beedrones 1.3.0
  * beehive 1.6.0
  * beehive-oauth2 1.2.0
  * beehive-resource 1.6.0
  * beehive-service 1.5.0
  * beehive-ssh 1.2.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.5.0


## Version 1.5 (Sep 04, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.5.0
  * beedrones 1.3.0
  * beehive 1.5.0
  * beehive-oauth2 1.2.0
  * beehive-resource 1.6.0
  * beehive-service 1.5.0
  * beehive-ssh 1.2.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.5.0

## Version 1.4 (May 24, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.4.0
  * beedrones 1.2.0
  * beehive 1.4.0
  * beehive-oauth2 1.1.0
  * beehive-resource 1.5.0
  * beehive-service 1.4.0
  * beehive-ssh 1.1.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.4.0

## Version 1.3 (February 27, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.3.0
  * beedrones 1.1.0
  * beehive 1.3.0
  * beehive-oauth2 1.0.0
  * beehive-resource 1.4.0
  * beehive-service 1.3.0
  * beehive-ssh 1.0.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.3.0

## Version 1.2 (February 01, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.2.0
  * beedrones 1.1.0
  * beehive 1.2.0
  * beehive-oauth2 1.0.0
  * beehive-resource 1.3.0
  * beehive-service 1.2.0
  * beehive-ssh 1.0.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.2.0

## Version 1.1 (January 13, 2019)

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.1.0
  * beedrones 1.1.0
  * beehive 1.1.0
  * beehive-oauth2 1.0.0
  * beehive-resource 1.2.0
  * beehive-service 1.1.0
  * beehive-ssh 1.0.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.1.0

## Version 1.0 (July 31 2018)

First release.

* Added
* Fixed
* Integrated
* Various bugfixes
* Internal Packages
  * beecell 1.0.0
  * beedrones 1.0.0
  * beehive 1.0.0
  * beehive-oauth2 1.0.0
  * beehive-resource 1.0.0
  * beehive-service 1.0.0
  * beehive-ssh 1.0.0
  * beehive-mgmt 1.0.0
  * beehive-cli 1.0.0
