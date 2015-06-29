from controller.conf import use_sql, use_json
from controller.exceptions import ImproperConfig


if use_sql:
    from controller.conf import sqlalchemy_engine
    from sqlalchemy import Column, TEXT
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine

    Base = declarative_base()

    class DashboardDB(Base):
        __tablename__ = 'dashboard'
        id = Column(TEXT, primary_key=False)
        name = Column(TEXT, nullable=False)

    engine = create_engine(str(sqlalchemy_engine))

    Base.metadata.create_all(engine)

else:
    if use_json:
        from controller.conf import json_dbname
        with open('%s' % json_dbname, 'w') as f:
            f.write('{}')
            f.close()
    else:
        raise ImproperConfig(message="Provide json_dbname or sqlalchemy_engine in config file.")



