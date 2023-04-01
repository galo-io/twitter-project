from huggingface_hub.inference_api import InferenceApi
from dotenv import load_dotenv
import os

load_dotenv()

class huggingFaceInference():

    def __init__(self, token):
        self._access_token = token
    
    def bertModel(self):
        """
        Generates a Request to the BERT model in the hugging face hub for inference
        """
        inference=InferenceApi(repo_id='bert-base-multilingual-cased', token=self._access_token)
        pass
