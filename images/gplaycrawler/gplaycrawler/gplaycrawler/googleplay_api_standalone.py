from enum import IntEnum
from pprint import pprint
import requests

from gpapi.googleplay import GooglePlayAPI
from gpapi.googleplay import LoginError
from google.protobuf.message import DecodeError

from settings import token_url

class ERRORS(IntEnum):
    OK = 0
    TOKEN_DISPENSER_AUTH_ERROR = 5
    TOKEN_DISPENSER_SERVER_ERROR = 6
    KEYRING_NOT_INSTALLED = 10
    CANNOT_LOGIN_GPLAY = 15

def retrieve_token():
    r = requests.get(token_url)
    if r.text == 'Auth error':
        print('Token dispenser auth error, probably too many connections')
        sys.exit(ERRORS.TOKEN_DISPENSER_AUTH_ERROR)
    elif r.text == "Server error":
        print('Token dispenser server error')
        sys.exit(ERRORS.TOKEN_DISPENSER_SERVER_ERROR)
    token, gsfid = r.text.split(" ")
    return token, gsfid

def connect_to_googleplay_api():
    playstore_api = GooglePlayAPI(locale="en_US", timezone="UTC", device_codename='bacon')
    token, gsfid = retrieve_token()
    playstore_api.login(authSubToken=token, gsfId=int(gsfid, 16))
    return playstore_api

# if __name__ == '__main__':
#     playstore_api = connect_to_googleplay_api()
#     pprint(playstore_api.details('com.awcogagi.airwar'))