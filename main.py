#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import pickle

from twitter_helper import connect_twitter


def load_newest_id():
    save_path = os.path.normpath(
        os.path.join(
            os.path.abspath(__file__), "../save_id/newest_tweet_id.pkl"
        )
    )
    try:
        with open(save_path, "rb") as loading_file:
            newest_id = pickle.load(loading_file)
    except FileNotFoundError:
        newest_id = None
    return newest_id


def get_jol_tweet(newest_id):
    twitter = connect_twitter("RT_bot")
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {"screen_name": "JorudanLive"}
    if newest_id is not None:
        params.update({"since_id": newest_id})
    else:
        pass
    req = twitter.get(url, params=params)
    timeline = json.loads(req.text)
    return timeline


def get_lines():
    lines_path = os.path.normpath(
        os.path.join(os.path.abspath(__file__), "../config/lines.json")
    )
    with open(lines_path, "r", encoding="utf-8") as lines_file:
        lines_org = json.load(lines_file)
        lines = lines_org["lines"]
    return lines


def get_lines_tweet(timeline, lines):
    rt_ids = []
    for tweet in timeline:
        for hashtag in tweet["entities"]["hashtags"]:
            if hashtag["text"] in lines:
                rt_ids.append(tweet["id"])
                break
            else:
                pass
    return rt_ids


def retweet(rt_ids):
    twitter = connect_twitter("RT_bot")
    params = {}
    for rt_id in reversed(rt_ids):
        url = (
            "https://api.twitter.com/1.1/statuses/retweet/"
            + str(rt_id)
            + ".json"
        )
        twitter.post(url, params=params)


def get_newest_id(timeline, newest_id_o):
    try:
        last = timeline[0]
        newest_id = last["id"]
    except IndexError:
        newest_id = newest_id_o
    return newest_id


def save_newest_id(newest_id):
    save_path = os.path.normpath(
        os.path.join(
            os.path.abspath(__file__), "../save_id/newest_tweet_id.pkl"
        )
    )
    with open(save_path, "wb") as saving_file:
        pickle.dump(newest_id, saving_file)


def main():
    newest_id_o = load_newest_id()
    timeline = get_jol_tweet(newest_id_o)
    lines = get_lines()
    rt_ids = get_lines_tweet(timeline, lines)
    retweet(rt_ids)
    newest_id_n = get_newest_id(timeline, newest_id_o)
    save_newest_id(newest_id_n)


if __name__ == "__main__":
    main()
