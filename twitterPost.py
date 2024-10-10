import tweepy
import API_keys

from loggingAndOutput import Logging
logging = Logging(True)


client = tweepy.Client(
    consumer_key=API_keys.twitter_API_key,
    consumer_secret=API_keys.twitter_API_key_secret,
    access_token=API_keys.twitter_access_token,
    access_token_secret=API_keys.twitter_access_token_secret
)

auth = tweepy.OAuth1UserHandler(
    API_keys.twitter_API_key,
    API_keys.twitter_API_key_secret,
    API_keys.twitter_access_token,
    API_keys.twitter_access_token_secret
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


    # error handling
    try:
        # post
        response = client.create_tweet(text=text, media_ids=mediaID_list)
        # get a return back
        logging.say(f"From Twitter Post: {response}")

    except Exception as e:
        logging.error(f"Error in Twitter Posting {e}")

