import logging
from pathlib import Path

class logConstructor():

    def __init__(self, file_name:str):
        self._file_name = file_name

    def createLogger(self):
        """
        Log instance wich creates a file in `logs` directory.

        Authors:
            @marcuscardona

        Since:
            03-2023
        """
        # Create the log and set the level to INFO
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Log's Format and Path
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
        path = Path(f'./logs/{self._file_name}.log')

        # Create the file
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger
