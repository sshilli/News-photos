import tweepy

CONSUMER_KEY = "249E5GLxUhPCo8tKmi27R2Hdh"
CONSUMER_SECRET = "qWWBMwsHTvQDHF8GiA2H4vaszWilVpLH9LwtEkjEjuviqdI2R1"
ACCESS_TOKEN = "1178395130467733504-Yqu6RKsAO8flAwedtHFQwU2TR0mCCS"
ACCESS_TOKEN_SECRET = "bivNLppWzRFfn8tZMXPmgUI9gehVxGm3wtMsyzsLZep3P"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAI5ekAEAAAAATsu9FIydLn%2Fs0omflv0LzVu9pE4%3DnhOLu8xSz9TBJAfzlNK3HPY8cLvjFFbvzo3eIIoOc9tUtO1RKA"

def tweet(images, weekday):
    api = tweepy.Client(bearer_token=BEARER_TOKEN, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, 
    consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    api.create_tweet(text= weekday + "'s Photos!",
        media_ids=images)


