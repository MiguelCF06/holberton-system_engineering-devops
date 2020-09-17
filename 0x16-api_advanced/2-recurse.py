#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the
titles of all hot articles for a given subreddit."""
    if subreddit is None:
        return None
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    response = requests.get(url, headers={"User-Agent": "miguel_cf"}).json()
    titles = response.get("data").get("children")
    for article in titles:
        hot_list.append(article.get("data").get("title"))
    after = response.get("data").get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
