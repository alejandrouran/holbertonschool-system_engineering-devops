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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)

    if r.status == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
