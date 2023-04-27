from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, Meta_data

users = Table("users", Meta_data,
              Column("id", Integer, primary_key=True),
              Column("name", String(255), nullable=False),
              Column("username", String(255), nullable=False),
              Column("user_password", String(255), nullable=False))

Meta_data.create_all(engine)