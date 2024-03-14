import requests
from datetime import datetime, timedelta
import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = config.API_KEY
NEWS_API_KEY = config.NEWS_API_KEY

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"full",
    "apikey":API_KEY
}

response = requests.get(url = STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()
data = response.json()

def yesterday(frmt='%Y-%m-%d', string=True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday

def day_before_yesterday(frmt='%Y-%m-%d', string=True):
    day_b_yesterday = datetime.now() - timedelta(2)
    if string:
        return day_b_yesterday.strftime(frmt)
    return day_b_yesterday

def today(frmt='%Y-%m-%d', string=True):
    t = datetime.now()
    if string:
        return t.strftime(frmt)
    return t

ty = today()
y = yesterday()
dy = day_before_yesterday()

yes_cp = data["Time Series (Daily)"][y]["4. close"]
dbeyes_cp = data["Time Series (Daily)"][dy]["4. close"]

difference = abs(float(yes_cp) - float(dbeyes_cp))

diff_percentage = (difference / float(yes_cp)) * 100

print(diff_percentage)

if diff_percentage > 1:
    news_parameters ={
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    res = requests.get(url= NEWS_ENDPOINT, params=news_parameters)
    news_data = res.json()["articles"]
    three_artciles = news_data[:3]
    print(three_artciles)
