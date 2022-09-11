#!/usr/bin/python3
"""
queries the Reddit API and returns
the number of subscribers
"""

import requests


def top_ten(subreddit):
    """
    ...
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'Alejandro Uran'}
    _size = {"limit": 10}
    r = requests.get(base_url, params=_size, head=head).json()
    child = r.get('data', {}).get('children', None)
    if child:
        for results in child:
            print(results.get('data').get('title'))
    else:
        print(None)
