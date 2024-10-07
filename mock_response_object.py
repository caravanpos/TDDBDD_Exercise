#from unittest.mock import Mock
#from requests import Response

#Response objects have a status_code attribute

#m = Mock(spec=Response,
#         status_code=404,
#         content='{"error":"not found"}')

#m.foo() #raises attribute, Response has no foo()
#m.json() #no error json is valid on Response
#m.status_code #no error raised, 404 returned
#m.text #no error, text is valid on Response
#m.name #raises AttributeError: Response was no name

import requests
from unittest.mock import patch, MagicMock

def imdb_info(title: str) -> dict:
    """Get results for a movie by title"""
    print(f"Searching IMDB for {title}")
    results = requests.get(f"https://imdb-api.com/API/SearchTitle/{title}")
    if results.status_code == 200:
        return results.json()
    return {}

if __name__ == '__main__':
    with patch('__main__.requests.get') as imdb_mock:
        imdb_mock.return_value = MagicMock(
            spec=requests.Response,
            status_code=200,
            json=MagicMock(return_value='{"title":"Bambi", "year":"1942"}')
        )
        print(imdb_info("Bambi"))
