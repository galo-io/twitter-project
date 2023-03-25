import os
import datetime
import tweepy
from dotenv import load_dotenv
import time
from . import tp_logger
from . import utils

load_dotenv()

class twitterBot():
  
    def __init__(self, consumer_key, consumer_secret, bearer_token, access_token, access_token_secret):
        """
        Initializes an API client that authorizes our connection with Twitter.
        Also updates the last connection.

        The API Keys are stored in a .env file.

        Authors:
            @joaoreboucas1
            @marcuscardona

        Since:
            02-2023
        """
        self.client = tweepy.Client(consumer_key=consumer_key
                     , consumer_secret=consumer_secret
                     , bearer_token=bearer_token
                     , access_token=access_token
                     , access_token_secret=access_token_secret
                     , wait_on_rate_limit=True)
        self.last_connection = datetime.datetime.now()
        self._logger = tp_logger.logConstructor(file_name='twitter').createLogger()

    def remove_first_non_alphabetic_chars(text):
        """
        Removes spurious characters from the beginning of a string

        Inputs:
            text: string
        
        Outputs:
            text: string without spurious characters
        """

    def tweet(self, text, comment_to_tweet_id=None):
        """
        Tweets a string of text. If the length of text 280, a thread is created using the 
        long_text_into_tweets function. To comment on an existint tweet, one should pass the
        comment_to_tweet_id argument.

        Inputs:
            text = string of text
            comment_to_tweet_id = tweet id to comment on
        Outputs:
            A tweet from the username logged into the bot.

        Authors:
            @joaoreboucas1
            @marcuscardona
        
        Since:
            02-2023.
        """
        text = utils.stringUtils().remove_first_non_alphabetic_chars(text)
        if len(text) > 280:
            list_text = utils.stringUtils().turn_long_text_into_subtexts(text, subtext_length=280)
            for i, tweets in enumerate(list_text):
                if i == 0:
                    tweet_id = self.client.create_tweet(text=tweets, in_reply_to_tweet_id=comment_to_tweet_id).data['id']
                    first_id = tweet_id
                    self._logger.info(f'Tweet index {i+1} - Tweet ID: {tweet_id}')
                    time.sleep(10)
                else:
                    tweet_id = self.client.create_tweet(text=tweets
                                                           , in_reply_to_tweet_id = tweet_id).data['id']
                    self._logger.info(f'Tweet index {i+1} - Tweet ID: {tweet_id}')
                    time.sleep(10)
        else:
            tweet_id = self.client.create_tweet(text=text).data['id']
            first_id = tweet_id
            self._logger.info(f'Tweet index {1} - Tweet ID: {tweet_id}')
        
        return int(first_id)

    def send_dm(self, recipient_username, text):
        recipient_data = self.client.get_user(username=recipient_username)
        recipient_id = recipient_data.data.data['id']
        self.client.create_direct_message(participant_id=recipient_id, text=text)

