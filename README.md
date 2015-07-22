# What is CloudHSM  

<img src="/images/elephant_new.jpg" width="800" height="500" />

 * CloudHSM is one of the many services from Amazon ( AWS )
 * If you are familar with HSM it is a HSM sitting in the Amazon Data center.
 * CloudHSM's are not Virtualized and these are Physical devices sitting in Amazon Data centers(VPC).
 * CloudHSM's are SafeNet Luna provisioned in the AWS VPC.

### What is a HSM ( Hardware Security Module )  
A physical computing device that 
- safeguards and 
- manages digital keys 
for cryptographic opertaions( Ex : symmetric key, asymmetric key opertaions)

### Key concept 
- Keys are created in the HSM
- Keys live in the HSM
- Keys die in the HSM

Bottom line a key never leaves the HSM.

## Getting started with CloudHSM
- Provisioning a new CloudHSM
-- Historical Info : In good old days you would open a ticket with Amazon with your VPC info/Region/subnet  and they would provision the HSM.
-- Auto provisoning using boto
--- AWS Charges an upfront fee of $5000.00 ( Please check the http://aws.amazon.com/cloudhsm/faqs/ for the exact amount ) when provisioning
--- You need the following to provision a CloudHSM
---- Region
---- Subnet
---- ssh key pair
When a HSM is provisioned all you see is a ENI in the AWS Console, which looks like

## How to monitor CloudHSM
###  Using SNMP
-- Create an SNMP user on CloudHSM as

```
 lunash*> sysconf snmp user add -s monitorhsm -authPa <**********> -authProtocol SHA -privPa <**********> -privPr AES
```
-- Re-start SNMP as
```
 lunash*> service restart snmp
```
Note
-- Sometimes SNMP is is not enabled by default on the HSM's. To enable SNMP
```
 lunash*> sysconf snmp enable
```

-- Perofrm a quick test to ensure you are able to get to SNMP as
```
 snmpget -v3 -u monitorhsm -l authPriv -a SHA -A ******* -x AES -X ****** 10.12.12.23 1.3.6.1.2.1.2.2.1.10.2

```

### Setting up remove logging for  CloudHSM using rsyslogs

- As the CloudHSM is provisoned in the VPC, your rsyslog instance also needs to be in the VPC.
- While provisining a new CloudHSM you can provide the IP of a rsyslog server so cloudHSM can forward the syslogs.
```
import boto


- Setting up a rsyslog server on Ubuntu ( Install the latest version )

```
       sudo add-apt-repository ppa:adiscon/v8-stable
       sudo apt-get update
       sudo apt-get install rsyslog
```

- Using logstash to Ingest rsyslog to ElasticSearch

## Alerting on CloudHSM


### CloudHSM Inventory
- It is common for orgs to have CloudHSM in different regions/environments/subnets
- Here is a quick script i use to get the CloudHSM Invntories across all the accounts/regions


## How to backup a CloudHSM
- Do you know CloudHSM can only be backed up to a CloudHSM Backup. This how a CloudHSM Backup looks like. 
 <img src="/images/hsm1.png" width="300" height="200" />
 <img src="/images/hsm2.png" width="300" height="200" />
- The one thing you cannot have it in the cloud as they need to be physically connect to a server/instance
- Obviosuly as the keys are sensitive you would want to have them backed up to the CloudHSM

## How to restore a CloudHSM Backup
- As important a backup is, it is equally important to test your restoures to ensure it works end to end.
