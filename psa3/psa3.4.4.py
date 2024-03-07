from datetime import datetime
import matplotlib.pyplot as plt
import json
import nltk


our_word = input('Input your word: ')
stop_list = ['https', '..', '@', '!', ',', '.', '?', '%', 'http', ':']
dates = []
times = []

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
        if word.lower() == our_word:
            try:
                date = datetime.strptime(str(tweet['created_at']),'%Y-%m-%d %H:%M:%S +0000').strftime('%m.%Y')
            except:
                pass
            if date not in dates:
                dates.append(date)
            fdist[date]+=1
for date in dates:
    times.append(fdist[date])

plt.style.use('ggplot')

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

x_pos = [i for i, _ in enumerate(dates)]

plt.bar(x_pos, times, color='red')
plt.xlabel("Month")
plt.ylabel("Times")
plt.title(f'Frequency of word {our_word}')

plt.xticks(x_pos, dates)

plt.show()
