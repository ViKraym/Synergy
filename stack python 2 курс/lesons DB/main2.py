from orm.connection import Connection
from orm.session_builder import SessionBuilder
from orm.base_table import BaseTable
from orm.tables.users import Users

session = SessionBuilder(
    Connection(
        server='localhost',
        port=5432,
        user='postgres',
        password='password',
        dbname='synergy',
        sql_type='Postgresql'
    )
)

# BaseTable.metadata.drop_all(session.engine)
BaseTable.metadata.create_all(session.engine)