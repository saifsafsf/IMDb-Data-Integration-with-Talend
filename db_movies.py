from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import pandas as pd


password = quote_plus('your_pass_here')
port = 'your_port_here'
engine = create_engine(f'mysql://root:{password}@localhost:{port}')
conn = engine.connect()

pd.read_sql(text('CREATE DATABASE movies;'), conn)

conn.close()
