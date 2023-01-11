from sqlalchemy import Table, Column , ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data
from model.provincias import provincias


""" parametros:nombre/metadata qu se crea en la conexion/columnas que se usan en la tabla """
users = Table("users", meta_data,
              Column("id", Integer, primary_key=True),
              Column("lastname", String(255), nullable=False),
              Column("name", String(255), nullable=False),
              Column("dni", String(255), nullable=False),
              Column("fnac", String(255), nullable=False),
              Column("adress", String(255), nullable=False),
              Column("id_Provincia",Integer,ForeignKey('provincias.id'))
              )

meta_data.create_all(engine)