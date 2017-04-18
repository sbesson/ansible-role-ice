import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ice_version(Command, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    assert Command.exists('icegridnode')
    c = Command('icegridnode --version')
    if host == 'ice-35':
        assert c.stderr.startswith('3.5.')
    else:
        assert c.stderr.startswith('3.6.')


def test_icepy_version(Command, TestinfraBackend):
    host = TestinfraBackend.get_hostname()
    c = Command('python -c "import Ice; print Ice.stringVersion()"')
    if host == 'ice-35':
        assert c.stdout.startswith('3.5.')
    else:
        assert c.stdout.startswith('3.6.')
