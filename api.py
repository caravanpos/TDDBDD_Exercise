import requests
from unittest import mock


def imdb_info(site):
    """Get results for a testing by a title"""
    print(f"Searching Site for {site}")
    results = requests.get(f"{site}")    
    return results.status_code

if __name__ == '__main__':
    print(imdb_info("https://www.twitter2.com/"))