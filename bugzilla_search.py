__author__ = 'harsh'

from conf import bugzilla_base_url
import multiprocessing
from icalendar import Calendar
from exceptions import InvalidBugzillaSearchKey
from helper import list_of_strings
import requests


def mapper(keyword):
    url = bugzilla_base_url + "?ctype=ics&quicksearch=%s"
    keyword = str(keyword).replace(" ", "+")
    r = requests.get(url % keyword)
    print(r.url)
    obj = Calendar.from_ical(r.text)
    data = obj.walk()
    print(data[1:])
    return data[1:]


class BugzillAPI(object):
    items = []

    def __init__(self, keywords):
        """

        :param keywords: list
        :raise InvalidBugzillaSearchKey:
        """
        if keywords:
            self.keywords = list_of_strings(keywords)
        else:
            raise InvalidBugzillaSearchKey

    def main(self):
        p = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
        x = p.map(mapper, self.keywords)
        p.close()
        p.join()

        for i in x:
            for j in i:
                self.items.append(j)

        return self.items


if __name__ == '__main__':
    pass