import yagmail
import pandas
from news import NewsFeed
import datetime
import time


while True:
    if datetime.datetime.now().hour == 12 and datetime.datetime.now().minute == 50:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%y-%m-%d'),
                                 to_date=datetime.datetime.now().strftime('%y-%m-%d'))
            email = yagmail.SMTP(user="********abc@gmail.com", password="9999999999")
            email.send(to=row['email'],
                       subject= f"your {row['interest']} news for today!",
                       contents=f"Hi {row['name']}\n, See whats's on about {row['interest']} today.\n {news_feed.get()}")

    time.sleep(60)
