import os
import sys

from dotenv import load_dotenv

from src.twitter_bot import twitterBot
from src.rand_prompt import randomize_params, read_file
# from src.sql_connector import sqlConnector

# Hack for local import
sys.path.append("../../")
from llm_connect.interface import get_response

def main():
    
    load_dotenv()
    
    # Instantiate the Bot
    bot = twitterBot(consumer_key=os.getenv('TWEEPY_CONSUMER_KEY_PCF')
                   , consumer_secret=os.getenv('TWEEPY_CONSUMER_SECRET_PCF')
                   , bearer_token=os.getenv('TWEEPY_BEARER_TOKEN_PCF')
                   , access_token=os.getenv('TWEEPY_ACCESS_TOKEN_PCF')
                   , access_token_secret=os.getenv('TWEEPY_ACCESS_TOKEN_SECRET_PCF'))

    # Generate random prompt
    template = read_file("movie_script")
    genre, protagonist_name, protagonist_surname, \
    occupation, occupation_complement, adjective, \
    first_famous, second_famous, first_theme, second_theme = randomize_params()
    prompt = template.format(
        genre=genre
      , protagonist_name=protagonist_name
      , protagonist_surname=protagonist_surname
      , occupation=occupation
      , occupation_complement=occupation_complement
      , adjective=adjective
      , first_famous=first_famous
      , second_famous=second_famous
      , first_theme=first_theme
      , second_theme=second_theme
    )

    # Get the movie params output
    max_tries = 5
    tries = 0
    while tries < max_tries:
        response = get_response(prompt)
        if response is None:
            print("WARNING: could not get response from LLM. Trying again...")
            tries += 1
        else:
            break

    if response is None:
        print(f"ERROR: could not get response from LLM after {max_tries} tries.")
        exit(1)

    tweet_id = bot.tweet(text=response, comment_to_tweet_id=None)
    
    # Store the data in DB
    # 
    # schema ={
    #     'date': datetime.now().date()
    #   , 'first_tweet_id': tweet_id
    #   , 'genres': response_params['genres']
    #   , 'protagonist_name': response_params['protagonist_name']
    #   , 'protagonist_surname': response_params['protagonist_surname']
    #   , 'occupations': response_params['occupations']
    #   , 'occupation_complements': response_params['occupation_complements']
    #   , 'adjectives': response_params['adjectives']
    #   , 'first_famous_people': response_params['first_famous_people']
    #   , 'second_famous_people': response_params['second_famous_people']
    #   , 'first_theme': response_params['first_theme']
    #   , 'second_theme': response_params['second_theme']
    #   , 'generated_movie': str(response)
    # }
# 
    # sql = sqlConnector(username=os.getenv('SQL_USER')
    #               , password=os.getenv('SQL_PASSWORD')
    #               , server=os.getenv('SQL_SERVER')
    #               , port=os.getenv('SQL_PORT')
    #               , database='tp')
# 
    # sql.insertInto(table_name='paulocamaraflix', json=schema)

if __name__ == '__main__':
    main()