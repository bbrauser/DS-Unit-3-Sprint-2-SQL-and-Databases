import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('titanic.csv')


engine = create_engine('postgres://cwsewxgg:mrmUpCk3SyyGEG4kW_HczxWF-4JOL-O5@drona.db.elephantsql.com:5432/cwsewxgg')
df.to_sql('titanic', con = engine)