# Overview

This repository contains files referenced during the January 2014 Bucks County DevOps Meetup [MongoDB - The Basics and Slightly Beyond](http://www.meetup.com/Bucks-County-DevOps/events/153800082/).

## Vagrant

I have used [Vagrant](http://www.vagrantup.com/) to define several VMs.

* m1 => Standalone MongoDB instance
* r1 => Replica set member (node 1)
* r2 => Replica set member (node 2)
* r3 => Replica set member (node 3)

In order to bring up a stand-along mongo server, please do the following:

1. Bring up the standalone MongoDB instance:
```
vagrant up m1
```
2. Connect to the VM:
```
vagrant ssh m1
```
3. Open the Javascript Mongo shell:
```
mongo
```



In order to bring up a bare-metal replica set, please do the following:

1. Bring up the replicaset Vagrant VMs:
```
vagrant up r1 && vagrant up r2 && vagrant up r3
```
2. Connect to VM r1:
```
vagrant ssh r1
```
3. Configure the replicaset from r1:
```
mongo < /home/vagrant/add_members.js
```
4. Open the mongo Javascript Mongo shell:
```
mongo
```
5. Verify the status of the replicaset:
```
rs.status()
```
6.  Verify the configuration of the replicaset includes tags:
```
rs.config()
```

# Working with Sample Data
The examples in the Meetup will focus on working with a standard set of data.  

## Data Import
1. Once the replicaset is up and running, connect to the r1 Vagrant VM:
```
vagrant ssh m1
```
2. Import the sample dataset:
```
mongoimport -c attendees -d bcdo /vagrant/scripts/attendees.json --jsonArray
```