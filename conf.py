import yaml
default_file = "config/config.cfg"
default_token = ""

with open(default_file) as f:
    conf = yaml.load(f)

print(conf)

github_isPrivate = conf['github'][0].get("private",False)
github_access_token = conf['github'][1].get("api_token",default_token)

print(github_isPrivate)
print(github_access_token)