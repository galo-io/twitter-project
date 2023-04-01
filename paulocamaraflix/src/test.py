from sql_connector import sqlConnector
import os
from dotenv import load_dotenv

load_dotenv()

sql = sqlConnector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT')
                  , database='tp')

query = """
SELECT first_tweet_id as tweet_id
     , genres
     , protagonist_name
     , protagonist_surname
     , occupations
     , occupation_complements
     , first_famous_people
     , second_famous_people
     , first_theme
     , second_theme
FROM tp.paulocamaraflix
WHERE date = (
    SELECT MAX(date)
    FROM tp.paulocamaraflix
);
"""

elements = sql.queryData(query=query)
print(type(elements[0]))
print(elements[0])