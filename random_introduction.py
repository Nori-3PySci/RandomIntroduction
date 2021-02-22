# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import tweepy
import datetime
import random

account = "@account"

n_people = 1

time_now = datetime.datetime.now()

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


# -

def follower_listing(account):
    
    follower_id_all = tweepy.Cursor(api.followers_ids, id = account, cursor = -1).items()
    
    f_list = []
    
    for follower_id in follower_id_all:
        f_list.append(follower_id)
    
    return f_list


def get_name(id_list):
    
    n_list = []
    
    for user_id in id_list:
        n_list.append("@" + api.get_user(user_id).screen_name)
        
    return n_list


def intro_tweet(intro_name_list, n_people, time_now):
    tweet_content = '\n\n'.join(intro_name_list)
    api.update_status("ランダムでフォロワーさん" + str(n_people) + "人紹介！\n\n" + tweet_content + "\n\nいつもありがとうございます！\n\n" + time_now.strftime("%Y/%m/%d %H:%M:%S") + "\n\n#フォロー感謝砲")


def main(account, time_now, n_people):
    followerlist = follower_listing(account)
    intro_id_list = random.sample(followerlist, n_people)
    intro_name_list = get_name(intro_id_list)
    intro_tweet(intro_name_list, n_people, time_now)


if __name__ == '__main__':
    main(account, time_now, n_people)


