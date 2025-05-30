from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy.orm import Mapper, mapped_column

from sqlalchemy import inspection



class BaseTable(DeclarativeBase):
    __abstract__ = True
    
    type_annotation_map = {
        "IID": Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
        }
    
    def __init__(self, **args):
        columns = self.__table__.c.keys()
        for key, value in args.items():
            if key in columns: setattr(self, key, value)