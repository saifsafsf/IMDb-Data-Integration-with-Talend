from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd


password = quote_plus('$@!#isSQL11')
engine = create_engine(f'mysql://root:{password}@localhost:3306')
conn = engine.connect()

pd.read_sql(text('CREATE DATABASE movies;'), conn)

conn.close()