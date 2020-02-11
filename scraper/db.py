import os
import urllib
from contextlib import contextmanager

import sqlalchemy as sa
import sqlalchemy.ext.declarative as sa_ext_decl
from sqlalchemy import SMALLINT, VARCHAR, Column, Integer, DateTime

Base = sa_ext_decl.declarative_base()


class TopPhones(Base):
    __tablename__ = "TOP_PHONES"
    SNAP_TIME = Column(DateTime, primary_key=True)
    RANKING = Column(SMALLINT, primary_key=True)
    PHONE = Column(VARCHAR(255))
    DAILY_HITS = Column(Integer)


def sessionmaker(debug=os.getenv("DEBUG", "false").lower() in {"true", "1"}):
    connection_str = "{driver}://{user}:{pwd}@{server}/{db_name}".format(
        driver="mysql+pymysql",
        user=os.getenv("SQL_USERNAME"),
        pwd=os.getenv("SQL_PASSWORD"),
        server=os.getenv("SQL_SERVER"),
        db_name="master"
    )
    engine = sa.create_engine(connection_str, echo=debug)

    @sa.event.listens_for(engine, "before_cursor_execute")
    def dummy_receive_before_cursor_execute(conn, cursor, statement, params, context, executemany):
        if executemany:
            cursor.fast_executemany = True

    return sa.orm.sessionmaker(bind=engine)


# exposed for other modules:
Session = sessionmaker()


@contextmanager
def session_scope():
    """with statements are the preferred way to access sessions"""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def write_to_db(db_snaps):
    with session_scope() as session:
        session.bulk_insert_mappings(TopPhones, db_snaps)
