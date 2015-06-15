from conf import conf
from git import GithubByUsername,GithubByRepo
from udd import UddbyEmail
"""
print(conf)
print(conf['private'][0].get("status",))
print(type(conf['private'][0].get("status",)))
---

r = ['dpocock/github-icalendar',]

g = GithubByRepo(r)
res = g.main()
print(res)
-----

r = ['ninjatrench','dpocock']
g = GithubByUsername(r)

res = g.main()
print(res)
----

r = ["daniel@pocock.pro","debian-accessibility@lists.debian.org"]
u = UddbyEmail(r)
res = u.main()

print(res)
print(type(res))
print(len(res))
"""
