import random
from pathlib import Path

def read_file(file_stem: str) -> str:
    """
    Looks in `prompts/` directory for a text file. Pass in file name only (i.e. the stem), not extension.
    Returns the contents of the file
    Example: `prompts/hello-world.txt` -> read_file('prompts/hello-world.txt')

    Authors:
        @OthersideAI
    """
    
    return Path(f"prompts/{file_stem}.txt").read_text(encoding='UTF-8')

PromptParams = list[str]

def randomize_params() -> PromptParams:
    '''
    Description: generates random parameters for the prompt placeholders
    Output:
        `prompt_params`: a list containing all randomized data for the prompt
    '''
    genre                 = random.choice(read_file('genres').split('\n'))
    protagonist_name      = random.choice(read_file('protagonist_name').split('\n'))
    protagonist_surname   = random.choice(read_file('protagonist_surname').split('\n'))
    occupation            = random.choice(read_file('occupations').split('\n'))
    occupation_complement = random.choice(read_file('occupation_complements').split('\n'))
    adjective             = random.choice(read_file('adjectives').split('\n'))
    first_famous          = random.choice(read_file('famous_people').split('\n'))
    second_famous         = random.choice(read_file('famous_people').split('\n'))
    first_theme           = random.choice(read_file('themes').split('\n'))
    second_theme          = random.choice(read_file('themes').split('\n'))
    return [
        genre,
        protagonist_name,
        protagonist_surname,
        occupation,
        occupation_complement,
        adjective,
        first_famous,
        second_famous,
        first_theme,
        second_theme
    ]
