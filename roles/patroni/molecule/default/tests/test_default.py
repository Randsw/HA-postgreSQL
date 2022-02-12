import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_listening_patroni_RESTAPI(host):
    assert host.socket("tcp://0.0.0.0:8008").is_listening

def test_patroni_is_running(host):
    assert host.service('patroni').is_running

def test_patroni_config_exist(host):
    patroni_conf = host.file('/etc/patroni/instance.yml')
    assert patroni_conf.exists

def test_listening_etcd(host):
    assert host.socket("tcp://127.0.0.1:2379").is_listening

def test_etcd_is_running(host):
    assert host.service('etcd').is_running

def test_etcd_config_exist(host):
    etcd_conf = host.file('/etc/etcd/etcd.yml')
    assert etcd_conf.exists

def test_postgres_config_exist(host):
    postgres_conf = host.file('/etc/postgresql/12/main/postgresql.conf')
    assert postgres_conf.exists