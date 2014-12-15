# -*- coding: utf-8 -*-

import os
import re
import time
import json
import requests
import html2text
import ConfigParser
from bs4 import BeautifulSoup

session = None

def create_session():

    global session

    cf = ConfigParser.ConfigParser()
    cf.read("config.ini")
    email = cf.get("info", "email")
    password = cf.get("info", "password")
    s = requests.session()
    login_data = {"email": email, "password": password}
    s.post('http://www.zhihu.com/login', login_data)
    session = s


class Question:

    url = None
    soup = None
    # session = None


    def __init__(self, url, title = None):
        
        if url[0:len(url) - 8] != "http://www.zhihu.com/question/":
            raise ValueError("\"" + url + "\"" + " : it isn't a question url.")
        else:     
            self.url = url
            if title != None:
                self.title = title

    # def create_session(self):
    #     cf = ConfigParser.ConfigParser()
    #     cf.read("config.ini")
    #     email = cf.get("info", "email")
    #     password = cf.get("info", "password")
    #     s = requests.session()
    #     login_data = {"email": email, "password": password}
    #     s.post('http://www.zhihu.com/login', login_data)
    #     self.session = s

    def parser(self):

        global session

        if session == None:
            create_session()
        s = session
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

    def get_answers_num(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        answers_num = 0
        if soup.find("h3", id = "zh-question-answer-num") != None:
            answers_num = int(soup.find("h3", id = "zh-question-answer-num")["data-num"])
        return answers_num

    def get_followers_num(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        followers_num = int(soup.find("div", class_ = "zg-gray-normal").a.strong.string)
        return followers_num

    def get_topics(self):
        if self.soup == None:
            self.parser()
        soup = self.soup
        topic_list = soup.find_all("a", class_ = "zm-item-tag")
        topics = []
        for i in topic_list:
            topics.append(i.contents[0].encode("utf-8").replace("\n", ""))
        return topics

    # def get_top_answer(self):

    #     if self.get_answers_num() == 0:
    #         print "No answer."
    #         return 
    #     else:
    #         if self.soup == None:
    #             self.parser()
    #         soup = BeautifulSoup(self.soup.encode("utf-8"))
    #         author = None
    #         if soup.find("h3", class_ = "zm-item-answer-author-wrap") == u"匿名用户":
    #             author_url = None
    #             author = User(author_url)
    #         else:
    #             author_tag = soup.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
    #             author_id = author_tag.string.encode("utf-8")
    #             author_url = "http://www.zhihu.com" + author_tag["href"]
    #             author = User(author_url, author_id)

    #         count = soup.find("span", class_ = "count").string
    #         if count[-1] == "K":
    #             upvote = int(count[0:(len(count) - 1)]) * 1000
    #         elif count[-1] == "W":
    #             upvote = int(count[0:(len(count) - 1)]) * 10000
    #         else:
    #             upvote = int(count)

    #         answer_url = "http://www.zhihu.com" + soup.find("a", class_ = "answer-date-link")["href"]

    #         top_answer = soup.find("div", class_ = " zm-editable-content clearfix")
    #         soup.body.extract()
    #         soup.head.insert_after(soup.new_tag("body", **{'class':'zhi'}))
    #         soup.body.append(top_answer)
    #         img_list = soup.find_all("img", class_ = "content_image lazy")
    #         for img in img_list:
    #             img["src"] = img["data-actualsrc"]
    #         content = soup
    #         answer = Answer(answer_url, self, author, upvote, content)
    #         return answer

    def get_all_answers(self):

        global session

        if self.get_answers_num() == 0:
            print "No answer."
            return
            yield
        else:
            answers_num = self.get_answers_num()
            for i in range((answers_num - 1) / 50 + 1):
                if i == 0:
                    for j in range(min(answers_num, 50)):
                        if self.soup == None:
                            self.parser()
                        soup = BeautifulSoup(self.soup.encode("utf-8"))

                        author = None
                        if soup.find_all("h3", class_ = "zm-item-answer-author-wrap")[j].string == u"匿名用户":
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
                        img_list = soup.find_all("img", class_ = "origin_image zh-lightbox-thumb lazy")
                        for img in img_list:
                            img["src"] = img["data-actualsrc"]
                        noscript_list = soup.find_all("noscript")
                        for noscript in noscript_list:
                            noscript.extract()
                        content = soup
                        answer = Answer(answer_url, self, author, upvote, content)
                        yield answer
                else:
                    s = session
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
                    for j in range(min(answers_num - i * 50, 50)):
                        soup = BeautifulSoup(self.soup.encode("utf-8"))

                        answer_soup = BeautifulSoup(answer_list[j])

                        author = None
                        if answer_soup.find("h3", class_ = "zm-item-answer-author-wrap").string == u"匿名用户":
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
                        img_list = soup.find_all("img", class_ = "origin_image zh-lightbox-thumb lazy")
                        for img in img_list:
                            img["src"] = img["data-actualsrc"]
                        noscript_list = soup.find_all("noscript")
                        for noscript in noscript_list:
                            noscript.extract()
                        content = soup
                        answer = Answer(answer_url, self, author, upvote, content)
                        yield answer

    def get_top_i_answers(self, i):
        # if i > self.get_answers_num():
        #     i = self.get_answers_num()
        j = 0
        answers = self.get_all_answers()
        for answer in answers:
            j = j + 1
            if j > i:
                break
            yield answer

    def get_top_answer(self):
        for answer in self.get_top_i_answers(1):
            return answer


class User:

    user_url = None
    # session = None
    soup = None

    def __init__(self, user_url, user_id = None):
        if user_url == None:
            self.user_id = "匿名用户"
        elif user_url[0:28] != "http://www.zhihu.com/people/":
            raise ValueError("\"" + user_url + "\"" + " : it isn't a user url.")
        else:
            self.user_url = user_url
            if user_id != None:
                self.user_id = user_id

    # def create_session(self):
    #     cf = ConfigParser.ConfigParser()
    #     cf.read("config.ini")
    #     email = cf.get("info", "email")
    #     password = cf.get("info", "password")
    #     s = requests.session()
    #     login_data = {"email": email, "password": password}
    #     s.post('http://www.zhihu.com/login', login_data)
    #     self.session = s

    def parser(self):

        global session

        if session == None:
            create_session()
        s = session
        r = s.get(self.user_url)
        soup = BeautifulSoup(r.content)
        self.soup = soup

    def get_user_id(self):
        if self.user_url == None:
            # print "I'm anonymous user."
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

    def get_followees_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            followees_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
                    .find("a").strong.string)
            return followees_num

    def get_followers_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            followers_num = int(soup.find("div", class_ = "zm-profile-side-following zg-clear") \
                    .find_all("a")[1].strong.string)
            return followers_num

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

    def get_asks_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            asks_num = int(soup.find_all("span", class_ = "num")[0].string)
            return asks_num

    def get_answers_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            answers_num = int(soup.find_all("span", class_ = "num")[1].string)
            return answers_num

    def get_collections_num(self):
        if self.user_url == None:
            print "I'm anonymous user."
            return 0
        else:
            if self.soup == None:
                self.parser()
            soup = self.soup
            collections_num = int(soup.find_all("span", class_ = "num")[3].string)
            return collections_num

    def get_followees(self):

        global session

        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            followees_num = self.get_followees_num()
            if followees_num == 0:
                return
                yield
            else:
                if session == None:
                    create_session()
                s = session
                followee_url = self.user_url + "/followees"
                r = s.get(followee_url)
                soup = BeautifulSoup(r.content)
                for i in range((followees_num - 1) / 20 + 1):
                    if i == 0:
                        user_url_list = soup.find_all("h2", class_ = "zm-list-content-title")
                        for j in range(min(followees_num, 20)):
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
                        for j in range(min(followees_num - i * 20, 20)):
                            followee_soup = BeautifulSoup(followee_list[j])
                            user_link = followee_soup.find("h2", class_ = "zm-list-content-title").a
                            yield User(user_link["href"], user_link.string.encode("utf-8"))

    def get_followers(self):

        global session

        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            followers_num = self.get_followers_num()
            if followers_num == 0:
                return
                yield
            else:
                if session == None:
                    create_session()
                s = session
                follower_url = self.user_url + "/followers"
                r = s.get(follower_url)
                soup = BeautifulSoup(r.content)
                for i in range((followers_num - 1) / 20 + 1):
                    if i == 0:
                        user_url_list = soup.find_all("h2", class_ = "zm-list-content-title")
                        for j in range(min(followers_num, 20)):
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
                        for j in range(min(followers_num - i * 20, 20)):
                            follower_soup = BeautifulSoup(follower_list[j])
                            user_link = follower_soup.find("h2", class_ = "zm-list-content-title").a
                            yield User(user_link["href"], user_link.string.encode("utf-8"))

    def get_asks(self):

        global session

        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            asks_num = self.get_asks_num()
            if session == None:
                create_session()
            s = session
            if asks_num == 0:
                return
                yield
            else:  
                for i in range((asks_num - 1) / 20 + 1):
                    ask_url = self.user_url + "/asks?page=" + str(i + 1)
                    r = s.get(ask_url)
                    soup = BeautifulSoup(r.content)
                    for question in soup.find_all("a", class_ = "question_link"):
                        url = "http://www.zhihu.com" + question["href"]
                        title = question.string.encode("utf-8")
                        yield Question(url, title)                    

    def get_answers(self):

        global session

        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            answers_num = self.get_answers_num()
            if session == None:
                create_session()
            s = session
            if answers_num == 0:
                return
                yield
            else:
                for i in range((answers_num - 1) / 20 + 1):
                    answer_url = self.user_url + "/answers?page=" + str(i + 1)
                    r = s.get(answer_url)
                    soup = BeautifulSoup(r.content)
                    for answer in soup.find_all("a", class_ = "question_link"):
                        question_url = "http://www.zhihu.com" + answer["href"][0:18]
                        question_title = answer.string.encode("utf-8")
                        question = Question(question_url, question_title)
                        yield Answer("http://www.zhihu.com" + answer["href"], question, self)

    def get_collections(self):

        global session

        if self.user_url == None:
            print "I'm anonymous user."
            return
            yield
        else:
            collections_num = self.get_collections_num()
            if session == None:
                create_session()
            s = session
            if collections_num == 0:
                return
                yield
            else:
                for i in range((collections_num - 1) / 20 + 1):
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
    # session = None
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

    # def create_session(self):
    #     cf = ConfigParser.ConfigParser()
    #     cf.read("config.ini")
    #     email = cf.get("info", "email")
    #     password = cf.get("info", "password")
    #     s = requests.session()
    #     login_data = {"email": email, "password": password}
    #     s.post('http://www.zhihu.com/login', login_data)
    #     self.session = s

    def parser(self):

        global session

        if session == None:
            create_session()
        s = session
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
            img_list = soup.find_all("img", class_ = "origin_image zh-lightbox-thumb lazy")
            for img in img_list:
                img["src"] = img["data-actualsrc"]
            noscript_list = soup.find_all("noscript")
            for noscript in noscript_list:
                noscript.extract()
            content = soup
            self.content = content
            return content

    def to_txt(self):

        content = self.get_content()
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
            print file_name
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
            print file_name
            f = open(os.path.join(os.path.join(os.getcwd(), "text"), file_name), "wt")
            f.write(self.get_question().get_title() + "\n\n")
        f.write("作者: " + self.get_author().get_user_id() + "  赞同: " + str(self.get_upvote()) + "\n\n")
        f.write(body.get_text().encode("utf-8"))
        f.write("\n" + "原链接: " + self.answer_url)
        f.close()

    # def to_html(self):
    #     content = self.get_content()
    #     if self.get_author().get_user_id() == "匿名用户":
    #         file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.html"
    #         f = open(file_name, "wt")
    #         print file_name
    #     else:
    #         file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.html"
    #         f = open(file_name, "wt")
    #         print file_name
    #     f.write(str(content))
    #     f.close()

    def to_md(self):
        content = self.get_content()
        if self.get_author().get_user_id() == "匿名用户":
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.md"
            print file_name
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "markdown"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "markdown")))
            if os.path.exists(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name)):
                f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "a")
                # f_2 = open(os.path.join(os.path.join(os.getcwd(), "markdown"), "2_" + file_name), "a")
                f.write("\n")
                # f_2.write("\n")
            else:
                f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "a")
                # f_2 = open(os.path.join(os.path.join(os.getcwd(), "markdown"), "2_" + file_name), "a")
                f.write("# " + self.get_question().get_title() + "\n")
                # f_2.write("# " + self.get_question().get_title() + "\n")
        else:
            if not os.path.isdir(os.path.join(os.path.join(os.getcwd(), "markdown"))):
                os.makedirs(os.path.join(os.path.join(os.getcwd(), "markdown")))
            file_name = self.get_question().get_title() + "--" + self.get_author().get_user_id() + "的回答.md"
            print file_name
            f = open(os.path.join(os.path.join(os.getcwd(), "markdown"), file_name), "wt")
            # f_2 = open(os.path.join(os.path.join(os.getcwd(), "markdown"), "2_" + file_name), "wt")
            f.write("# " + self.get_question().get_title() + "\n")
            # f_2.write("# " + self.get_question().get_title() + "\n")
        f.write("## 作者: " + self.get_author().get_user_id() + "  赞同: " + str(self.get_upvote()) + "\n")
        # f_2.write("## 作者: " + self.get_author().get_user_id() + "  赞同: " + str(self.get_upvote()) + "\n")
        text = html2text.html2text(content.decode('utf-8')).encode("utf-8")

        r = re.findall(r'\*\*(.*?)\*\*', text)
        for i in r:
            if i != " ":
                text = text.replace(i, i.strip())

        r = re.findall(r'_(.*)_', text)
        for i in r:
            if i != " ":
                text = text.replace(i, i.strip())

        r =re.findall(r'!\[\]\((?:.*?)\)', text)
        for i in r:
            text = text.replace(i, i + "\n\n")

        f.write(text)
        # f_2.write(text)
        f.write("#### 原链接: " + self.answer_url)
        # f_2.write("#### 原链接: " + self.answer_url)
        f.close()
        # f_2.close()



class Collection:

    url = None
    # session = None
    soup = None

    def __init__(self, url, name = None, creator = None):

        if url[0:len(url) - 8] != "http://www.zhihu.com/collection/":
            raise ValueError("\"" + url + "\"" + " : it isn't a collection url.")
        else:
            self.url = url
            if name != None:
                self.name = name
            if creator != None:
                self.creator = creator

    # def create_session(self):
    #     cf = ConfigParser.ConfigParser()
    #     cf.read("config.ini")
    #     email = cf.get("info", "email")
    #     password = cf.get("info", "password")
    #     s = requests.session()
    #     login_data = {"email": email, "password": password}
    #     s.post('http://www.zhihu.com/login', login_data)
    #     self.session = s

    def parser(self):

        global session

        if session == None:
            create_session()
        s = session
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

    def get_all_answers(self):

        global session

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
                    author_url = None
                    author = User(author_url)
                else:
                    author_tag = answer.find("h3", class_ = "zm-item-answer-author-wrap").find_all("a")[1]
                    author_id = author_tag.string.encode("utf-8")
                    author_url = "http://www.zhihu.com" + author_tag["href"]
                    author = User(author_url, author_id)
                yield Answer(answer_url, question, author)
            i = 2
            s = session
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

    def get_top_i_answers(self, i):
        j = 0
        answers = self.get_all_answers()
        for answer in answers:
            j = j + 1
            if j > i:
                break
            yield answer
