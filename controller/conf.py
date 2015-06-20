import yaml
import pkg_resources
from controller.exceptions import ImproperConfig
Flag = False
github_token_exists = False

default_config_file = "/home/harsh/Desktop/dashboard/config/config.cfg"
dependency = [
    "requests",
    "Flask",
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

github_isPrivate = conf.get('github_is_private', False)
github_access_token = conf.get('github_access_token', False)

if github_access_token:
    github_token_exists = True

if github_isPrivate:
    if github_access_token:
        Flag = True
    else:
        raise ImproperConfig(message="github repository mode is set to private but github_access_token is missing")

try:
    assert debconf_url
    assert ubuntu_events_url
    assert dbname
    assert bind_address, bind_port
    assert bugzilla_base_url
    assert bitbucket_base_url
    assert bitbucket_api_url
    Flag = True

except Exception as e:
    print(e)
    Flag = False


if __name__ == '__main__':
    if not Flag:
        raise ImproperConfig()