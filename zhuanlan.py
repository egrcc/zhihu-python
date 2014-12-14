import requests
from bs4 import BeautifulSoup

class Zhuanlan:

    url = None
    title = None

    def __init__(self, url):
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
        print soup
        self.title = soup.find("div", class_ = "navbar-content").span["title"]

def main():
    url = "http://zhuanlan.zhihu.com/GayScript"
    zhuanlan = Zhuanlan(url)
    print zhuanlan.title
    print type(zhuanlan.title)


if __name__ == "__main__":
    main()

        