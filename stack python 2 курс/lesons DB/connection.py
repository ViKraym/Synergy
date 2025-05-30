class Connection:
    def __init__(self, user, password, server, port, sql_type, **args):
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.sql_type = sql_type
        self.args = args
        
    @property
    def engine(self):
        if self.sql_type == "PostgresSQL":
            return f'postgresql://{self.user}:{self.password}@{self.server}:{str(self.port)}/{self.args["dbname"]}'