import yaml
import pkg_resources
from exceptions import ImproperConfig

default_config_file = "config/config.cfg"
dependency = [
    "requests",
    "Flask",
    "Flask-Classy",
    "PyYaml",
    "PyGithub",
    "icalendar"
]
pkg_resources.require(dependency)

with open(default_config_file) as f:
    conf = yaml.load(f)

dbname = conf.get('dbname', False)
bind_address = conf.get('bind_address', False)
bind_port = conf.get('bind_port', False)
debconf_url = conf.get('debconf_url', False)
ubuntu_events_url = conf.get('ubuntu_events_url', False)

bugzilla_base_url = conf.get('bugzilla_base_url', False)

bitbucket_base_url = conf.get('bitbucket_base_url', False)
bitbucket_api_url = conf.get('bitbucket_api_url', False)

if 'github' in conf:
    if len(conf['github']) == 2:
        github_isPrivate = conf['github'][0].get("private", False)
        github_access_token = conf['github'][1].get("api_token")
    else:
        raise ImproperConfig("Provide Github configurations including private and api_token.")
else:
    raise ImproperConfig()

try:
    assert debconf_url
    assert ubuntu_events_url
    assert github_access_token
    assert dbname
    assert bind_address, bind_port
    assert bugzilla_base_url
    assert bitbucket_base_url
    assert bitbucket_api_url

except Exception:
    raise ImproperConfig()


if __name__ == '__main__':
    pass
#print(conf)
#print(github_isPrivate)
#print(github_access_token)
