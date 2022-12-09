from tweepy import API, OAuth1UserHandler

def __init__(self):
    self.CONSUMER_KEY = 'SSfJDg4QEF3V7KXFSjQs0IPOL'
    self.CONSUMER_SECRET = 'a3hUYEuXJz3K8u1YojBa9Y28mafWCndm2XXglapMC3yz8BxPy0'
    self.ACCESS_KEY = ''
    self.ACCESS_SECRET = ''


def tweet(self, weekday, images):
    auth = OAuth1UserHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET, callback="oob")
    auth_url = auth.get_authorization_url()
    print("Authorization URL: " + auth_url)

    verifier = input("Input PIN: ").strip()
    auth.get_access_token(verifier)
    self.ACCESS_KEY = auth.access_token
    self.ACCESS_SECRET = auth.access_token_secret
    print ("ACCESS_KEY = " + self.ACCESS_KEY)
    print ("ACCESS_SECRET = " + self.ACCESS_SECRET)


    api = API(auth)

    dayImages = []
    for image in images:
        rmed = api.media_upload(image)
        dayImages.append(rmed.image)
    
    statusT = weekday + "'s Photos!"
    api.update_status(media_ids = dayImages, status=statusT)
