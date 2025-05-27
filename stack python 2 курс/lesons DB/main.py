from sqlalchemy import create_engine
import sqlalchemy as db

from sqlalchemy.orm import sessionmaker

connection_string = f"sqlite:///mydb.db"

engine = create_engine(connection_string)
metadata_obj = db.MetaData()

profile = db.Table(
    'profile',
    metadata_obj,
    db.Column('email', db.String, primary_key=True),
    db.Column('name', db.String),
    db.Column('contact', db.Integer),
    
)

metadata_obj.create_all(engine)

# Session = sessionmaker(bind=engine)
# Session = Session()