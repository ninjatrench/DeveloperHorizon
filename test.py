from bitbucket_issues import BitBucketAPI
from conf import conf
from git import GithubByUsername, GithubByRepo
from udd import UddbyEmail
from direct import DebSummit
from bugzilla_search import BugzillAPI


def print_conf():
    print(conf)
    print(conf['private'][0].get("status", ))
    print(type(conf['private'][0].get("status", )))


def github_by_repo():
    inputs = ['dpocock/github-icalendar', ]
    obj = GithubByRepo(inputs)
    resp = obj.main()
    print(resp)
    return resp


def github_by_username():
    inputs = ['ninjatrench', 'dpocock']
    obj = GithubByUsername(inputs)
    resp = obj.main()
    print(resp)
    return resp


def udd_by_email():
    inputs = ["daniel@pocock.pro", "debian-accessibility@lists.debian.org"]
    obj = UddbyEmail(inputs)
    resp = obj.main()
    print(resp)
    print(type(resp))
    print(len(resp))
    return resp


def deb_summit():
    obj = DebSummit()
    resp = obj.main()
    print(resp)
    return resp


def bugzilla_api():
    inputs = ['screen splash', 'ww']
    obj = BugzillAPI(inputs)
    resp = obj.main()
    print(resp)
    return resp


def bit_bucket():
    inputs = ["jagguli/aioweb", "jagguli/aioweb"]
    g = BitBucketAPI(inputs)
    resp = g.main()
    print(resp)
    print(len(resp))
    return resp

if __name__ == '__main__':
    pass