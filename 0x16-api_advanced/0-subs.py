#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    number of suscribes
    """
    r = requests.get("https://www.reddit.com/r/{}/about.json"
                     .format(subreddit),
                     headers={"User-Agent": "My-User-Agent"},
                     allow_r=False)
    if r.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
