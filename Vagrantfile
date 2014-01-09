# -*- mode: ruby -*-
# vi: set ft=ruby :
chef_server_key = ".chef/chef-validator.pem"
chef_server = "https://chef.local.vm"
chef_environment = "vagrant"

MONGO_INSTALL = <<-FIN
#!/bin/sh

if [ -f /etc/redhat-release ]; then
  test -d /var/lib/mongo || {
    echo "Installing MongoDB (ES variant)"
    cat > /etc/yum.repos.d/mongodb.repo <<EOI
[mongodb]
name=MongoDB Repository
baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
gpgcheck=0
enabled=1
EOI
    yum install -y mongo-10gen mongo-10gen-server
    service mongod start
}
elif [ -f /etc/debian_version ]; then
  echo "Debian-based system..."
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
  echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
  apt-get update
  apt-get install mongodb-10gen
fi  

# Update /etc/hosts
cat > /etc/hosts <<EOI
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.1.100  m1 m1.local.vm
192.168.1.200  m2 m2.local.vm
192.168.1.300  m3 m3.local.vm

EOI

FIN

Vagrant.configure("2") do |config|
  config.vm.define "m1" do |m1|
    m1.vm.box = "precise64"
    m1.vm.box_url = "http://files.vagrantup.com/precise64.box"
    m1.vm.network :forwarded_port, guest: 27017, host: 3000
    m1.vm.network :forwarded_port, guest: 28017, host: 3100
    m1.vm.network :private_network, ip: '192.168.1.100'
    m1.vm.hostname = "m1"
    m1.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'm1']
    end
    m1.vm.provision :shell, :inline => MONGO_INSTALL
  end

  config.vm.define "m2" do |m2|
    m2.vm.box = "precise64"
    m2.vm.box_url = "http://files.vagrantup.com/precise64.box"
    m2.vm.network :forwarded_port, guest: 27017, host: 4000
    m2.vm.network :forwarded_port, guest: 28017, host: 4100
    m2.vm.network :private_network, ip: '192.168.1.200'
    m2.vm.hostname = "m2"
    m2.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'm2']
    end
    m2.vm.provision :shell, :inline => MONGO_INSTALL
  end

  config.vm.define "m3" do |m3|
    m3.vm.box = "precise64"
    m3.vm.box_url = "http://files.vagrantup.com/precise64.box"
    m3.vm.network :forwarded_port, guest: 27017, host: 5000
    m3.vm.network :forwarded_port, guest: 28017, host: 5100
    m3.vm.network :private_network, ip: '192.168.1.300'
    m3.vm.hostname = "m3"
    m3.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'm3']
    end
    m3.vm.provision :shell, :inline => MONGO_INSTALL
  end
end
