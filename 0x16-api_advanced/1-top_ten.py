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
    user = 'reddit_user'

    headers = {'User-Agent': user}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print('None')
    else:
        data = req.json()['data']
        post_list = data['children']

        for posts in post_list[0:10]:
            print(posts['data']['title'])
