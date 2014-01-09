# -*- mode: ruby -*-
# vi: set ft=ruby :
chef_server_key = ".chef/chef-validator.pem"
chef_server = "https://chef.local.vm"
chef_environment = "vagrant"

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
  
    m1.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = ["cookbooks"]
      chef.add_recipe "mongodb::default"
    end
    
  end

  config.vm.define "r1" do |r1|
    r1.vm.box = "precise64"
    r1.vm.box_url = "http://files.vagrantup.com/precise64.box"
    r1.vm.network :forwarded_port, guest: 27017, host: 4000
    r1.vm.network :forwarded_port, guest: 28017, host: 4100
    r1.vm.network :private_network, ip: '192.168.1.200'
    r1.vm.hostname = "r1"
    r1.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'r1']
    end
    
    r1.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = ["cookbooks"]
      chef.add_recipe "mongodb::default"
      chef.add_recipe "mongodb::replicaset"
    end
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
