#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Build-in / Std
import os, sys, time, platform, random
import re, json
from cookielib import LWPCookieJar
#import multiprocessing, multithreading

# requirements
import requests, termcolor
from bs4 import BeautifulSoup
# html2text

requests = requests.Session()
requests.cookies = LWPCookieJar('cookiejar')

"""
    Cookies: 
        https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file

    Code:
        import os
        from cookielib import LWPCookieJar

        import requests

        s = requests.Session()
        s.cookies = LWPCookieJar('cookiejar')
        if not os.path.exists('cookiejar'):
            # Create a new cookies file and set our Session's cookies
            print('setting cookies')
            s.cookies.save()
            r = s.get('http://httpbin.org/cookies/set?k1=v1&k2=v2')
        else:
            # Load saved cookies from the file and use them in a request
            print('loading saved cookies')
            s.cookies.load(ignore_discard=True)
            r = s.get('http://httpbin.org/cookies')
        print(r.text)
        # Save the session's cookies back to the file
        s.cookies.save(ignore_discard=True)

"""

"""
    termcolor : https://pypi.python.org/pypi/termcolor

        Text colors:
            grey, red, green, yellow, blue, magenta, cyan, white

        Text highlights:
            on_grey, on_red, on_green, on_yellow
            on_blue, on_magenta, on_cyan, on_white

        Attributes:
            bold, dark, underline, blink, reverse, concealed

        Example:
            import sys
            from termcolor import colored, cprint

            text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
            print(text)
            cprint('Hello, World!', 'green', 'on_red')

            print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
            print_red_on_cyan('Hello, World!')
            print_red_on_cyan('Hello, Universe!')

            for i in range(10):
                cprint(i, 'magenta', end=' ')

            cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
"""

class Logging:
    flag = True

    @staticmethod
    def error(msg):
        if Logging.flag == True:
            print "".join(  [ termcolor.colored("ERROR", "red"), ": ", termcolor.colored(msg, "white") ] )
    @staticmethod
    def warn(msg):
        if Logging.flag == True:
            print "".join(  [ termcolor.colored("WARN", "yellow"), ": ", termcolor.colored(msg, "white") ] )
    @staticmethod
    def info(msg):
        # attrs=['reverse', 'blink']
        if Logging.flag == True:
            print "".join(  [ termcolor.colored("INFO", "magenta"), ": ", termcolor.colored(msg, "white") ] )
    @staticmethod
    def debug(msg):
        if Logging.flag == True:
            print "".join(  [ termcolor.colored("DEBUG", "magenta"), ": ", termcolor.colored(msg, "white") ] )
    @staticmethod
    def success(msg):
        if Logging.flag == True:
            print "".join(  [ termcolor.colored("SUCCES", "green"), ": ", termcolor.colored(msg, "white") ] )

# Setting Logging
Logging.flag = True

class LoginPasswordError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"帐号密码错误"
        else: self.message = message
        Logging.error(self.message)

class NetworkError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"网络异常"
        else: self.message = message
        Logging.error(self.message)
class AccountError(Exception):
    def __init__(self, message):
        if type(message) != type("") or message == "": self.message = u"帐号类型错误"
        else: self.message = message
        Logging.error(self.message)

"""


"""
class Auth:
    cookies = {}

    password = None
    email = None
    phone = None

    def __init__(self, account=None, password=None):
        if re.match(r"^\d{11}$", account): self.phone = account
        elif re.match(r"^\S+\@\S+\.\S+$", account): self.email = account
        else: raise AccountError(u"帐号类型错误1")
        self.password = password

    def check_cookie(self):
        url = "http://www.zhihu.com/settings/profile"

        requests.cookies.load(ignore_discard=True)

        r = requests.get(url, allow_redirects=False)
        status_code = int(r.status_code)
        if status_code == 301 or status_code == 302:
            # 未登录
            return False
        elif status_code == 200:
            return True
        else:
            raise NetworkError(u"网络故障")

    def signin(self):
        islogin = self.check_cookie()
        if islogin == True:
            return open("cookiejar", "r").read()

        form_data = self.build_form()
        """
            result: 
                {"result": True}
                {"error": {"code": 19855555, "message": "unknow.", "data": "data" } }
                {"error": {"code": -1, "message": u"unknow error"} }
        """
        result = self.upload_form(form_data)
        if "error" in result:
            if result["error"]['code'] == 1991829:
                # 验证码错误
                Logging.error(u"验证码输入错误，请准备重新输入。" )
                return self.signin()
            else:
                Logging.warn(u"unknow error." )
        elif "result" in result and result['result'] == True:
            # 登录成功
            requests.cookies.save()
            return self.cookies

    def build_form(self):
        form = {"password": self.password, "remember_me": True }
        if self.email != None:
            form['email'] = self.email
        elif self.phone != None:
            # DEBUG: 未验证 表单数据是否为 `phone`
            Logging.warn(u"手机登录尚未测试!!!" )
            form['phone'] = self.phone
        else:
            raise AccountError(u"帐号类型错误")

        form['_xsrf'] = self.search_xsrf()
        form['captcha'] = self.download_captcha()
        return form

    def upload_form(self, form):

        url = "http://www.zhihu.com/login/email"
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
            'Host': "www.zhihu.com",
            'Origin': "http://www.zhihu.com",
            'Pragma': "no-cache",
            'Referer': "http://www.zhihu.com/",
            'X-Requested-With': "XMLHttpRequest"
        }
        # Login 
        r = requests.post(url, data=form, headers=headers)

        if int(r.status_code) == 200 and r.headers['content-type'].lower() == "application/json":
            result = r.json()
            if result["r"] == 0:
                # Login Success.
                Logging.success(u"登录成功！" )
                # Save Cookies.
                for key in dict(r.cookies):
                    self.cookies[key] = dict(r.cookies)[key]
                return {"result": True}
            elif result["r"] == 1:
                # error
                return {"error": {"code": int(result['errcode']), "message": result['msg'], "data": result['data'] } }
            else:
                # unknow error.
                Logging.warn(u"表单上传出现未知错误: \n \t %s )" % ( str(result) ) )
                return {"error": {"code": -1, "message": u"unknow error"} }

    def search_xsrf(self):
        url = "http://www.zhihu.com/"
        r = requests.get(url)
        if int(r.status_code) != 200:
            raise NetworkError(u"验证码请求失败")

        # Save Cookies.
        for key in dict(r.cookies):
            self.cookies[key] = dict(r.cookies)[key]

        results = re.compile(r"\<input\stype=\"hidden\"\sname=\"_xsrf\"\svalue=\"(\S+)\"", re.DOTALL).findall(r.text)
        if len(results) < 1:
            Logging.info(u"提取XSRF 代码失败" )
            return None
        return results[0]
    
    def download_captcha(self):
        url = "http://www.zhihu.com/captcha.gif"
        r = requests.get(url, params={"r": random.random()} )
        if int(r.status_code) != 200:
            raise NetworkError(u"验证码请求失败")
        # Save Cookies.
        for key in dict(r.cookies):
            print "Recvie Cookie: ", key, "=", dict(r.cookies)[key]
            self.cookies[key] = dict(r.cookies)[key]

        image_name = u"verify." + r.headers['content-type'].split("/")[1]
        open( image_name, "wb").write(r.content)
        """
            System platform: https://docs.python.org/2/library/platform.html
        """
        if platform.system() == "Linux":
            os.system("see %s &" % image_name )
        elif platform.system() == "Darwin":
            os.system("open %s &" % image_name )
        elif platform.system() == "SunOS":
            os.system("open %s &" % image_name )
        elif platform.system() == "FreeBSD":
            os.system("open %s &" % image_name )
        elif platform.system() == "Unix":
            os.system("open %s &" % image_name )
        elif platform.system() == "OpenBSD":
            os.system("open %s &" % image_name )
        elif platform.system() == "NetBSD":
            os.system("open %s &" % image_name )
        elif platform.system() == "Windows":
            os.system("open %s &" % image_name )
        else:
            Logging.info(u"我们无法探测你的作业系统，请自行打开验证码 %s 文件，并输入验证码。" % os.path.join(os.getcwd(), image_name) )
        #Logging.info(u"我们无法探测你的作业系统，请自行打开验证码 %s 文件，并输入验证码。" % os.path.join(os.getcwd(), image_name) )
        captcha_code = raw_input( termcolor.colored("请输入验证码: ", "cyan") )
        return captcha_code

    def logout(self):
        os.system("rm cookiejar")

def test_auth_with_email():
    account = ""
    password = ""
    auth = Auth(account=account, password=password)
    cookies = auth.signin()
    print open("cookiejar", "r").read()

def test_auth_with_phone():
    pass

def test_auth_with_cookiejar():
    pass



if __name__ == "__main__":
    test_auth_with_email()
