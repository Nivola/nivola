# Changelog

## Version 1.8 (Oct 23, 2020)

* Added ...
    * add sql_stack_v2 with sql stack based on stack_v2
    * added dbaas api v2.0. Class ApiDatabaseServiceInstance was replaced with ApiDatabaseServiceInstanceV2
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
  * beehive-service 1.6.0
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
