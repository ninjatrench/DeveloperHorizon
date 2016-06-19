from icalendar import Event
import feedparser


class FeedAPI(object):

    def __init__(self, url, type="RSS"):
        self.events = []
        self.url = url
        self.obj = None
        self.flag = False
        #self.load_parse()

    def load_parse(self):
        try :
            self.obj = feedparser.parse(self.url)
        except Exception as e:
            print(e)
            self.flag = False
        else:
            self.flag = True

    def build_event_atom(self, entry):
        e = Event()
        e['UID'] = entry.id
        e['SUMMARY'] = entry.title
        e['DESCRIPTION'] = entry.description
        e['URL'] = entry.link
        e['DTSTAMP'] = entry.published
        self.events.append(e)

    def build_event_rss(self, entry):
        e = Event()
        e['UID'] = entry.id
        e['SUMMARY'] = entry.title
        e['DESCRIPTION'] = entry.description
        e['URL'] = entry.link
        e['DTSTAMP'] = entry.date
        self.events.append(e)

    def flow_control(self):
        if self.flag:
            for i in self.obj.entries:
                self.build_event_rss(entry=i)
            return self.events
        return False


class AtomAPI(FeedAPI):
    def __init__(self, url):
        super().__init__(url=url, type="ATOM")

    def main(self):
        self.load_parse()
        resp = self.flow_control()
        if resp:
            return resp
        else:
            return []


class RssAPI(FeedAPI):
    def main(self):
        pass