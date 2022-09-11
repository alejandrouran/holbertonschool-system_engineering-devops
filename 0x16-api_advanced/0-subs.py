#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""

import request
import sys


def number_of_subscribers(subreddit):
    """
    number of suscribes
    """
    try:
        base_url = 'https://www.reddit.com/r/'
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(
            base_url + '{}/about.json'.format(subreddit), headers=headers)
        return r.json().get('data').get('subscribers')
    except ValueError:
        return 0
