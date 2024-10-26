"""
MIT License

Copyright (c) 2024 Jordan Maxwell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from panda3d_rest import http

def get_itchio_api_key() -> str:
    """
    Returns the itch.io API key provided by the itch.io launcher.
    This is used to authenticate with the itch.io API.
    """

    # Get the API key from the environment
    api_key = os.getenv('ITCHIO_API_KEY')

    # Check if the API key is set
    if api_key is None:
        raise ValueError('ITCHIO_API_KEY environment variable is not set')

    return api_key

def get_itchio_api_key_expiration() -> str:
    """
    Returns the expiration date of the itch.io API key provided 
    by the itch.io launcher. This is used to determine when the
    API key should be refreshed.
    """

    # Get the API key expiration from the environment
    api_key_expiration = os.getenv('ITCHIO_API_KEY_EXPIRES_AT ')

    # Check if the API key expiration is set
    if api_key_expiration is None:
        raise ValueError('ITCHIO_API_KEY_EXPIRES_AT environment variable is not set')

    return api_key_expiration

def verify_launched_from_itchio() -> bool:
    """
    Verifies that the application was launched from the itch.io launcher.
    """

    # Check if the itch.io API key is set
    try:
        get_itchio_api_key()
    except ValueError:
        return False

    return True

def perform_itchio_api_request(url: str, callback: object, method='GET') -> None:
    """
    Performs an itch.io API request using the itch.io API key.
    """

    # Get the itch.io API key and the http client
    api_key = get_itchio_api_key()
    rest_client = http.HTTPRest()

    if method == 'GET':
        http_method = rest_client.perform_json_get_request
    elif method == 'POST':
        http_method = rest_client.perform_json_post_request
    else:
        raise ValueError('Invalid HTTP method: %s' % method)
    
    # Perform the request
    headers = {
        'Authorization': 'Bearer %s' % api_key
    }

    http_method(url, headers=headers, callback=callback)
    
def get_itchio_credential_info(callback: object) -> None:
    """
    Returns information on the set of credentials used to make this API request. In particular, 
    the response includes the list of scopes the credentials give access to, and if it's a JWT token, the expiration date
    """

    # Perform the itch.io API request
    perform_itchio_api_request('https://itch.io/api/1/jwt/credentials/info', callback)

def get_itchio_account_info(callback: object) -> None:
    """
    Fetches public profile data for the authenticated user.
    """

    # Perform the itch.io API request
    perform_itchio_api_request('https://itch.io/api/1/jwt/me', callback)

def get_itchio_account_games(callback: object) -> None:
    """
    Fetches a list of games the user has uploaded or is a collaborator on.
    """

    # Perform the itch.io API request
    perform_itchio_api_request('https://itch.io/api/1/jwt/my-games', callback)

def get_itchio_game_download_key(game_id: str, callback: object) -> None:
    """
    Checks if a download key exists for game and returns it.

    GAME_ID can be retrieved from the my-games API call above.

    Requires either of the following parameter:

    download_key: The download key to look up,
    or user_id: The user identifier to look up download keys for.
    or email: The e-mail to look up download keys for.
    You can use this API call to verify that someone has a valid download key to download the game.

    The download key can be extracted from a buyer’s download URL. For example:

    http://leafo.itch.io/x-moon/download/YWKse5jeAeuZ8w3a5qO2b2PId1sChw2B9b637w6z

    The download key would be YWKse5jeAeuZ8w3a5qO2b2PId1sChw2B9b637w6z.
    """

    # Perform the itch.io API request
    perform_itchio_api_request('https://itch.io/api/1/jwt/game/%s/download_keys' % game_id, callback)

def get_itchio_game_purchases(game_id: str, callback: object) -> None:
    """
    Returns the purchases an email address has created for a given game. Only successfully completed purchases are shown.

    GAME_ID can be retrieved from the my-games API call above.

    Requires either of the following parameters:

    email: The email address to look up purchases for,
    or user_id: The user identifier to look up purchases for.
    The call is aware of verified email addresses associated with the one you provide. Meaning if someone has the email person@example.com and has linked person2@example.com. You can request with either email address to get their purchase regardless of which email address it originated from.

    You can use this API call to verify that someone has bought your game on itch.io on your own server. You are responsible for verifying their email address first, otherwise they could attempt to guess an email they don'’'t own in order to fake ownership.
    """

    # Perform the itch.io API request
    perform_itchio_api_request('https://itch.io/api/1/jwt/game/%s/purchases' % game_id, callback)