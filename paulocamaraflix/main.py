from src.twitter_bot import twitterBot
from src.openai_prompt import openaiPrompt
from src.sql_connector import sqlConnector
from dotenv import load_dotenv
from datetime import datetime
import os

def main():
    
    load_dotenv()
    
    # Instantiate the Bot
    bot = twitterBot(consumer_key=os.getenv('TWEEPY_CONSUMER_KEY_PCF')
                   , consumer_secret=os.getenv('TWEEPY_CONSUMER_SECRET_PCF')
                   , bearer_token=os.getenv('TWEEPY_BEARER_TOKEN_PCF')
                   , access_token=os.getenv('TWEEPY_ACCESS_TOKEN_PCF')
                   , access_token_secret=os.getenv('TWEEPY_ACCESS_TOKEN_SECRET_PCF'))

    prompt_generator = openaiPrompt()
    
    # Get the movie params output
    response_params = prompt_generator.get_response(prompt='movie_script', tokens = 1000)
    response = movies_params['generated_prompt']
        
    tweet_id = bot.tweet(text = response, comment_to_tweet_id=None)
    
    # Store the data in DB
    schema ={
        'date': datetime.now().date()
      , 'first_tweet_id': tweet_id
      , 'genres': response_params['genres']
      , 'protagonist_name': response_params['protagonist_name']
      , 'protagonist_surname': response_params['protagonist_surname']
      , 'occupations': response_params['occupations']
      , 'occupation_complements': response_params['occupation_complements']
      , 'adjectives': response_params['adjectives']
      , 'first_famous_people': response_params['first_famous_people']
      , 'second_famous_people': response_params['second_famous_people']
      , 'first_theme': response_params['first_theme']
      , 'second_theme': response_params['second_theme']
      , 'generated_movie': str(response)
    }

    sql = sqlConnector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT')
                  , database='tp')

    sql.insertInto(table_name='paulocamaraflix', json=schema)

if __name__ == '__main__':
    main()