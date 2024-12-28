from http.client import responses
from dotenv import load_dotenv
import os
import requests

class APIHandler:
    """
    Class responsible for interacting with the Azure Translator API. It manages
    API keys, endpoint configuration, and sends translation requests.
    """

    def __init__(self):
        """
        Initializes the APIHandler with environment variables for Azure API keys and endpoint.
        """
        load_dotenv()
        self._url = os.getenv("AZURE_ENDPOINT")
        self._key = os.getenv("AZURE_API_KEY")
        self._region = os.getenv("AZURE_REGION")
        self._content_type = "application/json"
        self._headers = {
            "Ocp-Apim-Subscription-Key": self._key,
            "Ocp-Apim-Subscription-Region": self._region,
            "Content-Type": self._content_type
        }

    def translate_text(self, request_body, target_lang, source_lang):
        """
        Sends a request to the Azure Translator API to translate text.

        Args:
            request_body (list): A list of dictionaries, each containing a chunk of text to translate.
            target_lang (str): The language code for the target language.
            source_lang (str): The language code for the source language.

        Returns:
            Response: The response object from the requests library.
        """
        url = f"{self._url}/translate?api-version=3.0&from={source_lang}&to={target_lang}"
        response = requests.post(url, headers=self._headers, json=request_body)
        return response