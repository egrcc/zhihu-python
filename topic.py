# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

class Topic:

    name = None

    def __init__(self, url = None):

        self.url = url
        
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
        email = cf.get("info", "email")
        password = cf.get("info", "password")
        s = requests.session()
        login_data = {"email": email, "password": password}
        s.post('http://www.zhihu.com/login', login_data)
        self.session = s

        r = s.get(url)
        soup = BeautifulSoup(r.content)
        self.soup = soup
        self.name = soup.find("div", id = "zh-topic-title").h1.string.encode("utf-8")

    def get_follower_num(self):
        soup = self.soup
        follower_num = int(soup.find("div", class_ = "zm-topic-side-followers-info") \
                .a.strong.string.encode("utf-8"))
        return follower_num


def main():
    url = "http://www.zhihu.com/topic/19612637"
    topic = Topic(url)
    print topic.name
    follower_num = topic.get_follower_num()
    print follower_num

if __name__ == "__main__":
    main()