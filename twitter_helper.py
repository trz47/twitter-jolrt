#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from requests_oauthlib import OAuth1Session


def connect_twitter(account_type):
    key_parh = os.path.normpath(
        os.path.join(os.path.abspath(__file__), "../config/keys.json")
    )
    with open(key_parh, "r", encoding="utf-8") as keys_file:
        keys = json.load(keys_file)
    twitter = OAuth1Session(
        keys[account_type]["CONSUMER_KEY"],
        keys[account_type]["CONSUMER_SECRET"],
        keys[account_type]["ACCESS_TOKEN"],
        keys[account_type]["ACCESS_TOKEN_SECRET"],
    )
    return twitter


if __name__ == "__main__":
    # 接続確認用にタイムライン取得
    twitter = connect_twitter("RT_bot")
    params = {}
    req = twitter.get(
        "https://api.twitter.com/1.1/statuses/home_timeline.json",
        params=params,
    )
    timeline = json.loads(req.text)

    # ツイート本文表示
    for tweet in timeline:
        print(tweet["text"])
