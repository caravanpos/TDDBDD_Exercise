import requests
from unittest import mock


def imdb_info(title):
    """Get results for a movie by a title"""
    print(f"Searching IMDB for {title}")
    results = requests.get(f"https://imdb-api.com/API/SearchTitle/{title}")
    return results

if __name__ == '__main__':
    """Run some mock tests"""
    with mock.patch('requests.get', return_value={'status_code': 200}) as dummy:
        print(imdb_info("Bambi"))