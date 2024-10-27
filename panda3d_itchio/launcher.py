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
