#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed
for a given subreddit."""
    if subreddit is None:
        print(None)
    ten_counter = 0
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "miguel_cf"}).json()
    hot_posts = response.get("data").get("children")
    for post in hot_posts:
        print(post.get("data").get("title"))
        ten_counter += 1
        if ten_counter == 10:
            break
