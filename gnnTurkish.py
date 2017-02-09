from beacon import Beacon
from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import twitter


def page_creator():
    today = datetime.datetime.today()
    fouryears = datetime.timedelta(days=1554)
    centruziedTime = today - fouryears
    year = centruziedTime.year
    month = centruziedTime.month
    day = centruziedTime.day
    monthpass = month
    daypass = day
    if day < 10:
        daypass = str("0"+str(day))
    if month < 10:
        monthpass = str("0"+str(month))
    monthcreator = {
    1:"Ocak",
    2:"Şubat",
    3:"Mart",
    4:"Nisan",
    5:"Mayıs",
    6:"Haziran",
    7:"Temmuz",
    8:"Ağustos",
    9:"Eylül",
    10:"Ekim",
    11:"Kasım",
    12:"Aralık"
    }
    month_str = monthcreator[month]
    link = "http://www.hurriyet.com.tr/index/?&cal=open&d={}{}{}".format(
            year, monthpass, daypass)
    return day, month, year, link, daypass, monthpass


def parseNews(huntFor, newslist):
    parsedNews = []
    for i in range(len(newslist)):
        new_temp = newslist[i]
        for j in range(len(huntFor)):
            new_temp = new_temp.replace(huntFor[j], "")
        parsedNews.append(new_temp)
    return parsedNews

day_, month_, year_, pagelink, dayreal, monthreal = page_creator()
page_ = urlopen(pagelink)
pageData_ = page_.read()
page = BeautifulSoup(pageData_, "html.parser")
news_ = page.find("div", class_="news-section").findChildren('div', class_ = "news")
news = []
for i in range(len(news_)):
    news.append(news_[i].get_text())


continue_ = True
newsFinal = parseNews(["Gündem", "Ekonomi", "Hürriyet Arşiv", "Ankara", "Ege",
                       "{}.{}.{}".format(day_, month_, year_)], news)
turn = 0
Beacon.post_tweet(newsFinal, 130, 'passwords.config', True, day_, month_, year_)
turn += 1
print("Transmission completed...")
