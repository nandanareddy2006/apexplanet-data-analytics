from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///../sales.db")

def run_query(query):
    return pd.read_sql(query, engine)