__author__ = 'harsh'

class ExpectedDictAsInput(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Dictionary required as input"
        else:
            self.message = message

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class ImproperConfig(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Provide all required configuration in config file."
        else:
            self.message = message

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class InvalidRemoteUrl(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Invalid or Blank remote iCal file/URL provided"
        else:
            self.message = message

        super().__init__(self.message)

    def __repr__(self):
        return self.message


class InvalidBugzillaSearchKey(Exception):
    def __init__(self, message=None, error=None, *args):
        if not message:
            self.message = "Invalid or Blank search keyword provided"
        else:
            self.message = message
        super().__init__(self.message)

    def __repr__(self):
        return self.message


class ExpectedListAsInput(Exception):
    def __init__(self, *args):
        self.message = "Expected input parameter as List []"
        super().__init__(self.message)

    def __repr__(self):
        return self.message