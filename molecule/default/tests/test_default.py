import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ice_version(host):
    hostname = host.backend.get_hostname()
    assert host.exists('icegridnode')
    c = host.run('icegridnode --version')
    if hostname == 'ice-35':
        assert c.stderr.startswith('3.5.')
    else:
        assert c.stderr.startswith('3.6.')


def test_icepy_version(host):
    hostname = host.backend.get_hostname()
    c = host.run('python -c "import Ice; print Ice.stringVersion()"')
    if hostname == 'ice-35':
        assert c.stdout.startswith('3.5.')
    else:
        assert c.stdout.startswith('3.6.')


def test_ice_devel(host):
    hostname = host.backend.get_hostname()
    if hostname == 'ice-35':
        assert not host.package('ice-c++-devel').is_installed
    else:
        assert host.package('ice-all-devel').is_installed
