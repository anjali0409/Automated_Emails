#Api key: 776339b8ec7c41d98d6b6f062a999ee4
import requests
from pprint import pprint

class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "http://newsapi.org/v2/everything?"
    api_key = "776339b8ec7c41d98d6b6f062a999ee4"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&"\
              f"from={self.from_date}&"\
              f"to={self.to_date}&"\
              f"language={self.language}&"\
              f"apiKey={self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

news_feed = NewsFeed(interest='nasa', from_date='2021-03-11', to_date='2021-03-12', language='en')
print(news_feed.get())