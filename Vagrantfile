# -*- mode: ruby -*-
# vi: set ft=ruby :
UPDATE_HOSTS = <<-EOI
cat > /etc/hosts <<EOF
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.1.100 m1 m1.local.vm
192.168.1.200 r1 r1.local.vm
192.168.1.210 r2 r2.local.vm
192.168.1.220 r3 r3.local.vm
EOF
EOI

INSTALL_STANDALONE_MONGO = <<-EOI
echo "Copying mongodb-linux-x86_64-2.4.9.tgz to /home/vagrant"
cp /vagrant/mongodb-linux-x86_64-2.4.9.tgz /home/vagrant || {
  cd /home/vagrant
  wget -q http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
  cp /home/vagrant/mongodb-linux-x86_64-2.4.9.tgz /vagrant
}
echo "Extracting mongodb-2.4.9..." && tar xvzf mongodb-linux-x86_64-2.4.9.tgz -C /home/vagrant
echo "Creating link /home/vagrant/mongodb..." && ln -s /home/vagrant/mongodb-linux-x86_64-2.4.9 /home/vagrant/mongodb
mkdir -p /home/vagrant/mongodb/{log,data} && mkdir /home/vagrant/mongodb/data/db
chown -R vagrant:vagrant /home/vagrant/mongodb
echo "Starting mongodb..."
/home/vagrant/mongodb/bin/mongod --fork --logpath /home/vagrant/mongodb/log/mongo.log --logappend --dbpath /home/vagrant/mongodb/data/db --rest
EOI

INSTALL_FIRST_REPLICA_MONGO = <<-EOI
echo "Copying mongodb-linux-x86_64-2.4.9.tgz to /home/vagrant"
cp /vagrant/mongodb-linux-x86_64-2.4.9.tgz /home/vagrant || {
  cd /home/vagrant
  wget -q http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
  cp /home/vagrant/mongodb-linux-x86_64-2.4.9.tgz /vagrant
}

echo "Extracting mongodb-2.4.9..." && tar xvzf mongodb-linux-x86_64-2.4.9.tgz -C /home/vagrant
echo "Creating link /home/vagrant/mongodb..." && ln -s /home/vagrant/mongodb-linux-x86_64-2.4.9 /home/vagrant/mongodb
mkdir -p /home/vagrant/mongodb/{log,data} && mkdir /home/vagrant/mongodb/data/db
chown -R vagrant:vagrant /home/vagrant/mongodb
echo "Starting mongodb..."
/home/vagrant/mongodb/bin/mongod --fork --logpath /home/vagrant/mongodb/log/mongo.log --logappend --dbpath /home/vagrant/mongodb/data/db --replSet bcdo --rest
sleep 20
echo "Creating replica set..."
cat > /home/vagrant/create_replica.js <<FIN
rs.initiate()
FIN

echo "Creating script for adding other replicaset members..."
cat > /home/vagrant/add_members.js <<FIN
rs.add("r2:27017")
rs.add("r3:27017")

var conf = rs.config()
conf.members[0].tags = {'env':'production', 'dc':'pa'}
conf.members[1].tags = {'env':'production', 'dc':'nj'}
conf.members[2].tags = {'env':'production', 'dc':'pa'}

rs.reconfig(conf)
FIN

/home/vagrant/mongodb/bin/mongo < /home/vagrant/create_replica.js
EOI

INSTALL_NEXT_REPLICA_MONGO = <<-EOI
echo "Copying mongodb-linux-x86_64-2.4.9.tgz to /home/vagrant"
cp /vagrant/mongodb-linux-x86_64-2.4.9.tgz /home/vagrant || {
  cd /home/vagrant
  wget -q http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
  cp /home/vagrant/mongodb-linux-x86_64-2.4.9.tgz /vagrant
}
echo "Extracting mongodb-2.4.9..." && tar xvzf mongodb-linux-x86_64-2.4.9.tgz -C /home/vagrant
echo "Creating link /home/vagrant/mongodb..." && ln -s /home/vagrant/mongodb-linux-x86_64-2.4.9 /home/vagrant/mongodb
mkdir -p /home/vagrant/mongodb/{log,data} && mkdir /home/vagrant/mongodb/data/db
chown -R vagrant:vagrant /home/vagrant/mongodb
echo "Starting mongodb..."
/home/vagrant/mongodb/bin/mongod --fork --logpath /home/vagrant/mongodb/log/mongo.log --logappend --dbpath /home/vagrant/mongodb/data/db --replSet bcdo --rest
EOI

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
  
    m1.vm.provision :shell, :inline => UPDATE_HOSTS
    m1.vm.provision :shell, :inline => INSTALL_STANDALONE_MONGO
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
    
    r1.vm.provision :shell, :inline => UPDATE_HOSTS
    r1.vm.provision :shell, :inline => INSTALL_FIRST_REPLICA_MONGO
  end

  config.vm.define "r2" do |r2|
    r2.vm.box = "precise64"
    r2.vm.box_url = "http://files.vagrantup.com/precise64.box"
    r2.vm.network :forwarded_port, guest: 27017, host: 5000
    r2.vm.network :forwarded_port, guest: 28017, host: 5100
    r2.vm.network :private_network, ip: '192.168.1.210'
    r2.vm.hostname = "r2"
    r2.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'r2']
    end

    r2.vm.provision :shell, :inline => UPDATE_HOSTS
    r2.vm.provision :shell, :inline => INSTALL_NEXT_REPLICA_MONGO
  end

  config.vm.define "r3" do |r3|
    r3.vm.box = "precise64"
    r3.vm.box_url = "http://files.vagrantup.com/precise64.box"
    r3.vm.network :forwarded_port, guest: 27017, host: 6000
    r3.vm.network :forwarded_port, guest: 28017, host: 6100
    r3.vm.network :private_network, ip: '192.168.1.220'
    r3.vm.hostname = "r3"
    r3.vm.provider :virtualbox do |v|
      v.customize ['modifyvm', :id, '--name', 'r3']
    end

    r3.vm.provision :shell, :inline => UPDATE_HOSTS
    r3.vm.provision :shell, :inline => INSTALL_NEXT_REPLICA_MONGO
  end
end
