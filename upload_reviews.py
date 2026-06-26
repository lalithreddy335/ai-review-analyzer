import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

conn = snowflake.connector.connect(
    user='LALITHREDDY08',
    password='Lalithreddy@08',
    account='majtqgn-cy84052',
    warehouse='DEV_WH',
    database='ECOMMERCE_DB',
    schema='RAW'
)

cursor = conn.cursor()
cursor.execute("USE DATABASE ECOMMERCE_DB")
cursor.execute("USE SCHEMA RAW")

df = pd.read_csv('analyzed_reviews.csv')
df.columns = [c.upper() for c in df.columns]

write_pandas(conn, df, 'AI_REVIEW_ANALYSIS', auto_create_table=True, overwrite=True)
print(f"✅ Uploaded {len(df)} analyzed reviews to Snowflake!")

conn.close()