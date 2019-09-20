#!/usr/bin/python3
""" calls Reddit API and returns the number of subscribers """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ queries the Reddit API and returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {"User-Agent": "Diego"}
    subs = requests.get(url, headers=headers, allow_redirects=False,)
    if subs:
        data = subs.json().get('data')
        children = data.get("children")
        for child in children:
            data_child = child.get("data")
            title = data_child.get("title")
            hot_list.append(title)
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
