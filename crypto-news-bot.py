import requests
import time
import os
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
NEWS_TOKEN = os.getenv('NEWS_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def publish_to_telegram(news_title, news_source, news_date):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendmessage"

    payload = {
        "text": "<strong>" + news_title + "🚀🌕</strong>" + '\n\n' + "Source: " + "<a href=" + news_source + " >" + news_source + "</a>" +
                '\n\n' + "Date: " + news_date,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": 0,
        "chat_id": CHAT_ID
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    requests.request("POST", url, json=payload, headers=headers)


def get_articles():
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={NEWS_TOKEN}"

    response = requests.get(url)

    return response.json()


previous_article = ""

while True:
    articles = get_articles()['results'][0]
    title = articles['title']
    source = articles['domain']
    date = articles['published_at']
    date = date.replace('T', ' ').replace('Z', ' ')

    if title != previous_article:
        previous_article = title
        print(title, source, date)

    time.sleep(60)
