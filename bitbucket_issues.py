__author__ = 'harsh'

import requests
import json
import icalendar
import multiprocessing
import re
from conf import bitbucket_api_url, bitbucket_base_url


def make_url(url):
    if url and type(url) is str:
        url = url.replace("/1.0/repositories/","").replace("issues","issue")
        return str(bitbucket_base_url + url)
    else:
        return bitbucket_base_url

def make_todo(issue):
    print(issue)
    try:
        todo = icalendar.Todo()
        todo['uid'] = issue.get('local_id', None)
        todo['summary'] = issue.get('title', None)
        todo['description'] = str(issue.get('content', None))
        todo['url'] = make_url(issue.get("resource_uri", None))
        todo['created'] = issue.get('utc_created_on', None)
        todo['last-modified'] = issue.get('utc_last_updated', None)
        todo['status'] = 'NEEDS-ACTION'
        todo['emailID'] = ""
        todo['category'] = issue["metadata"].get('kind')
        todo['organizer'] = ""
        return todo

    except Exception as e:
        print(e)
        return None


class BitBucketAPI(object):
    Flag = True
    items = []

    def __init__(self, repos):
        self.repos = repos

    def main(self):
        try:
            for i in self.repos:
                self.items += self.fetch_issue_by_repo(i)

        except Exception as e:
            print(e)

        finally:
            return self.items

    def fetch_issue_by_repo(self, repo_name):
        repo_name_parts = str(repo_name).split('/')
        user = repo_name_parts[0]
        repo_title = repo_name_parts[1]
        if self.Flag:
            r = requests.get(bitbucket_api_url % (user, repo_title))
            data = json.loads(r.text)
            issues = data.get('issues', False)
            if issues:
                p = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
                items = p.map(make_todo, issues)
                p.close()
                p.join()
                return items
            else:
                return []