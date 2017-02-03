from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import twitter


def take_passwords():
    file_ = open("passwords.txt", "r")
    passes = file_.read().split("\n")
    file_.close()
    return passes


def page_creator():
    today = datetime.datetime.today()
    fouryears = datetime.timedelta(days=1460)
    centruziedTime = today - fouryears
    year = centruziedTime.year
    month = centruziedTime.month
    day = centruziedTime.day
    monthcreator = {
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
    }
    month_str = monthcreator[month]
    link = "https://en.wikipedia.org/wiki/Portal:Current_events/{}_{}".format(
            month_str, year)
    return day, month_str, year, link


def parseNews(huntFor, newslist):
    for i in range(len(huntFor)):
        continue_ = True
        while continue_ == True:
            try:
                newslist.remove(huntFor[i])
            except ValueError:
                continue_ = False
                pass
    return newslist

day_, month_, year_, pagelink = page_creator()
page_ = urlopen(pagelink)
pageData_ = page_.read()
page = BeautifulSoup(pageData_, "html.parser")
news_ = page.find(id="{}_{}_{}".format(year_, month_, day_)).findNext('table').get_text()
news = news_.split('\n')
continue_ = True
newsFinal = parseNews(["Armed conflicts and attacks", "", " ",
                       "Arts and culture", "Disasters and accidents",
                       "International relations", "Law and crime",
                       "Politics and elections", "Sport",
                       "Science and technology", "Business and economy",
                       "Health and environment", "wiev", "view", "history",
                       "edit", "Religion"], news)
passwords = take_passwords()
connection = twitter.Api(consumer_key=passwords[0],
                  consumer_secret=passwords[1],
                  access_token_key=passwords[2],
                  access_token_secret=passwords[3],
                  sleep_on_rate_limit=True)
connection.PostUpdate('News from Earth: {} {}, {}'.format(month_, day_, year_))
for i in range(len(newsFinal)):
    if len(newsFinal[i]) <= 140:
        connection.PostUpdate(newsFinal[i])
print("Transmission completed...")
