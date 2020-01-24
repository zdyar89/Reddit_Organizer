import praw 
import pandas as pd
import datetime as dt

username = input('What is your reddit name?: ')
password = input('What is your password?: ')

reddit = praw.Reddit(client_id='uNyVpBjMbWzxIQ', \
                     client_secret='DiRSAS3ZJ0gfDNYKZmp4-iwRVxE', \
                     user_agent='redditScraper', \
                     username =username, \
                     password=password)

zmd = reddit.user.me()

savedpostsdict = {"saved content url": [], \
                "saved content title": []}
savedcommentsdict = {"saved comments": []}

savedcontent = zmd.saved(limit=50)

for submission in savedcontent:
    if isinstance(submission, praw.models.Comment):
        savedcommentsdict["saved comments"].append(submission.body)
    elif isinstance(submission, praw.models.Comment):
        savedpostsdict["saved content url"].append(submission.url)
        savedpostsdict["saved content title"].append(submission.title)

present_posts_data= pd.DataFrame(savedpostsdict)
present_comments_data = pd.DataFrame(savedcommentsdict)
present_posts_data.to_csv('savedredditposts.csv', index=True)
present_comments_data.to_csv('savedredditcomments.csv', index=True)
