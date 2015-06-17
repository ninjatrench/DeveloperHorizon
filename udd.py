__author__ = 'harsh'

import requests
import json
import icalendar
import multiprocessing
from helper import check_list


def make_summary(issue) -> str:
    description = issue.get(":description", None)
    source = issue.get(":source", None)
    if source and description:
        s = "%s:%s" % (source, description)
        return s
    else:
        return str(description)


def build(issue):
    try:
        todo = icalendar.Todo()
        todo['summary'] = make_summary(issue)
        todo['description'] = issue.get(":details", None)
        todo['url'] = issue.get(":link", None)
        """
        todo['uid'] = ""
        todo['created'] = issue.created_at
        todo['last-modified'] = issue.updated_at
        todo['organizer'] = ''
        """
        todo['status'] = 'NEEDS-ACTION'
        todo['category'] = issue.get(":type", None)
        return todo

    except Exception as e:
        print(e)
        return None


class UddByEmail(object):
    Flag = True
    items = []

    def __init__(self, emails):
        """

        :type emails: list
        """
        self.emails = check_list(emails)

    def main(self) -> list:
        try:
            if self.Flag:
                for email in self.emails:
                    item = self.fetch_data(email=email)
                    self.items += item

        except Exception as e:
            print(e)

        finally:
            return self.items

    def fetch_data(self, email):
        r = requests.get("https://udd.debian.org/dmd/?format=json&email1=%s" % email)
        data = json.loads(r.text)
        p = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
        item = p.map(build, data)
        p.close()
        p.join()
        return item