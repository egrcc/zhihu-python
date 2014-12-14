# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import json
import os
import re
import html2text
import ConfigParser
# from copy import deepcopy, copy

class Question:

    url = None
    # title = None
    # detail = None
    # answer_num = None
    soup = None
    session = None

    def __init__(self, url, title = None):
        
        self.url = url
        if title != None:
            self.title = title

        # cf = ConfigParser.ConfigParser()
        # cf.read("config.ini")
        # email = cf.get("info", "email")
        # password = cf.get("info", "password")
        # s = requests.session()
        # login_data = {"email": email, "password": password}
        # s.post('http://www.zhihu.com/login', login_data)
        # self.session = s

        # r = s.get(url)
        # soup = BeautifulSoup(r.content)
        # self.soup = soup
        # self.title = soup.find("h2", class_ = "zm-item-title").string.encode("utf-8").replace("\n", "")
        # self.detail = str(soup.find("div", id = "zh-question-detail").div)
        # if soup.find("h3", id = "zh-question-answer-num") != None:
        #     self.answer_num = int(soup.find("h3", id = "zh-question-answer-num")["data-num"])
        # else:
        #     self.answer_num = 0
        # f = open("test.html", "wt")
        # f.write(r.content)
        # f.close()
        # print soup


    def create_session(self):
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
        email = cf.get("info", "email")
        password = cf.get("info", "password")
        s = requests.session()
        login_data = {"email": email, "password": password}
        s.post('http://www.zhihu.com/login', login_data)
        self.session = s

    def parser(self):
        if self.session == None:
            self.create_session()
        s = self.session
        r = s.get(self.url)
        soup = BeautifulSoup(r.content)
        self.soup = soup

    def get_title(self):
        if hasattr(self, "title"):
            return self.title
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            title = soup.find("h2", class_ = "zm-item-title").string.encode("utf-8").replace("\n", "")
            self.title = title
            return title

    def get_detail(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        detail = soup.find("div", id = "zh-question-detail").div.get_text().encode("utf-8")
        return detail

    def get_answer_num(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        answer_num = 0
        if soup.find("h3", id = "zh-question-answer-num") != None:
            answer_num = int(soup.find("h3", id = "zh-question-answer-num")["data-num"])
        return answer_num


    def get_follower_num(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        follower_num = int(soup.find("div", class_ = "zg-gray-normal").a.strong.string)
        return follower_num


    def get_topic(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        topic_list = soup.find_all("a", class_ = "zm-item-tag")
        topic = []
        for i in topic_list:
            topic.append(i.contents[0].encode("utf-8").replace("\n", ""))
        return topic

    def get_top_answer(self):
        # soup = deepcopy(self.soup)
        # start_time = time.time()
        if self.get_answer_num() == 0:
            print "No answer."
            return 
        else:
            if self.soup == None:
                self.parser()
            soup = BeautifulSoup(self.soup.encode("utf-8"))
            # end_time  = time.time()
            # print end_time - start_time
            # s = self.session
            # r = s.get(self.url)
            # soup = BeautifulSoup(r.content)
            author = None
            if soup.find("h3", class_ = "zm-item-answer-author-wrap") == u"匿名用户":
                # author_id = "匿名用户"
                author_url = None
                author = User(author_url)
            else:
                author_tag = soup.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                author_id = author_tag.string.encode("utf-8")
                author_url = "http://www.zhihu.com" + author_tag["href"]
                author = User(author_url, author_id)

            count = soup.find("span", class_ = "count").string
            if count[-1] == "K":
                upvote = int(count[0:(len(count) - 1)]) * 1000
            elif count[-1] == "W":
                upvote = int(count[0:(len(count) - 1)]) * 10000
            else:
                upvote = int(count)

            answer_url = "http://www.zhihu.com" + soup.find("a", class_ = "answer-date-link")["href"]

            top_answer = soup.find("div", class_ = " zm-editable-content clearfix")
            soup.body.extract()
            soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
            soup.body.append(top_answer)
            img_list = soup.find_all("img", class_ = "content_image lazy")
            for img in img_list:
                img["src"] = img["data-actualsrc"]
            # print type(img_list[0])
            # print soup.get_text().encode("utf-8").strip()
            # f = open("answer.html", "wt")
            # f.write(soup.get_text().encode("utf-8").strip())
            # f.close()
            # content = str(soup)
            content = soup
            answer = Answer(answer_url, self, author, upvote, content)
            return answer

    def get_all_answer(self):
        if self.get_answer_num() == 0:
            print "No answer."
            return
            yield
        else:
            answer_num = self.get_answer_num()
            for i in range((answer_num - 1) / 50 + 1):
                if i == 0:
                    for j in range(min(answer_num, 50)):
                        if self.soup == None:
                            self.parser()
                        soup = BeautifulSoup(self.soup.encode("utf-8"))

                        author = None
                        if soup.find_all("h3", class_ = "zm-item-answer-author-wrap")[j].string == u"匿名用户":
                            # author_id = "匿名用户"
                            author_url = None
                            author = User(author_url)
                        else:
                            author_tag = soup.find_all("h3", class_ = "zm-item-answer-author-wrap")[j].find_all("a")[1]
                            author_id = author_tag.string.encode("utf-8")
                            author_url = "http://www.zhihu.com" + author_tag["href"]
                            author = User(author_url, author_id)

                        count = soup.find_all("span", class_ = "count")[j].string
                        if count[-1] == "K":
                            upvote = int(count[0:(len(count) - 1)]) * 1000
                        elif count[-1] == "W":
                            upvote = int(count[0:(len(count) - 1)]) * 10000
                        else:
                            upvote = int(count)

                        answer_url = "http://www.zhihu.com" + soup.find_all("a", class_ = "answer-date-link")[j]["href"]

                        answer = soup.find_all("div", class_ = " zm-editable-content clearfix")[j]
                        soup.body.extract()
                        soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
                        soup.body.append(answer)
                        img_list = soup.find_all("img", class_ = "content_image lazy")
                        for img in img_list:
                            img["src"] = img["data-actualsrc"]
                        content = soup
                        answer = Answer(answer_url, self, author, upvote, content)
                        yield answer
                else:
                    s = self.session
                    post_url = "http://www.zhihu.com/node/QuestionAnswerListV2"
                    _xsrf = self.soup.find("input", attrs = {'name': '_xsrf'})["value"]
                    offset = i * 50
                    params = json.dumps({"url_token":int(self.url[-8:-1] + self.url[-1]), "pagesize":50, "offset": offset})
                    data = {
                        '_xsrf': _xsrf,
                        'method': "next",
                        'params': params
                    }
                    header = {
                        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
                        'Host': "www.zhihu.com",
                        'Referer': self.url
                    }
                    r = s.post(post_url, data = data, headers = header)
                    answer_list = r.json()["msg"]
                    for j in range(min(answer_num - i * 50, 50)):
                        soup = BeautifulSoup(self.soup.encode("utf-8"))

                        answer_soup = BeautifulSoup(answer_list[j])

                        author = None
                        if answer_soup.find("h3", class_ = "zm-item-answer-author-wrap").string == u"匿名用户":
                            # author_id = "匿名用户"
                            author_url = None
                            author = User(author_url)
                        else:
                            author_tag = answer_soup.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                            author_id = author_tag.string.encode("utf-8")
                            author_url = "http://www.zhihu.com" + author_tag["href"]
                            author = User(author_url, author_id)

                        count = answer_soup.find("span", class_ = "count").string
                        if count[-1] == "K":
                            upvote = int(count[0:(len(count) - 1)]) * 1000
                        elif count[-1] == "W":
                            upvote = int(count[0:(len(count) - 1)]) * 10000
                        else:
                            upvote = int(count)

                        answer_url = "http://www.zhihu.com" + answer_soup.find("a", class_ = "answer-date-link")["href"]

                        answer = answer_soup.find("div", class_ = " zm-editable-content clearfix")
                        soup.body.extract()
                        soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
                        soup.body.append(answer)
                        img_list = soup.find_all("img", class_ = "content_image lazy")
                        for img in img_list:
                            img["src"] = img["data-actualsrc"]
                        content = soup
                        answer = Answer(answer_url, self, author, upvote, content)
                        yield answer


class User:

    # user_id = None
    user_url = None
    # followee_num = None
    # follower_num = None
    # agree_num = None
    # thanks_num = None
    # ask_num = None
    # answer_num = None
    # collection_num = None
    session = None
    soup = None

    def __init__(self, user_url, user_id = None):
        if user_url == None:
            self.user_id = "匿名用户"
            # self.user_id = user_id
        else:
            self.user_url = user_url
            if user_id != None:
                self.user_id = user_id

            # self.create_session()
            # cf = ConfigParser.ConfigParser()
            # cf.read("config.ini")
            # email = cf.get("info", "email")
            # password = cf.get("info", "password")
            # s = requests.session()
            # login_data = {"email": email, "password": password}
            # s.post('http://www.zhihu.com/login', login_data)
            # self.session = s
            # self.parser()
            # soup = self.soup
            # r = s.get(user_url)
            # soup = BeautifulSoup(r.content)
            # self.soup = soup

            # if user_id == None:
            #     self.user_id = soup.find("div", class_ = "title-section ellipsis") \
            #         .find("span", class_ = "name").string.encode("utf-8")
            # else: 
            #     self.user_id = user_id
            # self.followee_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
            #         .find("a").strong.string)
            # self.follower_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
            #         .find_all("a")[1].strong.string)
            # self.agree_num = int(soup.find("span", class_ = "zm-profile-header-user-agree").strong.string)
            # self.thanks_num = int(soup.find("span", class_ = "zm-profile-header-user-thanks").strong.string)
            # self.ask_num = int(soup.find_all("span", class_ = "num")[0].string)
            # self.answer_num = int(soup.find_all("span", class_ = "num")[1].string)
            # self.collection_num = int(soup.find_all("span", class_ = "num")[3].string)


    def create_session(self):
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
        email = cf.get("info", "email")
        password = cf.get("info", "password")
        s = requests.session()
        login_data = {"email": email, "password": password}
        s.post('http://www.zhihu.com/login', login_data)
        self.session = s

    def parser(self):
        if self.session == None:
            self.create_session()
        s = self.session
        r = s.get(self.user_url)
        soup = BeautifulSoup(r.content)
        self.soup = soup


    def get_user_id(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return "匿名用户"
        else:
            if hasattr(self, "user_id"):
                return self.user_id
            else:
                if self.soup == None:
                    self.parser()
                soup = self.soup
                user_id = soup.find("div", class_ = "title-section ellipsis") \
                        .find("span", class_ = "name").string.encode("utf-8")
                self.user_id = user_id
                return user_id


    def get_followee_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            followee_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
                    .find("a").strong.string)
            return followee_num

    def get_follower_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            follower_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
                    .find_all("a")[1].strong.string)
            return follower_num

    def get_agree_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            agree_num = int(soup.find("span", class_ = "zm-profile-header-user-agree").strong.string)
            return agree_num

    def get_thanks_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            thanks_num = int(soup.find("span", class_ = "zm-profile-header-user-thanks").strong.string)
            return thanks_num

    def get_ask_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            ask_num = int(soup.find_all("span", class_ = "num")[0].string)
            return ask_num

    def get_answer_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            answer_num = int(soup.find_all("span", class_ = "num")[1].string)
            return answer_num

    def get_collection_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            collection_num = int(soup.find_all("span", class_ = "num")[3].string)
            return collection_num


    def get_followee(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            followee_num = self.get_followee_num()
            if followee_num == 0:
                return
                yield
            else:
                if self.session == None:
                    self.create_session()
                s = self.session
                followee_url = self.user_url + "/followees"
                r = s.get(followee_url)
                soup = BeautifulSoup(r.content)
                for i in range((followee_num - 1) / 20 + 1):
                    if i == 0:
                        user_url_list = soup.find_all("h2", class_ = "zm-list-content-title")
                        for j in range(min(followee_num, 20)):
                            yield User(user_url_list[j].a["href"], user_url_list[j].a.string.encode("utf-8"))
                    else:
                        post_url = "http://www.zhihu.com/node/ProfileFolloweesListV2"
                        _xsrf = soup.find("input", attrs = {'name': '_xsrf'})["value"]
                        offset = i * 20
                        hash_id = re.findall("hash_id&quot;: &quot;(.*)&quot;},", r.text)[0]
                        params = json.dumps({"offset": offset,"order_by":"created","hash_id": hash_id})
                        data = {
                            '_xsrf': _xsrf,
                            'method': "next",
                            'params': params
                        }
                        header = {
                            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
                            'Host': "www.zhihu.com",
                            'Referer': followee_url
                        }
                        r = s.post(post_url, data = data, headers = header)
                        followee_list = r.json()["msg"]
                        for j in range(min(followee_num - i * 20, 20)):
                            followee_soup = BeautifulSoup(followee_list[j])
                            user_link = followee_soup.find("h2", class_ = "zm-list-content-title").a
                            yield User(user_link["href"], user_link.string.encode("utf-8"))


    def get_follower(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            follower_num = self.get_follower_num()
            if follower_num == 0:
                return
                yield
            else:
                if self.session == None:
                    self.create_session()
                s = self.session
                follower_url = self.user_url + "/followers"
                r = s.get(follower_url)
                soup = BeautifulSoup(r.content)
                for i in range((follower_num - 1) / 20 + 1):
                    if i == 0:
                        user_url_list = soup.find_all("h2", class_ = "zm-list-content-title")
                        for j in range(min(follower_num, 20)):
                            yield User(user_url_list[j].a["href"], user_url_list[j].a.string.encode("utf-8"))
                    else:
                        post_url = "http://www.zhihu.com/node/ProfileFollowersListV2"
                        _xsrf = soup.find("input", attrs = {'name': '_xsrf'})["value"]
                        offset = i * 20
                        hash_id = re.findall("hash_id&quot;: &quot;(.*)&quot;},", r.text)[0]
                        params = json.dumps({"offset": offset,"order_by":"created","hash_id": hash_id})
                        data = {
                            '_xsrf': _xsrf,
                            'method': "next",
                            'params': params
                        }
                        header = {
                            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
                            'Host': "www.zhihu.com",
                            'Referer': follower_url
                        }
                        r = s.post(post_url, data = data, headers = header)
                        follower_list = r.json()["msg"]
                        for j in range(min(follower_num - i * 20, 20)):
                            follower_soup = BeautifulSoup(follower_list[j])
                            user_link = follower_soup.find("h2", class_ = "zm-list-content-title").a
                            yield User(user_link["href"], user_link.string.encode("utf-8"))


    def get_ask(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            ask_num = self.get_ask_num()
            if self.session == None:
                self.create_session()
            s = self.session
            if ask_num == 0:
                return
                yield
            else:  
                for i in range((ask_num - 1) / 20 + 1):
                    ask_url = self.user_url + "/asks?page=" + str(i + 1)
                    r = s.get(ask_url)
                    soup = BeautifulSoup(r.content)
                    for question in soup.find_all("a", class_ = "question_link"):
                        url = "http://www.zhihu.com" + question["href"]
                        title = question.string.encode("utf-8")
                        yield Question(url, title)                    


    def get_answer(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            answer_num = self.get_answer_num()
            if self.session == None:
                self.create_session()
            s = self.session
            if answer_num == 0:
                return
                yield
            else:
                for i in range((answer_num - 1) / 20 + 1):
                    answer_url = self.user_url + "/answers?page=" + str(i + 1)
                    r = s.get(answer_url)
                    soup = BeautifulSoup(r.content)
                    for answer in soup.find_all("a", class_ = "question_link"):
                        question_url = "http://www.zhihu.com" + answer["href"][0:18]
                        question_title = answer.string.encode("utf-8")
                        question = Question(question_url, question_title)
                        yield Answer("http://www.zhihu.com" + answer["href"], question, self)


    def get_collection(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            collection_num = self.get_collection_num()
            if self.session == None:
                self.create_session()
            s = self.session
            if collection_num == 0:
                return
                yield
            else:
                for i in range((collection_num - 1) / 20 + 1):
                    collection_url = self.user_url + "/collections?page=" + str(i + 1)
                    r = s.get(collection_url)
                    soup = BeautifulSoup(r.content)
                    for collection in soup.find_all("div", class_ = "zm-profile-section-item zg-clear"):
                        url = "http://www.zhihu.com" + \
                            collection.find("a", class_ = "zm-profile-fav-item-title")["href"]
                        name = collection.find("a", class_ = "zm-profile-fav-item-title").string.encode("utf-8")
                        yield Collection(url, name, self)


class Answer:

    answer_url = None
    session = None
    soup = None

    def __init__(self, answer_url, question = None, author = None, upvote = None, content = None):

        self.answer_url = answer_url
        if question != None:
            self.question = question
        if author != None:
            self.author = author
        if upvote != None:
            self.upvote = upvote
        if content != None:
            self.content = content
        # if content == None and answer_url == None:
        #     print "can't get answer."
        #     self.content = content
        # elif content == None:
            # cf = ConfigParser.ConfigParser()
            # cf.read("config.ini")
            # email = cf.get("info", "email")
            # password = cf.get("info", "password")
            # s = requests.session()
            # login_data = {"email": email, "password": password}
            # s.post('http://www.zhihu.com/login', login_data)
            # self.session = s
            # r = s.get(answer_url)
            # soup = BeautifulSoup(r.content)
            
            # self.question = Question(answer_url[0:38])
            # if soup.find("h3", class_ = "zm-item-answer-author-wrap").string == u"匿名用户":
            #     # author_id = "匿名用户"
            #     author_url = None
            #     self.author = User(author_url)
            # else:
            #     author_tag = soup.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
            #     author_id = author_tag.string.encode("utf-8")
            #     author_url = "http://www.zhihu.com" + author_tag["href"]
            #     self.author = User(author_url, author_id)
            # self.upvote = int(soup.find("span", class_ = "count").string.encode("utf-8"))

            # answer = soup.find("div", class_ = " zm-editable-content clearfix")
            # soup.body.extract()
            # soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
            # soup.body.append(answer)
            # img_list = soup.find_all("img", class_ = "content_image lazy")
            # for img in img_list:
            #     img["src"] = img["data-actualsrc"]
            # self.content = soup


    def create_session(self):
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
        email = cf.get("info", "email")
        password = cf.get("info", "password")
        s = requests.session()
        login_data = {"email": email, "password": password}
        s.post('http://www.zhihu.com/login', login_data)
        self.session = s

    def parser(self):
        if self.session == None:
            self.create_session()
        s = self.session
        r = s.get(self.answer_url)
        soup = BeautifulSoup(r.content)
        self.soup = soup

    def get_question(self):
        if hasattr(self, "question"):
            return self.question
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            question_link = soup.find("h2", class_ = "zm-item-title zm-editable-content").a
            url = "http://www.zhihu.com" + question_link["href"]
            title = question_link.string.encode("utf-8")
            question = Question(url, title)
            return question

    def get_author(self):
        if hasattr(self, "author"):
            return self.author
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            if soup.find("h3", class_ = "zm-item-answer-author-wrap").string == u"匿名用户":
                author_url = None
                author = User(author_url)
            else:
                author_tag = soup.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                author_id = author_tag.string.encode("utf-8")
                author_url = "http://www.zhihu.com" + author_tag["href"]
                author = User(author_url, author_id)
            return author

    def get_upvote(self):
        if hasattr(self, "upvote"):
            return self.upvote
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            count = soup.find("span", class_ = "count").string
            if count[-1] == "K":
                upvote = int(count[0:(len(count) - 1)]) * 1000
            elif count[-1] == "W":
                upvote = int(count[0:(len(count) - 1)]) * 10000
            else:
                upvote = int(count)
            return upvote

    def get_content(self):
        if hasattr(self, "content"):
            return self.content
        else:
            if self.soup == None:
                self.parser()
            soup = BeautifulSoup(self.soup.encode("utf-8"))
            answer = soup.find("div", class_ = " zm-editable-content clearfix")
            soup.body.extract()
            soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
            soup.body.append(answer)
            img_list = soup.find_all("img", class_ = "content_image lazy")
            for img in img_list:
                img["src"] = img["data-actualsrc"]
            content = soup
            self.content = content
            return content


    def to_txt(self):

        content = self.get_content()
        # content = BeautifulSoup(self.content.encode("utf-8"))
        # content = deepcopy(self.content)
        body =content.find("body")
        br_list = body.find_all("br")
        for br in br_list:
            br.insert_after(content.new_string("\n"))
        li_list = body.find_all("li")
        for li in li_list:
            li.insert_before(content.new_string("\n"))

        if self.get_author().get_user_id() == "匿名用户":
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "text"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "text")))
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.txt"
            if os.path.exists(os.path.join(os.path.join(os.getcwd(), "text"), file_name)):
                f = open(os.path.join(os.path.join(os.getcwd(), "text"), file_name), "a")
                f.write("\n\n")
            else:
                f = open(os.path.join(os.path.join(os.getcwd(), "text"), file_name), "a")
                f.write(self.get_question().get_title() + "\n\n")
        else:
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "text"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "text")))
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.txt"
            f = open(os.path.join(os.path.join(os.getcwd(), "text"), file_name), "wt")
            f.write(self.get_question().get_title() + "\n\n")
        f.write("作者: " + self.get_author().get_user_id() + "  赞同: " + str(self.get_upvote()) + "\n\n")
        f.write(body.get_text().encode("utf-8"))
        f.write("\n" + "原链接: " + self.answer_url)
        f.close()

    # def to_html(self):
    #     content = self.content
    #     if self.author.user_id == "匿名用户":
    #         f = open(self.question.get_title() + "-" + self.author.user_id + "的回答.html", "wt")
    #     else:
    #         f = open(self.question.get_title() + "-" + self.author.user_id + "的回答.html", "wt")
    #     f.write(str(content))
    #     f.close()

    def to_md(self):
        content = self.get_content()
        if self.get_author().get_user_id() == "匿名用户":
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.md"
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "markdown"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "markdown")))
            if os.path.exists(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name)):
                f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "a")
                f.write("\n")
            else:
                f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "a")
                f.write("# " + self.get_question().get_title() + "\n")
        else:
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "markdown"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "markdown")))
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.md"
            f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "wt")
            f.write("# " + self.get_question().get_title() + "\n")
        f.write("## 作者: " + self.get_author().get_user_id() + "  赞同: " + str(self.get_upvote()) + "\n")
        f.write(html2text.html2text(content.decode('utf-8')).encode("utf-8"))
        f.write("#### 原链接: " + self.answer_url)
        f.close()



class Collection:

    url = None
    session = None
    soup = None

    def __init__(self, url, name = None, creator = None):      
        self.url = url
        if name != None:
            self.name = name
        if creator != None:
            self.creator = creator

    def create_session(self):
        cf = ConfigParser.ConfigParser()
        cf.read("config.ini")
        email = cf.get("info", "email")
        password = cf.get("info", "password")
        s = requests.session()
        login_data = {"email": email, "password": password}
        s.post('http://www.zhihu.com/login', login_data)
        self.session = s

    def parser(self):
        if self.session == None:
            self.create_session()
        s = self.session
        r = s.get(self.url)
        soup = BeautifulSoup(r.content)
        self.soup = soup

    def get_name(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            self.name = soup.find("h2", id = "zh-fav-head-title").string.encode("utf-8").strip()
            return self.name

    def get_creator(self):
        if hasattr(self, 'creator'):
            return self.creator
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            creator_id = soup.find("h2", class_ = "zm-list-content-title").a.string.encode("utf-8")
            creator_url = "http://www.zhihu.com" + soup.find("h2", class_ = "zm-list-content-title").a["href"]
            creator = User(creator_url, creator_id)
            self.creator = creator
            return creator

    def get_all_answer(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        answer_list = soup.find_all("div", class_ = "zm-item")
        if len(answer_list) == 0:
            print "the collection is empty."
            return
            yield
        else:
            question_url = None
            question_title = None
            for answer in answer_list:
                question_link = answer.find("h2")
                if question_link != None:
                    question_url = "http://www.zhihu.com" + question_link.a["href"]
                    question_title = question_link.a.string.encode("utf-8")
                question = Question(question_url, question_title)
                answer_url = "http://www.zhihu.com" + answer.find("span", class_ = "answer-date-link-wrap").a["href"]
                author = None
                if answer.find("h3", class_ = "zm-item-answer-author-wrap") == u"匿名用户":
                    # author_id = "匿名用户"
                    author_url = None
                    author = User(author_url)
                else:
                    author_tag = answer.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                    author_id = author_tag.string.encode("utf-8")
                    author_url = "http://www.zhihu.com" + author_tag["href"]
                    author = User(author_url, author_id)
                yield Answer(answer_url, question, author)
            i = 2
            s = self.session
            while True:
                r = s.get(self.url + "?page=" + str(i))
                answer_soup = BeautifulSoup(r.content)
                answer_list = answer_soup.find_all("div", class_ = "zm-item")
                if len(answer_list) == 0:
                    break
                else:
                    for answer in answer_list:
                        question_link = answer.find("h2")
                        if question_link != None:
                            question_url = "http://www.zhihu.com" + question_link.a["href"]
                            question_title = question_link.a.string.encode("utf-8")
                        question = Question(question_url, question_title)
                        answer_url = "http://www.zhihu.com" + answer.find("span", class_ = "answer-date-link-wrap").a["href"]
                        author = None
                        if answer.find("h3", class_ = "zm-item-answer-author-wrap") == u"匿名用户":
                            # author_id = "匿名用户"
                            author_url = None
                            author = User(author_url)
                        else:
                            author_tag = answer.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                            author_id = author_tag.string.encode("utf-8")
                            author_url = "http://www.zhihu.com" + author_tag["href"]
                            author = User(author_url, author_id)
                        yield Answer(answer_url, question, author)
                i = i + 1




def main():
    url = "http://www.zhihu.com/question/24580896"
    # question = Question(url)
    # question.get_all_answer()
    # print question.get_title()
    # print question.get_detail()
    # print question.get_answer_num()
    # print question.get_follower_num()
    # for topic in question.get_topic():
    #     print topic
    # answer = question.get_top_answer()
    # i = 0
    # for answer in answers:
    #     i = i + 1
    #     if i > 5:
    #         break
    #     answer.to_txt()
    #     print answer.author.user_id + "'s answer...."


    # user_url = "http://www.zhihu.com/people/Metaphox"
    # user = User(user_url)
    # print user.get_follower_num()
    # print user.get_followee_num()
    # print user.get_collection_num()
    # print user.get_ask_num()
    # print user.get_answer_num()
    # print user.get_agree_num()
    # print user.get_thanks_num()
    # print user.get_user_id()
    # followees = user.get_followee()

    # i = 0
    # for follower in followees:
    #     i = i + 1
    #     if i > 5:
    #         break
    #     print follower.user_id
    #     print follower.user_url

    collection_url = "http://www.zhihu.com/collection/19619098"
    collection = Collection(collection_url)
    print collection.get_name()
    print collection.get_creator().get_user_id()
    answers = collection.get_all_answer()
    i = 0
    for answer in answers:
        i = i + 1
        if i > 5:
            break
        print answer.get_question().get_title()
        print answer.get_upvote()
        answer.to_md()

if __name__ == '__main__':
    main()

