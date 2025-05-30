from base_table import BaseTable
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import *
import datetime

class Users(BaseTable):

    __tablename__ = 'Users'
    
    
    # ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ID: Mapped[BaseTable.type_annotation_map['IID']]
    Name: Mapped[str]
    Age: Mapped[int]
    CreatedOn: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTEMP'))
    UpdatedAr: Mapped[datetime.datetime] = mapped_column(server_default=text('CURRENT_TIMESTEMP'), onupdate = datetime.datetime.now())