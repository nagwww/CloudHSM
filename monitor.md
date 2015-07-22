# Monitoring your CloudHSM  

##  Using SNMP
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
```


- Setting up a rsyslog server on Ubuntu ( Install the latest version )

```
       sudo add-apt-repository ppa:adiscon/v8-stable
       sudo apt-get update
       sudo apt-get install rsyslog
```

- Using logstash to Ingest rsyslog to ElasticSearch
