from src.twitter_bot import twitterBot
from src.openai_prompt import openaiPrompt
from src.sql_connector import sqlConnector
from dotenv import load_dotenv
from datetime import datetime
import os
load_dotenv()

def main():

    sql = sqlConnector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT')
                  , database='tp')
    
    # Get the last tweet from @paulocamaraflix
    query = sql.importQuery(filename='movie_review')
    
    # Save the result in a dictionary
    params=sql.queryData(query=query)[0]

    # Load the model
    prompt_generator = openaiPrompt()
    
    # Get the movie params output
    response_params = prompt_generator.get_response(prompt='movie_review', tokens = 1200, params=params)
    response = response_params['generated_prompt']

    # Twitter Bot
    bot = twitterBot(consumer_key=os.getenv('TWEEPY_CONSUMER_KEY_GALOCRITICA')
                   , consumer_secret=os.getenv('TWEEPY_CONSUMER_SECRET_GALOCRITICA')
                   , bearer_token=os.getenv('TWEEPY_BEARER_TOKEN_GALOCRITICA')
                   , access_token=os.getenv('TWEEPY_ACCESS_TOKEN_GALOCRITICA')
                   , access_token_secret=os.getenv('TWEEPY_ACCESS_TOKEN_SECRET_GALOCRITICA'))  

    tweet_id = bot.tweet(text=response, comment_to_tweet_id=params['movie_tweet_id'])
    
    # Store the data in DB
    schema ={
        'date': datetime.now().date()
      , 'tweet_id': tweet_id
      , 'movie_tweet_id': params['movie_tweet_id']
      , 'generated_review': str(response)
    }

    sql.insertInto(table_name='galocritica', json=schema)

if __name__ == '__main__':
    main()