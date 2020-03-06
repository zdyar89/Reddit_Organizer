# Will be using praw modules. And pandas to format the scraped data to port to .csv file
import praw
import pandas as pd
import csv
from sqlalchemy import create_engine
import psycopg2
import sys
import io

# Ask for user authentication first
usernamed = 'zakapalooza' #input("What's your username? ")
passwrd = 'Sam!102589' #input("What's your password? ")

# PostGreSQL DB Connection
connection = psycopg2.connet(database='redditSortDB', 
                            user='postgres', 
                            passwrd='searcy')

cur = connection.cursor()
cur.execute('SELECT version()')
version = cur.fetchone()[0]
print(version)

# User will need to create an app in reddit and put in the id and secret tokens to use this
reddit = praw.Reddit(client_id='uNyVpBjMbWzxIQ', \
                    client_secret='DiRSAS3ZJ0gfDNYKZmp4-iwRVxE', \
                    user_agent='redditScraper', \
                    username=usernamed, \
                    password=passwrd)

# Created two dictionaries to store the saved content. One for posts and one for comments since they can't mingle
#savedpostsdict = {"subreddit": [], \"saved content url":[], \"saved content title":[] }

savedpostsdict = {"placeholder" : []} 
# Scrapes all of the user's own content
savedcontent = reddit.user.me().saved(limit=None)

# Checks each saved content to see if it is a comment or submitted post instance and appends to respective dictionaries
for submission in savedcontent:
    
    if isinstance(submission, praw.models.Submission):
        sub = str(submission.subreddit)
        title = str(submission.title) + ' : ' + str(submission.url)
        if sub not in savedpostsdict:
            savedpostsdict.update({str(sub) : [title]})
        else:    
            savedpostsdict[sub].append(' ' + title)
            

df = pd.DataFrame.from_dict(savedpostsdict,orient='index').transpose()    
df.to_csv(r'./dataframe.csv')
#for item in sorted(savedpostsdict):
    
    #print(item, ' : ' , savedpostsdict[item] , '\n')



