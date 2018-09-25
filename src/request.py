import json
from os import getenv
from base64 import b64encode
from requests import request
from dotenv import load_dotenv
from pathlib import Path
from time import sleep

from . import url_parser

load_dotenv(dotenv_path=Path(".env"))

token_url = "https://accounts.spotify.com/api/token"


class Request:
    def __init__(self):
        self.client_id = getenv('CLIENT_ID')
        self.client_secret = getenv('CLIENT_SECRET')
        self.__authenticate()

    def get(self, url, query={}, parsed=False):
        """ Makes a get request to the Spotify API """
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        parsed_url = url_parser.parse(url) if not parsed else url
        response = request(
            "GET", parsed_url, headers=headers, params=query)
        if response.status_code == 200:
            # Successful GET request
            return json.loads(response.text)
        elif response.status_code == 401:
            # Need to reauthenticate
            self.__authenticate()
            return self.get(parsed_url, query, True)
        elif response.status_code == 429:
            # Rate limiting from Spotify API
            sleep(response.headers['Retry-After'])
            return self.get(parsed_url, query, True)
        else:
            raise Exception(response.text)

    def __authenticate(self):
        """ Generates an access token for the Spotify API """
        client_details = f'{self.client_id}:{self.client_secret}'.encode(
            'utf8')
        basic_auth = b64encode(client_details).decode('utf8')
        payload = "grant_type=client_credentials"
        headers = {
            'Authorization': f"Basic {basic_auth}",
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = request("POST", token_url,
                           data=payload, headers=headers)
        if response.status_code != 200:
            raise Exception("Unable to authenticate")
        parsed_response = json.loads(response.text)
        self.access_token = parsed_response['access_token']
