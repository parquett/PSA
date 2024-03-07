import json
import nltk
#nltk.download('punkt')

stop_list = ['https', '..', '@', '!', ',', '.', '?', '%', 'http', ':']

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

with open(r"tweets.json", "r", encoding='utf-8') as file:
    json_list = json.loads(file.read())
    for tweet in json_list:
        tweet['rating'] = 0
        tweets.append(tweet)

for tweet in tweets:
    words = nltk.word_tokenize(tweet['text'])
    for word in words:
        if word not in stop_list:
            fdist[word.lower()]+=1

top_10 = fdist.most_common(10)
print(top_10)



