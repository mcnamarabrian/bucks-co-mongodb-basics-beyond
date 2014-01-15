# Overview

This repository contains files referenced during the January 2014 Bucks County DevOps Meetup [MongoDB - The Basics and Slightly Beyond](http://www.meetup.com/Bucks-County-DevOps/events/153800082/).

## Vagrant

I have used [Vagrant](http://www.vagrantup.com/) to define several VMs.

* m1 => Standalone MongoDB instance
* r1 => Replica set member (node 1)
* r2 => Replica set member (node 2)
* r3 => Replica set member (node 3)

I have also used the [vagrant-cachier](https://github.com/fgrehm/vagrant-cachier) Vagrant plugin to cache packages/gems.

In order to bring up a bare-metal replica set, please do the following:

# Bring up the replicaset Vagrant VMs (vagrant up r1 && vagrant up r2 && vagrant up r3)

# Once r2 and r3 are booted, configure the replicaset from r1 (/home/vagrant/mongodb/bin/mongo < /home/vagrant/add_members.js)

# Connect to any of the Vagrant VMs (vagrant ssh r1)

# Open the mongo Javascript shell (/home/vagrant/mongodb/bin/mongo)

# Verify the status of the replicaset (rs.status())

## Scripts

I have created some Python scripts that use the PyMongo driver to interact with the Mongo replica set.

