import yaml
import pkg_resources
from controller.exceptions import ImproperConfig

Flag = False
use_json = False
use_sql = False
github_token_exists = False

# Default file location of config file, give absolute path only
default_config_file = "/home/harsh/Desktop/dashboard/config/config.cfg"

# Dependent python modules. refer documentation on how to install them
dependency = [
    "requests",
    "Flask",
    "PyYaml",
    "PyGithub",
    "icalendar",
    "aiohttp"
]
pkg_resources.require(dependency)

with open(default_config_file) as f:
    conf = yaml.load(f)

# Setting for flask web server
bind_address = conf.get('bind_address', False)
bind_port = conf.get('bind_port', False)

# Setting for conference and event URL
debconf_url = conf.get('debconf_url', False)
ubuntu_events_url = conf.get('ubuntu_events_url', False)

# Other data sources. Base url is url of remote rest api. (very less likely to change)
bugzilla_base_url = conf.get('bugzilla_base_url', False)
bitbucket_base_url = conf.get('bitbucket_base_url', False)
bitbucket_api_url = conf.get('bitbucket_api_url', False)

#S ync Private repository on github
github_isPrivate = conf.get('github_is_private', False)
github_access_token = conf.get('github_access_token', False)

# choose database type, either json storage or SQL
# JSON will be stored on file system
# SQL-alchemy is used which supports sqlite3, mysql, posgresql
json_dbname = conf.get('json_dbname', False)
sqlalchemy_engine = conf.get('sqlalchemy_engine', False)


# URL shortening service by Debian
deb_li_base_url = conf.get('deb_li_base_url', False)
deb_li_api_url = conf.get('deb_li_api_url', False)

# Verifying config file inputs and configurations.
if sqlalchemy_engine:
    use_sql = True

if json_dbname:
    use_json = True

# IF JSON AND SQL both are mentioned then SQL is given priority

if use_json or use_sql:
    pass
else:
    raise ImproperConfig(message="Provide json_dbname or sqlalchemy_engine in config file.")

if github_access_token:
    github_token_exists = True

if github_isPrivate:
    if github_access_token:
        Flag = True
    else:
        raise ImproperConfig(message="github repository mode is set to private but github_access_token is missing")

if deb_li_api_url and deb_li_base_url:
    pass
else:
    raise ImproperConfig(message="Provide valid 'deb_li_base_url' and  'deb_li_api_url'")

try:
    assert debconf_url
    assert ubuntu_events_url
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