import praw 
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='uNyVpBjMbWzxIQ', \
                     client_secret='DiRSAS3ZJ0gfDNYKZmp4-iwRVxE', \
                     user_agent='redditScraper', \
                     username ='zakapalooza', \
                     password='Sam!102589')

subreddit = reddit.subreddit('art')

zmd = reddit.redditor(name='zakapalooza')
listgen = zmd.saved

for post in listgen:
    print(post)


top_subreddit = subreddit.top()

##for submission in subreddit.top():
   ## print(submission.title, submission.id)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], 
                "comms_num": [], \
                "created": [], \
                "body":[]
                }

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
print(topics_data)
