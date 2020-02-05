# Will be using praw modules. And pandas to format the scraped data to port to .csv file
import praw
import pandas as pd
import csv

# Ask for user authentication first
usernamed = 'zakapalooza' #input("What's your username? ")
passwrd = 'Sam!102589' #input("What's your password? ")

# User will need to create an app in reddit and put in the id and secret tokens to use this
reddit = praw.Reddit(client_id='uNyVpBjMbWzxIQ', \
                    client_secret='DiRSAS3ZJ0gfDNYKZmp4-iwRVxE', \
                    user_agent='redditScraper', \
                    username=usernamed, \
                    password=passwrd)

# Created two dictionaries to store the saved content. One for posts and one for comments since they can't mingle
#savedpostsdict = {"subreddit": [], \"saved content url":[], \"saved content title":[] }

savedpostsdict = {}
# Scrapes all of the user's own content
savedcontent = reddit.user.me().saved(limit=None)

count = 0
# Checks each saved content to see if it is a comment or submitted post instance and appends to respective dictionaries
for submission in savedcontent:
    if isinstance(submission, praw.models.Submission):
            savedpostsdict.setdefault(str(submission.subreddit), [])
            savedpostsdict[str(submission.subreddit)].append(submission.url + " : ")
            count += 1
        


with open('mycsv.csv', 'w', newLine='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['col1', 'col2', 'col3'])
    thewriter.writerow(['one', 'two', 'three'])

##could use pickle module to store as binary stream for lists

# Formats dictonaries with scraped data accordingly with Pandas
#present_posts_data = pd.DataFrame(savedpostsdict)

# Ports each dictionary to a .csv file and numbers them in order. .csv files should be in the same folder as this main.py script
#present_posts_data.to_csv('savedredditposts.csv', index=True)
