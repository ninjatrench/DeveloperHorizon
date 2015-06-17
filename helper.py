__author__ = 'harsh'
from icalendar import Calendar
from exceptions import ExpectedListAsInput

list_of_strings = lambda items: [key for key in items if type(key) is str]
list_unique_items = lambda items: set(items)


def check_list(inputs) -> list:
    if type(inputs) is list:
        return inputs
    else:
        raise ExpectedListAsInput()


class CalendarBuilder(object):
    cal = Calendar()

    def __init__(self, items):
        self.items = check_list(items)

    def display(self) -> str:
        return self.cal.to_ical().decode().replace("\r\n", "\n").replace("\r\n", "\n")

    def build_calendar(self):
        self.cal.add('prodid', '-//<website>//DashboardHorizon//')
        self.cal.add('version', '2.0')
        for i in self.items:
            for j in i:
                self.cal.add_component(j)

    def main(self) -> str:
        try:
            self.build_calendar()
            resp = self.display()
            return resp

        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return "Calendar formatter class"