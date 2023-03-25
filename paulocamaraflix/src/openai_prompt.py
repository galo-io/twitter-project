from dotenv import load_dotenv
import os
from pathlib import Path
import random
import openai
from . import tp_logger

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
        
        # Random choice from the parameters on prompt if not passed on the params dictionary
        try:
            genres = params['genre']
        except:
            genres=random.choice(self.read_prompt('genres').split('\n'))
        
        try:
            protagonist_name=params['protagonist_name']
        except:
            protagonist_name=random.choice(self.read_prompt('protagonist_name').split('\n'))
        
        try:
            protagonist_surname=params['protagonist_surname']
        except:
            protagonist_surname=random.choice(self.read_prompt('protagonist_surname').split('\n'))
        
        try:
            occupations=params['occupations']
        except:
            occupations=random.choice(self.read_prompt('occupations').split('\n'))
        
        try:
            occupation_complements = params['occupation_complements']    
        except:
            occupation_complements=random.choice(self.read_prompt('occupation_complements').split('\n'))          
        
        try:
            adjectives=params['adjectives']
        except:
            adjectives=random.choice(self.read_prompt('adjectives').split('\n'))
        
        try:
            first_famous_people=params['first_famous_people']
        except:
            first_famous_people=random.choice(self.read_prompt('famous_people').split('\n'))
        
        try:
            second_famous_people=params['second_famous_people']
        except:
            second_famous_people=random.choice(self.read_prompt('famous_people').split('\n'))
        
        try:
            first_theme=params['first_theme']
        except:
            first_theme=random.choice(self.read_prompt('themes').split('\n'))
        
        try:
            second_theme=params['second_theme']
        except:
            second_theme=random.choice(self.read_prompt('themes').split('\n'))
       
        # Format Query
        query = prompt.format(
            genres=genres
          , protagonist_name=protagonist_name
          , protagonist_surname=protagonist_surname
          , occupations=occupations
          , occupation_complements=occupation_complements
          , adjectives=adjectives
          , first_famous_people=first_famous_people
          , second_famous_people=second_famous_people
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
          'genres':genres
        , 'protagonist_name':protagonist_name
        , 'protagonist_surname':protagonist_surname
        , 'occupations':occupations
        , 'occupation_complements':occupation_complements
        , 'adjectives':adjectives
        , 'first_famous_people':first_famous_people
        , 'second_famous_people':second_famous_people
        , 'first_theme':first_theme
        , 'second_theme':second_theme
        , 'generated_prompt':generated_prompt
        }
        
        return output
        