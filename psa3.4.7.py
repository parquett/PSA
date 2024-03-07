import json
import nltk


stop_list = ['https', '..', '@', '!', ',', '.', '?', '%', 'http', ':', '``', '(', ')']
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
    for i in range(0, len(words)-1):
        if words[i].lower() == my_word.lower() and words[i+1] not in stop_list:
            next_word = words[i+1]
            fdist[next_word.lower()]+=1

top_3 = fdist.most_common(3)
print(top_3)