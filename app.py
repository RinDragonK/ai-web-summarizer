from fetch import fetch_article
from summarize import summarize

url = input("请输入网址：")

article = fetch_article(url)

print()

print(article[:1000])

print()

summary = summarize(article)

print(summary)