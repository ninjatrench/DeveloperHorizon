from conf import conf
from git import GithubByUsername,GithubByRepo
from udd import UddbyEmail
from direct import DebSummit
from icalendar import Calendar
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
----

d = DebSummit()
items = d.main()
print(items)
cal = Calendar()
cal.add('prodid', '-//danielpocock.com//GithubIssueFeed//')
cal.add('version', '2.0')
for i in items:
    cal.add_component(i)

def display(c):
    return c.to_ical().decode().replace("\r\n", "\n").replace("\r\n", "\n")

print(display(cal))

"""
