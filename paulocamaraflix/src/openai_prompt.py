from dotenv import load_dotenv
import os
from pathlib import Path
import random
import openai

from . import tp_logger
from .rand_prompt import randomize_params

class openaiPrompt():

    def __init__(self):
        load_dotenv()
        self._api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self._api_key
        self._logger = tp_logger.logConstructor(file_name='openAI').createLogger()

    def read_prompt(self, filename):
        """
        Looks in `prompts/` directory for a text file. Pass in file name only, not extension.
        Example: `prompts/hello-world.txt` -> read_prompt('hello-world')

        Authors:
            @OthersideAI
        """
        
        return Path('./prompts/{0}.txt'.format(filename)).read_text(encoding='UTF-8')

    def get_response(self, prompt, tokens=1000, params={}):
        """
        Returns a Davinci-003 prompt generated from the choosen prompt from
        Authors:
            @marcuscardona
        
        Since:
            02-2023
        """
        # Load the movie_script prompt
        prompt = self.read_prompt(prompt)
        genre, protagonist_name, protagonist_surname, occupation, occupation_complement, adjective, first_famous, second_famous, first_theme, second_theme = randomize_params()
        
        # Format Query
        query = prompt.format(
            genres=genre
          , protagonist_name=protagonist_name
          , protagonist_surname=protagonist_surname
          , occupations=occupation
          , occupation_complements=occupation_complement
          , adjectives=adjective
          , first_famous_people=first_famous
          , second_famous_people=second_famous
          , first_theme=first_theme
          , second_theme=second_theme
        )

        # Create Generated Text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=query,
            temperature=0.6,
            max_tokens = tokens
        )

        # Get the text from the json response
        generated_prompt=response.choices[0].text
        
        self._logger.info(f'{response.usage.prompt_tokens} prompt + {response.usage.completion_tokens} completion = {response.usage.total_tokens} tokens')
             
        # Transform the parameters in list
        output = {
          'genres':genre
        , 'protagonist_name':protagonist_name
        , 'protagonist_surname':protagonist_surname
        , 'occupations':occupation
        , 'occupation_complements':occupation_complement
        , 'adjectives':adjective
        , 'first_famous_people':first_famous
        , 'second_famous_people':second_famous
        , 'first_theme':first_theme
        , 'second_theme':second_theme
        , 'generated_prompt':generated_prompt
        }
        
        return output
        