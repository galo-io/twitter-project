from src.twitter_bot import twitterBot
from src.openai_prompt import openaiPrompt
from src.sql_connector import sqlConnector
from src.text_to_speech import tts
from dotenv import load_dotenv
from datetime import datetime
import os

def main():
    
    load_dotenv()
    
    sql = sqlConnector(username=os.getenv('SQL_USER')
                  , password=os.getenv('SQL_PASSWORD')
                  , server=os.getenv('SQL_SERVER')
                  , port=os.getenv('SQL_PORT')
                  , database='tp')
    
    # Get the last tweet from @paulocamaraflix
    query = """
        SELECT generated_movie
        FROM tp.paulocamaraflix
        WHERE date = (
            SELECT MAX(date)
            FROM tp.paulocamaraflix
        );
    """
    # Save the result in a dictionary
    params=sql.queryData(query=query)[0]

    audio = tts().generate_audio(text=params['generated_movie'], filename='audio_paulocamaraflix')
    
if __name__ == '__main__':
    main()