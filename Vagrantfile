# -*- mode: ruby -*-
# vi: set ft=ruby :
$postgres_instance_num = 2
$vm_ip_addr_start = 210
$bridge = "wlxa0a3f0908fbc" #name of network interface with internet connection 
$vm_cidr = "192.168.0" # virtual machines CIDR
Vagrant.configure("2") do |config|
    config.vm.box = "generic/ubuntu2004"
    config.vm.box_check_update = false
    (1..$postgres_instance_num).each do |i|
        config.vm.define "postgres-#{i}" do |node|
            node.vm.network "public_network", ip: "#{$vm_cidr}.#{$vm_ip_addr_start+i}", bridge: $bridge
            node.vm.hostname = "postgres-#{i}"
            node.vm.provider "virtualbox" do |vb|
                vb.gui = false
                vb.memory = "2048"
                vb.cpus=1
            end
        end
    end
    config.vm.define "etcd" do |node|
        node.vm.network "public_network", ip: "#{$vm_cidr}.#{$vm_ip_addr_start+$postgres_instance_num + 1}", bridge: $bridge
        node.vm.hostname = "etcd"
        node.vm.provider "virtualbox" do |vb|
            vb.gui = false
            vb.memory = "2048"
            vb.cpus=1
        end
    end
    config.vm.define "haproxy" do |node|
        node.vm.network "public_network", ip: "#{$vm_cidr}.#{$vm_ip_addr_start+$postgres_instance_num + 2}", bridge: $bridge
        node.vm.hostname = "haproxy"
        node.vm.provider "virtualbox" do |vb|
            vb.gui = false
            vb.memory = "2048"
            vb.cpus=1
        end
    end     
end