## Video HW by Junyou Chi
# Description
An api to get tweet online and convert to video to show the twitter posts

# Something new
I found that the queue system in old version is just a loop for tasks so I developed a new version for queue system and it should be fine. I uploaded the picture of running result for it.

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

# Run
run 'python Queue.py' to test the whole system. There are hardcoded keywords in Queue.py and you can change the keywords the the number of threads

or 

Import word2vid from hw4
and use word2vid(keyword) to use the word2vid part directly.


# result
I tested on my own computer and for test case in pytest file, I gave the videos in the file I uploaded. However, When I tested on github, the ffmpeg file cannot be installed due to the authority problems. This is the test result and videos are in project forder.
![Test Image 1](https://github.com/BUEC500C1/video-chijunyou/blob/master/result2.png)
