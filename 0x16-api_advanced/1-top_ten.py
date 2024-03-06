#!/usr/bin/python3
"""
Function queries Reddit API, prints the titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
            Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)"
    }

    params = {"limit": 10}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
