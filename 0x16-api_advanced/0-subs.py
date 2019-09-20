#!/usr/bin/python3
""" calls Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Diego"}
    subs = requests.get(url, headers=user_agent, allow_redirects=False)
    if subs:
        data = subs.json().get("data")
        num_subs = data.get("subscribers")
        return (num_subs)
    return (0)
