import tweepy

CONSUMER_KEY = "249E5GLxUhPCo8tKmi27R2Hdh"
CONSUMER_SECRET = "qWWBMwsHTvQDHF8GiA2H4vaszWilVpLH9LwtEkjEjuviqdI2R1"
ACCESS_TOKEN = "1178395130467733504-Yqu6RKsAO8flAwedtHFQwU2TR0mCCS"
ACCESS_TOKEN_SECRET = "bivNLppWzRFfn8tZMXPmgUI9gehVxGm3wtMsyzsLZep3P"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAI5ekAEAAAAATsu9FIydLn%2Fs0omflv0LzVu9pE4%3DnhOLu8xSz9TBJAfzlNK3HPY8cLvjFFbvzo3eIIoOc9tUtO1RKA"

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id="RC1lSEhIbk54V0lBbUllQkhBUkE6MTpjaQ",
    redirect_uri="http://127.0.0.1:8080",
    scope=["tweet.write"]
)

print(oauth2_user_handler.get_authorization_url())

authorization_response = input("http://127.0.0.1:8080")
access_token = oauth2_user_handler.fetch_token(authorization_response)

def tweet(images, weekday):
    client = tweepy.Client(access_token["access_token"])
    statusT = weekday + "'s Photos!"
    response = client.create_tweet(media_ids=images, text=statusT, user_auth=False)
    print(f"https://twitter.com/user/status/{response.data['id']}")
