# Will be using praw modules. And pandas to format the scraped data to port to .csv file
import praw
import pandas as pd

# Ask for user authentication first
usernamed = '' #input("What's your username? ")
passwrd = '' #input("What's your password? ")

# User will need to create an app in reddit and put in the id and secret tokens to use this
reddit = praw.Reddit(client_id='uNyVpBjMbWzxIQ', \
                    client_secret='DiRSAS3ZJ0gfDNYKZmp4-iwRVxE', \
                    user_agent='redditScraper', \
                    username=usernamed, \
                    password=passwrd)

# Created two dictionaries to store the saved content. One for posts and one for comments since they can't mingle
#savedpostsdict = {"subreddit": [], \"saved content url":[], \"saved content title":[] }

savedpostsdict = {'key': 'value'}

# Scrapes all of the user's own content
savedcontent = reddit.user.me().saved(limit=None)

# Checks each saved content to see if it is a comment or submitted post instance and appends to respective dictionaries
for submission in savedcontent:
    if isinstance(submission, praw.models.Submission):
            savedpostsdict.update( {str(submission.subreddit) : submission.url} )

count = 0


for items in sorted(savedpostsdict.keys()):
    print(items , " : " , savedpostsdict[items])
    count += 1

print(count)
# Formats dictonaries with scraped data accordingly with Pandas
#present_posts_data = pd.DataFrame(savedpostsdict)

# Ports each dictionary to a .csv file and numbers them in order. .csv files should be in the same folder as this main.py script
#present_posts_data.to_csv('savedredditposts.csv', index=True)
