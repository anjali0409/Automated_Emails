#Api key: 776339b8ec7c41d98d6b6f062a999ee4
import requests
from pprint import pprint
class NewsFeed:
    def __init__(self, data):
        self.data = data

    def get(self):
        pass

url = "http://newsapi.org/v2/everything?" \
      "qInTitle=meditation&"\
      "from=2021-03-11&"\
      "to=2021-03-12&"\
      "language=en&"\
      "apiKey=776339b8ec7c41d98d6b6f062a999ee4"
response =  requests.get(url)
content = response.json()
articles = content['articles']

email_body = ''
for article in articles:
    email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

print(email_body)