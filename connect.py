import sqlalchemy as s
import os

password = os.environ["PW_MYSQL_ROOT"]
database_name = "binance-battle"

#connection
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/{database_name}")
connection = engine.connect()
metadata = s.MetaData()

