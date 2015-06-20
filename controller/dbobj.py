import json
from controller.conf import dbname


class StoreSession(object):
    storage = 'controller/db/%s' % dbname
    data = {}

    def reload(self):
        with open(self.storage,'r') as f:
            self.data = json.loads(f.read())
            f.close()

    def __init__(self):
        self.reload()

    def exists(self, key):
        if key in self.data:
            return True
        else:
            return False

    def add(self, key, value):
        self.data[key] = value
        with open(self.storage,'w') as f:
            json.dump(self.data, f, indent=2, sort_keys=True)
            f.write('\n')
            f.close()

        self.reload()

    def get(self, key, default=False):
        """
        Returns value of the requested key
        """
        return self.data.get(key, default)
