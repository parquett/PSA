import json
import nltk

from nltk.tokenize import word_tokenize

stop_list = ['https', '..', '@', '!', ',', '.', '?', '%', 'http', ':', "''"]

Tweet = {
    'id',
    'text',
    'created_at',
    'likes',
    'retweets',
    'rating'
}

tweets: Tweet = []
fdist = nltk.FreqDist()
freqretw = nltk.FreqDist()
freqlikes = nltk.FreqDist()
word_rating = nltk.FreqDist()

with open(r"tweets.json", "r", encoding='utf-8') as file:
    json_list = json.loads(file.read())
    for tweet in json_list:
        tweet['rating'] = 0
        tweets.append(tweet)

for tweet in tweets:
    words = nltk.word_tokenize(tweet['text'])
    for word in words:
        total_tweets = 0
        total_likes = 0
        if word not in stop_list:
            fdist[word.lower()]+=1
            freqlikes[word.lower()] += tweet['likes']
            freqretw[word.lower()] += tweet['retweets']

for tweet in tweets:
    words = nltk.word_tokenize(tweet['text'])
    for word in words:
        if word not in stop_list:
            word_rating[word.lower()] = fdist[word.lower()] * (1.4 + freqretw[word.lower()]) * (1.2 + freqlikes[word.lower()])

top_10 = word_rating.most_common(10)
#print(top_10)

for i in range(0, 10):
    print(f'{i+1}) {top_10[i][0]}: {top_10[i][1]}')

