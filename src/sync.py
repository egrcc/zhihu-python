#!/usr/bin/env python
#-*- coding:utf-8 -*-

import thread
# Build-in / Std
import os, sys, time, platform, random
import re, json
from cookielib import LWPCookieJar
#import multiprocessing, multithreading

# requirements
import requests, termcolor

try:
    from bs4 import BeautifulSoup
except:
    import BeautifulSoup

requests = requests.Session()
requests.cookies = LWPCookieJar('cookiejar')
requests.cookies.load(ignore_discard=True)

def fetch( question_token ):
    url = "http://www.zhihu.com/question/" + str(question_token)
    try:
        r = requests.get(url, allow_redirects=False)
    except:
        time.sleep(2)
        print u"WARN: 网络异常 !"
        return fetch(question_token)

    status_code = int(r.status_code)
    if status_code == 200:
        # 无效的 问题 token
        print "SUCCESS: %s" % url
        open("data/"+question_token+".html", "w").write(r.text)
    elif status_code == 301 or status_code == 302:
        # unknow
        print "FAIL: %s" % url
        open("logs/"+str(status_code)+".log", "a").write(url+"\n")
    else:
        # network error.
        print "ERROR: %s" % url 
        open("logs/"+str(status_code)+".log", "a").write(url+"\n")
    time.sleep(1)

# Create two threads as follows
try:
    for token in range(0, 1000, 4):
        thread.start_new_thread( fetch, (token, ) )
        thread.start_new_thread( fetch, (token+1, ) )
        thread.start_new_thread( fetch, (token+2, ) )
        thread.start_new_thread( fetch, (token+3, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass


