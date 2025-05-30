from connection import Connection
from session_builder import SessionBuilder
from base_table import BaseTable
from users import Users

session = SessionBuilder(
    Connection(
        server='localhost',
        port=5432,
        user='postgres',
        password='password',
        dbname='synergy',
        sql_type='PostgresSQL'
    )
)

# BaseTable.metadata.drop_all(session.engine)
BaseTable.metadata.create_all(session.engine)