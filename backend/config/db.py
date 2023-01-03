from sqlalchemy import create_engine , MetaData
import mysql.connector


""" cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='logincat')
"""""" parametros: tipo de db,usuario de db,nombre de db """

engine = create_engine("mysql+pymysql://root:@localhost:3306/logincat")


meta_data = MetaData()
