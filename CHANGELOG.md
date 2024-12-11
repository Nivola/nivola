# Changelog

## versione 1.16.5
* Risolto
  - Rilascio Ip su vsphere: l'ip non era rilasciato se l'est_id il server Vsphere era None or inesistente
  - Verifica su tipi booleano
  - flavor in pre-import per vms con più di una cpu
* Aggiunto
  - log nel metodo delete rule
  - refactoring delle regole dfw di vsphere
  - Verifiche su tipi booleano
  - grafana: supporto a versione 11 gestiti errori e warning
  - rivista alcuni alert relativi alla configurazione monitoraggio
* Migliorato
  - messaggio di errore quando l'immagine non esiste nella zona (pod) cercata


## versione 1.16.4
* Risolto
  - creazione dbaas scelta del'interprete python usando i template e la versione del  DB
  -  uuid mancante dopo aggiornamento account

## versione 1.16.3
* Aggiunto
  - Enabled server actions (e.g. change flavor) on SQLServer engine
  - versione completa e metadata nel metodo db engines list
* Migliorato:
    - DNS_TTL
* Risolto
  - regressione nella aggiornamento di db-instances update

## versione 1.16.2
* Risolto
  - fix install_zabbix_proxy

## versione 1.16.1
* Risolto
  - descovering and configure of zabbix proxy
  - zabbix uri without port (if port is not present in conf)
  - manage image default min_ram_size while creating servers
  - ripristinata firma precedente per compatibilità backward
  - errori legati alla lunghezza del nome del server
  - verifica dei permessi relativi alle definizioni usate nella creazione di un dbaas
* Aggiunto
  - aggiunti attributi espliciti negli account per modello di gestione, zone(pods) di deploy, e modello di rete
  - verifica della coerenza delle capability rispetto agli attributi del'account
  - esposto metodo di verifica del'Account
  - gestione vista per esporre consumi a livello di servizio



## Version 1.16.0

* Aggiunto ...
  - Chiusura degli account: aggiunto parametro  "close_account"  pagli account chiusi prima ed invece della cancellazione
  - Account operator e Ruolo Account operator mancanti
  - Clonazione su vsphere
  - get account deleted, Account is_active
  - get node password
  - rivisti metodi per il cloning
  - Commentato codice obsolete
  - sync user revert per Grafana
  - update swagger users
  - sync_users con nuovo campo ldap di user
  - dbaas: check min_ram_size creating db
  - vsphere clone with instanceId of source VM
  - Fix check on last snapshot @see https://jira.csi.it/browse/NSP-2895
  - service metric: type hint, log
  - private cloud network using vsphere_only
  - blacked
  - headers updated
  - Debian 11 support
  - vsphere customization
  - vsphere clone
  - mariadb: fix task path
  - more robust waiting customization; this has been ported on platform, use vim and vsphere api from resource
    it goes against our layered architecture
* Risolto
  - clone swagger definition fix
  - fix log sync user if ldap is none
  - fix delete account: expiry date, active
  - fix wrong permission objid that resulted in error while creating account
  - user with taxcode
  - username and password
  - fix ubuntu: username get from ssh (ubuntu or root)
  - LB: add check for multiple uplink vnics
  - Correct lb import bug
  - Fix ssh authorized_keys in right location for non root users
  - Fix lb issue occurring when site-network is passed by name
  - bastion: fix delete if some data aren't present
  - links: find by objid
  - better logging for edge cases detection when wrong parent id
  - fix grafana sync user fornitori, fix cache resource not active
  - clone: minor
  - clone: add some comments
  - minor
  - clone patchset to use real admin user
  - fix username in ssh node
  - wip clone
  - vpshere clone, this step is not needed
  - fix new server instance
  - inst new
  - redis eliminate righe commentate
  - clone add ext_id to volume resource
  - Fix prvious commit
  - fix race condition on server creation; after a create MUST wait guest tool; this run after the startup of vm
  - fix wait for customization implementation; the old one continue to loop if the customization failed
  - server_event_exist
  - ssh and password
  - clone funzionante stessa zona
  - hostname for server
  - clone on same zone
  - openstack: check connection valid
  - Errori vari
  - alcuni branch rinominati
  - fix bug nel  token openstack
  - verifiche vsphere template server
  - Aggiornato changelog
  - Aggiornati autori using git shortlog
  - blacked files resi compiant pep8
  - aggiornameto headers
  - NPC-1011 - fix escaping range cidr in like condition e.g. %32 ->  \\\\/32



## Version v.1.15.3

* Aggiunto ...
  - Funzinalità per aggiornaere progetti awx ad una customazation esistente
  - aggiunte nove metriche: vm_power_on, db_<engine>_power_on
  - supporto per mariadb


* Risolto ...
  - backup dei nuovi pods - gestione dell'errore no orchestrators found
  - customization: aggiornati o rimosse codice temporaneo inserito per gestione di nuovi pod
  - type hint: ResourceCache
  - verificate aggiornamenti ComputeFlavor
  - Computeflavor.pre_update
  - restore point: default response
  - Veeam reuse connection token, aggiunta debug log
  - private cloud: vsphere only
  - mariadb: utilizzate variabili e nomi job parlanti
  - image: check pre_delete, param "min_ram_size"
  - update image: change msg error
  - fix insert/update image
  - vsphere template server check
  - See merge request nivola/cmp2/beehive-resource!6
  - vsphere template server check
  - fix CreateCustomizationAwxProjectRequestSchema
  - MariaDB Aggiunto new classes
  - Ssh gateway remove log
  - Vpc: commentato orchestrator_select_types
  - AvailabilityZone: orchestrator_select_types while creating in creazione e per get hypervisor, commentato altrove
  - fix msg applied_customization: Ansible connection with winrm is not supported through bastion
  - bugfix NPC-1009 NSP-1337
  - NPC-1009 NSP-1337 fix totale sbagliato dopo applicazione filtro objdef
  - type hint: vpc get proxy
  - Afggiornato manifest


## Version  1.15.1
* Risolto
  * Correzione bug vari
* Aggiunto
  * Audit Log CMP
  * Tracciatura degli accessi alle vm CMP dalle CLI in esecuzione sulle console di amministrazione
  * Revisione load balancer


## Version  1.15.0
* Risolto
* Aggiunto
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
* Risolto
  *	High	Bug	NPC-986	Durante la creazione degli account i ruoli creati mancano dei permessi su ApiMethod
  * High	Improvement	NPC-988	Max 2 core_per_socket in vm vsphere
  * Medium	Bug	NPC-985	Errore in calcellazione vm vmware quando le vm hanno volumi con ext _id posizionale e non con object id univoco vmwareo
  * Medium	Bug	NPC-987	Nei log della cmp compaiono informazioni riservate
* Aggiunto

## Version  1.14.0
* Risolto
* Aggiunto
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

* Risolto
  * 	Bug	NPC-964	la modifica di una imagine non supporta il parametro customization_spec_name	DORIA Gianni 72386	CLOSED
  * 	Bug	NPC-973	Errore in creazione Oracle 12EE	SACCHETTO Davide 2162	CLOSED
  * 	Bug	NPC-974	Consumi da Sanare	VALLERO Filippo 73338	CLOSED
  * 	Bug	NPC-976	modifica delle configurazione di risorse e servizi forza i valori a stringa	Unassigned	CLOSED
* Aggiunto
  *	Improvement	NPC-972	Creazione di volumi su vm Vsphere oltre il 16esimo fino al 64esimo.	PILOLLI Pietro 74008	CLOSED

## Version 1.13.0
* Risolto
  *	Revision of Openstack snapshot without usinig Volume Group
  * Some errors while creating dbaas postgres 12.4



## Version 1.12.0
* Risolto
  * fixed problem new elastic library
  * move from library dicttoxml to dict2xml
  * fixed problem deleting vm
  * fixed problem on dbinstance: check change type

## Version 1.11.0 (oct 21, 2022)

* Aggiunto ...
    * now compute instance support static ip passed from api
    * add compute instance host_group openstack: bck and nobck
    * add field nvl_HostGroup in DescribeInstancesV20 api
    * add LoggingServiceAPI, MonitoringSpaceServiceAPI, MonitoringInstanceServiceAPI,
    * add ApiMonitoringService, ApiMonitoringSpace, ApiMonitoringInstance
* Risolto
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

* Aggiunto ...
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
* Risolto
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

* Aggiunto ...
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
* Risolto
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

* Aggiunto ...
  * add new api ping (with sql check), capabilities and versione to /v1.0/nas, /v1.0/nes, /v1.0/nws, /v1.0/nrs, /v1.0/gas
  * add service instance check api
  * add service instance name validation
  * add owner propagation from keypair to ssh key
* Risolto
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

* Aggiunto ...
* Risolto
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

* Aggiunto ...
    * add sql_stack_v2 with sql stack based on stack_v2
    * added dbaas api v2.0. Class ApiDatabaseServiceInstance was replaced with ApiDatabaseServiceInstanceV2
        * engine supported: mysql, postgresql, oracle, sqlserver
    * added ComputeCustomization and AppliedComputeCustomization to run ansible playbook on ComputeInstance
    * added ApiComputeInstance action to add/remove security group
    * added ApiComputeInstance action to add/remove/revert snapshots
    * added ApiServiceDefinition field config in update api
    * add resource entity api to clean cache
* Risolto
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

* Aggiunto
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
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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

* Aggiunto
* Risolto
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
