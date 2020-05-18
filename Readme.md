## Video HW by Junyou Chi
# Description
An api to get tweet online and convert to video to show the twitter posts

# api used
tweepy: Used to gether twitter posts

# functions
gettweets: get twitter post online
Queue: to hold the queue for convertion
getkeys: read key file to extract key
makeImages: convert text to video

# install
First run conda "install -r requirements.txt"
then type your tweeter key into keys file

run python hw4 to test

or 

Import word2vid from hw4
and use word2vid(keyword)


# result
I tested on my own computer and for test case in pytest file, I gave the videos in the file I uploaded. However, When I tested on github, the ffmpeg file cannot be installed due to the authority problems. This is the test result and videos are in project forder.
![Image text](https://raw.githubusercontent.com/BUEC500C1/twitter-summarizer-rest-service-chijunyou/master/result.png)
