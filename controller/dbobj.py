import json
from controller.conf import use_sql, use_json
from controller.exceptions import ImproperConfig, ExpectedDictAsInput
from controller.conf import json_dbname


if use_sql:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from controller.db.createdb import DashboardDB, Base, sqlalchemy_engine

    class StoreSession(object):
        data = {}
        engine = create_engine(str(sqlalchemy_engine))
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        def __init__(self):
            pass

        def exists(self, key):
            r = self.session.query(DashboardDB).filter(id=key)
            if r:
                return True
            else:
                return False

        def add(self, key, value):
            if type(value) is dict:
                new_entry = DashboardDB(id=key, value=json.dumps(value))
                self.session.add(new_entry)
                self.session.commit()
            else:
                raise ExpectedDictAsInput()

        def get(self, key, default=False):
            # CODE PENDING
            pass


else:
    if use_json:
        class StoreSession(object):
            storage = 'controller/db/%s' % json_dbname
            data = {}

            def reload(self):
                try:
                    with open(self.storage, 'r') as f:
                        self.data = json.loads(f.read())
                        f.close()
                except FileNotFoundError:
                    print("run createDB before initiating main program.")

            def __init__(self):
                self.reload()

            def exists(self, key):
                if key in self.data:
                    return True
                else:
                    return False

            def add(self, key, value):
                self.data[key] = value
                with open(self.storage, 'w') as f:
                    json.dump(self.data, f, indent=2, sort_keys=True)
                    f.write('\n')
                    f.close()

                self.reload()

            def get(self, key, default=False):
                """
                Returns value of the requested key
                """
                return self.data.get(key, default)
    else:
        raise ImproperConfig(message="Provide json_dbname or sqlalchemy_engine in config file.")

if __name__ == '__main__':
    s = StoreSession()