import json
from collections import Counter

with open('news.json', encoding='utf-8') as f:
    json = json.load(f)

list_words = []
for article in json['rss']['channel']['items']:
    article_text = article['description']
    article_split = article_text.lower().split()
    for word in article_split:
        if len(word) > 6:
            list_words.append(word)
print('топ-10 слов: ', Counter(list_words).most_common(10))


