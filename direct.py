__author__ = 'harsh'
import requests
from icalendar import Calendar
from conf import debconf_url, ubuntu_events_url
from exceptions import InvalidRemoteUrl


class DirectUrl(object):

    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            raise InvalidRemoteUrl()

    def main(self):
        r = requests.get(self.url)
        print(r.url)

        obj = Calendar.from_ical(r.text)
        data = obj.walk()
        return data[1:]


class DebSummit(DirectUrl):
    def __init__(self, url=None):
        if not url:
            super().__init__(url=debconf_url)
        else:
            super().__init__(url=url)


class UbuntuEvents(DirectUrl):
    def __init__(self, url=None):
        if not url:
            super().__init__(url=ubuntu_events_url)
        else:
            super().__init__(url=url)