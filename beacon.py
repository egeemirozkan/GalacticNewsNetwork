import twitter
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Beacon:
    def take_passwords(string_):
        file_ = open(string_, "r")
        passes = file_.read().split("\n")
        file_.close()
        return passes


    def twittfy(string_):
        continue_ = True
        strings = []
        while continue_ == True:
            first_string = string_[:130]
            strings.append(first_string)
            string_ = string_[130:]
            if string_ == '':
                continue_ = False
        return strings, len(strings)
    def post_tweet(News, CharLimit, PasswordFile, tr= False, day_ = "", month_ = "", year_ = ""):
        passwords = Beacon.take_passwords(PasswordFile)
        connection = twitter.Api(consumer_key=passwords[0],
                          consumer_secret=passwords[1],
                          access_token_key=passwords[2],
                          access_token_secret=passwords[3],
                          sleep_on_rate_limit=True)
        continue_ = False
        t = 0
        while continue_ == True:
            for i in range(len(News)):
                    if len(News[i]) <= CharLimit:
                        try:
                            connection.PostUpdate(News[i])
                            t += 1
                        except:
                            pass
                    else:
                        try:
                            newProgress, countMessage = Beacon.twittfy(News[i])
                            for j in range(countMessage):
                                connection.PostUpdate(newProgress[-(j+1)] + " [{}/{}]".format(
                                                    str(countMessage - j), str(countMessage)))
                        except:
                            pass
                    if t == 10:
                        continue_ = False
            if tr:
                connection.PostUpdate("Haberler, tarih: {}.{}.{}".format(day_, month_, year_))

    def fetch_tweet():
        page_ = urlopen("https://twitter.com/gnn_alphacenta")
        pageData_ = page_.read()
        page = BeautifulSoup(pageData_, "html.parser")
        new = page.find("div", class_ = "js-tweet-text-container").get_text()
        return new

# egeemirozkan.com | Ege Emir Özkan
