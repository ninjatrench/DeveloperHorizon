__author__ = 'harsh'
from icalendar import Calendar

list_of_strings = lambda items: [key for key in items if type(key) is str]
list_unique_items = lambda items: set(items)


class CalendarBuilder(object):
    cal = Calendar()

    def __init__(self, items):
        self.items = list_of_strings(items)

    def display(self):
        return self.cal.to_ical().decode().replace("\r\n", "\n").replace("\r\n", "\n")

    def build_calendar(self):
        self.cal.add('prodid', '-//<website>//DashboardHorizon//')
        self.cal.add('version', '2.0')
        for i in self.items:
            self.cal.add_component(i)

    def main(self):
        try:
            self.build_calendar()
            resp = self.display()
            return resp

        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return "Calendar formatter class"