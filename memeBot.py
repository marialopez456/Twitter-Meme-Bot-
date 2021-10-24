#authors Maria L, Adam W, Carl M 
#date created 10/23/2021
#HackThisFall Project
#twitter bot that uploads memes from a file every 30 minutes and replies to users


import time
import tweepy
from tweepy.models import Status
import glob
import random

consumer_key= "#################"
consumer_secret="##############################"

key ="##################################"
secret="###################################"
mention_id=1
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
FILE = "IDs.txt"

api = tweepy.API(auth)
def logID(id, file):
    f_write = open(file, "w")
    f_write.write(str(id))
    f_write.close()
    return 1
mention_id = 1
words = ["give me a meme","can i have a meme","meme pls", "meme please","gimme meme", "i will like a meme sir","i would love a meme","meme meme meme!"]
message = "here is your meme @{}"
file_path_type= ["C:\\Users\\umalo\\Downloads\\meme\\1.jpg","C:\\Users\\umalo\\Downloads\\meme\\2.jpg"
,"C:\\Users\\umalo\\Downloads\\meme\\3.jpg","C:\\Users\\umalo\\Downloads\\meme\\4.jpg","C:\\Users\\umalo\\Downloads\\meme\\4.jpg",
"C:\\Users\\umalo\\Downloads\\meme\\5.jpg","C:\\Users\\umalo\\Downloads\\meme\\6.jpg"
,"C:\\Users\\umalo\\Downloads\\meme\\7.jpg","C:\\Users\\umalo\\Downloads\\meme\\8.jpg" ]  
# The actual bot
while True:
    mentions = api.mentions_timeline(since_id=mention_id) 
    tweet_iterator = tweepy.Cursor(api.mentions_timeline).items()
    latest_tweet = list(tweet_iterator)[-1]
    # Iterating through each mention tweet
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        logID(mention_id, FILE)
        if mention.in_reply_to_status_id is None:
            if True in [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    tweetId= latest_tweet.user.id 
                    username = latest_tweet.user.id 
                    images= glob.glob(random.choice(file_path_type))
                    random_image = random.choice(images)
                    media = api.media_upload(random_image)
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str,media_ids = [media.media_id_string] )
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc)
                except StopIteration:
                   break
    time.sleep(40) # The bot will only check for mentions every 15 seconds, unless you tweak this value

