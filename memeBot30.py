#authors Maria L, Adam W, Carl M 
#date created 10/23/2021
#HackThisFall Project
#twitter bot that uploads memes from a file every 30 minutes and replies to users

import time
import tweepy
from tweepy.models import Status
import glob
import random

consumer_key= "#####################"
consumer_secret="##########################"

key ="############################"
secret="###################################"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

file_path_type= ["C:\\Users\\umalo\\Downloads\\meme\\1.jpg","C:\\Users\\umalo\\Downloads\\meme\\2.jpg"
,"C:\\Users\\umalo\\Downloads\\meme\\3.jpg","C:\\Users\\umalo\\Downloads\\meme\\4.jpg","C:\\Users\\umalo\\Downloads\\meme\\4.jpg",
"C:\\Users\\umalo\\Downloads\\meme\\5.jpg","C:\\Users\\umalo\\Downloads\\meme\\6.jpg"
,"C:\\Users\\umalo\\Downloads\\meme\\7.jpg"]
while True: 
    images1= glob.glob(random.choice(file_path_type))
    random_image1= random.choice(images1)
    media1 = api.media_upload(random_image1)
    api.update_status("new meme uploaded ",media_ids = [media1.media_id_string])
    time.sleep(2000)
