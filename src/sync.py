#!/usr/bin/env python
#-*- coding:utf-8 -*-

import thread
from threading import Thread
# Build-in / Std
import os, sys, time, platform, random
import re, json
from cookielib import LWPCookieJar
#import multiprocessing, multithreading
from Queue import Queue
# requirements
import requests, termcolor

try:
    from bs4 import BeautifulSoup
except:
    import BeautifulSoup

requests = requests.Session()
requests.cookies = LWPCookieJar('cookiejar')
requests.cookies.load(ignore_discard=True)

q = Queue()

def fetch( question_token ):
    url = "http://www.zhihu.com/question/" + str(question_token)
    try:
        r = requests.get(url, allow_redirects=False)
    except:
        time.sleep(2)
        print u"WARN: 网络异常 -> %s" %(url)
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



def worker():
    while not q.empty():
        item = q.get()
        fetch(item)
        q.task_done()


for i in range(4):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for token in range(1000):
    q.put(token)

q.join()       # block until all tasks are done

print "INFO: Done."


