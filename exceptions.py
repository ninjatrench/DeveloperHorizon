__author__ = 'harsh'


class ImproperConfig(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Provide all required configuration in config file."

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class InvalidRemoteUrl(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Invalid or Blank remote iCal file provided"

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class InvalidBugzillaSearchKey(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Invalid or Blank search keyword provided"

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class ExpectedListAsInput(Exception):
    def __init__(self, *args):
        self.message = "Expected input parameter as List []"
        super().__init__(self.message)

    def __repr__(self):
        return self.message