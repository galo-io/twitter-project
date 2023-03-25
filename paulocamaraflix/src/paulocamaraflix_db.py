from sql_connector import sqlConnector
import os
from dotenv import load_dotenv

load_dotenv()

sql = sqlConnector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT')
                  , database='tp')

schema = {
    'date': 'date'
  , 'first_tweet_id': 'char(255)'
  , 'genres': 'char(255)'
  , 'protagonist_name': 'char(255)'
  , 'protagonist_surname': 'char(255)'
  , 'occupations': 'char(255)'
  , 'occupation_complements': 'char(255)'
  , 'adjectives': 'char(255)'
  , 'first_famous_people': 'char(255)'
  , 'second_famous_people': 'char(255)'
  , 'first_theme': 'char(255)'
  , 'second_theme': 'char(255)'
  , 'generated_movie': 'mediumtext'
}

sql.createDataBase('paulocamaraflix', schema)


schema = {
    'date': 'date'
  , 'tweet_id': 'char(255)'
  , 'movie_tweet_id': 'char(255)'
  , 'generated_review': 'mediumtext'
  
}

sql.createDataBase('galocritica', schema)
