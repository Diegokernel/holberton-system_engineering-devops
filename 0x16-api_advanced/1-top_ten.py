#!/usr/bin/python3
""" calls Reddit API and returns the number of subscribers """
import requests


def top_ten(subreddit):
    """ queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {"User-Agent": "Diego"}
    payload = {"limit": "10"}
    subs = requests.get(url, headers=user_agent, allow_redirects=False,
                        params=payload)
    if subs:
        data = subs.json().get("data")
        for child in data.get('children'):
            data_child = child.get('data')
            print(data_child.get('title'))
    else:
        print(None)
