import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('titanic.csv')

engine = create_engine('postgres://kbgqljxh:QHI-WkUVtOcs-pFDVaPgU60nqANxVObL@isilo.db.elephantsql.com:5432/kbgqljxh')
df.to_sql('titanic_regress', con = engine)