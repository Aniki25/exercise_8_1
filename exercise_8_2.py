import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('news.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item/description')

list_words = []
for article in news_list:
    article_split = article.text.lower().split()
    for word in range(len(article_split)):
        if len(article_split[word]) > 6:
            list_words.append(article_split[word])
print('топ-10 слов: ', Counter(list_words).most_common(10))

