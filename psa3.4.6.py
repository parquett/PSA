import json
import nltk


stop_list = ['https', '..', '@', '!', ',', '.', '?', '%', 'http', ':']
my_word = input('Input your word: ')

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
        if word not in stop_list and my_word == word.lower()[:len(my_word)]:
            fdist[word.lower()]+=1

top_3 = fdist.most_common(3)
print(top_3)