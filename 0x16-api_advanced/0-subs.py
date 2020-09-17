#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "miguel_cf"}).json()
    if response.get("error") == 404:
        return 0
    subs = response.get("data").get("subscribers")
    return subs
