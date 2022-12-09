import tweepy

consumer_key = "o99Nn7p75iCgu2wR6M9b4Slvf"
consumer_secret = "GkRkrZlknxq2PMXcc4Sp5x0tPHFHFP5JD9zV3oWYnmQ5oZcyVt"
access_token = "RC1lSEhIbk54V0lBbUllQkhBUkE6MTpjaQ"
access_token_secret = "XqAxFtFd7dt_QCUyY-WfUoJw-0aCN8a03owGw7_2unKW40eQGY"

def tweet(images, weekday):
    client = tweepy.Client(access_token["access_token"])

    response = client.create_tweet( text= weekday + "'s Photos!",
        media_ids=images)
    print(f"https://twitter.com/user/status/{response.data['id']}")
