import tweepy
import twitter_API_keys

from loggingAndOutput import Logging
logging = Logging(True)


client = tweepy.Client(
    consumer_key=twitter_API_keys.API_key,
    consumer_secret=twitter_API_keys.API_key_secret,
    access_token=twitter_API_keys.access_token,
    access_token_secret=twitter_API_keys.access_token_secret
)

auth = tweepy.OAuth1UserHandler(
    twitter_API_keys.API_key,
    twitter_API_keys.API_key_secret,
    twitter_API_keys.access_token,
    twitter_API_keys.access_token_secret
)


def postOnTwitter(text, listOfPathsToPhoto):
    # use the v1 API to upload images
    oldAPI = tweepy.API(auth)

    # upload and generate a list of the photoes to be posted
    mediaID_list = []
    if listOfPathsToPhoto != None:
        logging.log("there's a path", "\n")
        for path in listOfPathsToPhoto:
            logging.log(f'path is {path}', '\n')
            mediaToUpload = oldAPI.media_upload(path)
            mediaID_list.append(mediaToUpload.media_id)

    # post
    response = client.create_tweet(text=text, media_ids=mediaID_list)

    # get a return back
    logging.say(f"From Twitter Post: {response}")
