__author__ = 'harsh'
from icalendar import Calendar
from controller.exceptions import ExpectedListAsInput
import string
import random
from controller.dbobj import StoreSession

list_of_strings = lambda items: [key for key in items if type(key) is str]
list_unique_items = lambda items: set(items)


def generate_uid(n=12):
    s = ''.join(
        random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(n))
    return s


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


class FlaskError(object):
    something_went_wrong = {}

    def __init__(self, message=None):
        if message:
            self.something_went_wrong = {'Error': True,
                                         'Message': str(message)}
        else:
            self.something_went_wrong = {'Error': True,
                                         'Message': 'Some unknown error occurred, Please try again'}

    def get_error(self) -> dict:
        return self.something_went_wrong


class SaveSession(object):
    def __init__(self, **kwargs):
        try:
            print(kwargs)
            s = StoreSession()
            self.id = generate_uid()

            while s.exists(self.id):
                self.id = generate_uid()
            s.add(key=self.id, value=kwargs)

        except Exception as e:
            print(e)

    def save(self):
        return self.id
