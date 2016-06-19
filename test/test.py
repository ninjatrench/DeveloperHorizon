from controller.bitbucket_issues import BitBucketAPI
from controller.conf import conf
from controller.git import GithubByUsername, GithubByRepo
from controller.udd import UddByEmail
from controller.direct import DebSummit, UbuntuEvents
from controller.bugzilla_search import BugzillAPI
from controller.rss import RssAPI, AtomAPI
from controller.helper import CalendarBuilder


def print_conf():
    print(conf)
    print(conf['github'][0])
    print(type(conf['github'][0]))


def github_by_repo():
    inputs = ['dpocock/github-icalendar', 'ninjatrench/DeveloperHorizon']
    obj = GithubByRepo(inputs)
    resp = obj.main()
    # print(resp)
    return resp


def github_by_username():
    inputs = ['ninjatrench', 'dpocock']
    obj = GithubByUsername(inputs)
    resp = obj.main()
    # print(resp)
    return resp


def udd_by_email():
    inputs = ["daniel@pocock.pro", "debian-accessibility@lists.debian.org"]
    obj = UddByEmail(inputs)
    resp = obj.main()
    # print(resp)
    # print(type(resp))
    # print(len(resp))
    return resp


def ubuntu_events():
    obj = UbuntuEvents()
    resp = obj.main()
    # print(resp)
    return resp


def deb_summit():
    obj = DebSummit()
    resp = obj.main()
    # print(resp)
    return resp


def bugzilla_api():
    inputs = ['screen splash', 'ww']
    obj = BugzillAPI(inputs)
    resp = obj.main()
    # print(resp)
    return resp


def bit_bucket():
    inputs = ["jagguli/aioweb", "jagguli/aioweb"]
    g = BitBucketAPI(inputs)
    resp = g.main()
    # print(resp)
    # print(len(resp))
    return resp


def rss_feeds():
    r = RssAPI("http://lwn.net/headlines/newrss")
    resp = r.main()
    return resp

def atom_feeds():
    a = AtomAPI("https://www.gentoo.org/feeds/news.xml")
    resp = a.main()
    return resp


def test_build_all():
    # print_conf()
    items = []

    items.append(github_by_username())
    items.append(github_by_repo())
    items.append(udd_by_email())
    items.append(deb_summit())
    items.append(ubuntu_events())
    items.append(bugzilla_api())
    items.append(bit_bucket())
    items.append(rss_feeds())
    items.append(atom_feeds())

    c = CalendarBuilder(items)
    print("Started Building")
    resp = c.main()
    if resp:
        # print(resp)
        with open('test.ical', 'w') as f:
            f.write(resp)

    print("Finished")


if __name__ == '__main__':
    # test_build_all()
    import timeit

    print(timeit.timeit("test_build_all()", number=1, setup="from __main__ import test_build_all"))