import pandas as pd
import sqlite3 as sql

def create_table(db: str, src: str, name: str):
    con = sql.connect(db)
    table = pd.read_csv(src)
    table.to_sql(name, con, index=False)

def create_table(db: str, schema: str, name: str):
    pass

def populate_table(db: str, src: str, table: str, skipFirst=False):
    pass
