zhihu-python：获取知乎信息
===============================

介绍
----

zhihu-python 采用 python2.7 编写，用来方便地获取知乎上各种内容的信息，并且可以方便地将答案备份导出为 txt 或 markdown 文件。
由于知乎官方没有提供 api，所以有了此项目地存在。

依赖
-----

- 使用 `Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>`_ 解析 html 文档
- 使用 `requests <https://github.com/kennethreitz/requests>`_ 处理 http 请求
- 使用 `html2text <https://github.com/aaronsw/html2text>`_ 进行格式转换

没有的话可以使用 pip 安装：

.. code-block:: bash

    $ pip install requests
    $ pip install beautifulsoup4
    $ pip install html2text

**注意** ：如果同时安装了 python3 和 python2 ， pip 命令可能默认安装的是 python3 版本的包，故需将上述命令中的 pip 换成pip2 （比如在我的Ubuntu上）。

快速开始
---------

zhihu-python 主要文件为 zhihu.py ，配置文件为 config.ini , 将这两个文件下载到你的工作目录，并修改
config.ini 文件中的 email 为你的知乎账户邮箱，修改 password 为你的知乎账户密码。

 
Question：获取问题信息
~~~~~~~~~~~~~~~~~~~~~~~~

Question 代表一个问题，处理知乎问题相关操作。创建一个 Question 对象需传入该问题的 url ，如：

.. code-block:: python

    from zhihu import Question
    
    url = "http://www.zhihu.com/question/24269892"
    question = Question(url)

得到 Question 对象后，可以获取该问题的一些信息：

.. code-block:: python

    # -*- coding: utf-8 -*-
    from zhihu import Question
    
    url = "http://www.zhihu.com/question/24269892"
    question = Question(url)
    
    # 获取该问题的标题
    title = question.get_title()
    # 获取该问题的详细描述
    detail = question.get_detail()
    # 获取回答个数
    answer_num = question.get_answer_num()
    # 获取关注该问题的人数
    follower_num = question.get_follower_num()
    # 获取该问题所属话题
    topics = question.get_topics()
    # 获取排名第一的回答
    top_answer = question.get_top_answer()
    # 获取所有回答
    answers = question.get_all_answer()
    
    print title # 输出：现实可以有多美好？
    print detail 
    # 输出：
    # 本问题相对于“现实可以多残酷？传送门：现实可以有多残酷？
    # 题主：       昨天看了“现实可以有多残酷“。感觉不太好，所以我
    # 开了这个问题以相对应，希望能够“中和一下“。和那个问题题主不想
    # 把它变成“比惨大会“一样，我也不想把这个变成“鸡汤故事会“，或者
    # 是“晒幸福“比赛。所以大家从“现实，实际”的角度出发，讲述自己的
    # 美好故事，让大家看看社会的冷和暖，能更加辨证地看待世界，是此
    # 题和彼题共同的“心愿“吧。
    print answer_num # 输出：2441
    print follower_num # 输出：26910
    for topic in topics:
        print topic , # 输出：情感克制 现实 社会 个人经历
    print top_answer 
    # 输出：<zhihu.Answer instance at 0x7f8b6582d0e0>
    # 一个Answer类对象
    print answers 
    # 输出：<generator object get_all_answer at 0x7f8b66ba30a0>
    # 代表所有Answer的生成器

   
Answer：获取答案信息
~~~~~~~~~~~~~~~~~~~~~

Answer 代表了一个答案，处理知乎答案相关操作。创建一个 Answer 对象需传入该答案的 url ，如：

.. code-block:: python

    from zhihu import Answer
    
    answer_url = "http://www.zhihu.com/question/24269892/answer/29960616"
    answer = Answer(answer_url)

得到 Answer 对象后，可以获取该答案的一些信息：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    from zhihu import Answer
    
    answer_url = "http://www.zhihu.com/question/24269892/answer/29960616"
    answer = Answer(answer_url)
    # 获取该答案回答的问题
    question = answer.get_question()
    # 获取该答案的作者
    author = answer.get_author()
    # 获取该答案获得的赞同数
    upvote = answer.get_upvote()
    # 把答案输出为txt文件
    answer.to_txt()
    # 把答案输出为markdown文件
    answer.to_md()
    
    print question 
    # <zhihu.Question instance at 0x7f0b25d13f80>
    # 一个Question对象
    print question.get_title() # 输出：现实可以有多美好？
    print author 
    # <zhihu.User instance at 0x7f0b25425b90>
    # 一个User对象
    print author.get_user_id() # 输出：田浩
    print upvote # 输出：9320


User：获取用户信息
~~~~~~~~~~~~~~~~~~~~~~~

User 代表一个用户，处理用户相关操作。创建一个 User 对象需传入该用户的 url ，如：

.. code-block:: python
    
    from zhihu import User
    
    user_url = "http://www.zhihu.com/people/jixin"
    user = User(user_url)

得到 User 对象后，可以获取该用户的一些信息：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    from zhihu import User
    
    user_url = "http://www.zhihu.com/people/jixin"
    user = User(user_url)
    # 获取用户ID
    user_id = user.get_user_id()
    # 获取该用户的关注者人数
    follower_num = user.get_follower_num()
    # 获取该用户关注的人数
    followee_num =user.get_followee_num()
    # 获取该用户提问的个数
    ask_num = user.get_ask_num()
    # 获取该用户回答的个数
    answer_num = user.get_answer_num()
    # 获取该用户收藏夹个数
    collection_num = user.get_collection_num()
    # 获取该用户获得的赞同数
    agree_num = user.get_agree_num()
    # 获取该用户获得的感谢数
    thanks_num = user.get_thanks_num()
    
    # 获取该用户关注的人
    followees = user.get_followee()
    # 获取关注该用户的人
    followers = user.get_follower()
    # 获取该用户提的问题
    asks = user.get_ask()
    # 获取该用户回答的问题的答案
    answers = user.get_answer()
    # 获取该用户的收藏夹
    collections = user.get_collection()
    
    print user_id # 黄继新
    print follower_num # 614840
    print followee_num # 8408
    print ask_num # 1323
    print answer_num # 786
    print collection_num # 44
    print agree_num # 46387
    print thanks_num # 11477
    
    print followees
    # <generator object get_followee at 0x7ffcac3af050>
    # 代表所有该用户关注的人的生成器对象
    print followers
    # <generator object get_follower at 0x7ffcac3af0f0>
    # 代表所有关注该用户的人的生成器对象
    print asks
    # <generator object get_ask at 0x7ffcab9db780>
    # 代表该用户提的所有问题的生成器对象
    print answers
    # <generator object get_answer at 0x7ffcab9db7d0>
    # 代表该用户回答的所有问题的答案的生成器对象
    print collections
    # <generator object get_collection at 0x7ffcab9db820>
    # 代表该用户收藏夹的生成器对象


Collection：获取收藏夹信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collection 代表一个收藏夹，处理收藏夹相关操作。创建一个 Collection 对象需传入该收藏夹的 url ，如：

.. code-block:: python

    from zhihu import Collection
    
    collection_url = "http://www.zhihu.com/collection/36750683"
    collection = Collection(collection_url)

得到 Collection 对象后，可以获取该收藏夹的一些信息：

.. code-block:: python
    
    # -*- coding: utf-8 -*-
    from zhihu import Collection
    
    collection_url = "http://www.zhihu.com/collection/36750683"
    collection = Collection(collection_url)
    
    # 获取该收藏夹的创建者
    creator = collection.get_creator()
    # 获取该收藏夹的名字
    name = collection.get_name()
    # 获取该收藏夹下的所有答案
    answers = collection.get_all_answer()
    
    print creator 
    # <zhihu.User instance at 0x7fe1296f29e0>
    # 一个User对象
    print creator.get_user_id() # 稷黍
    print name # 给你一个不同的视角
    print answers 
    # <generator object get_all_answer at 0x7fe12a29b280>
    # 代表所有答案的生成器对象
    

综合实例
~~~~~~~~~~~~~~~

有待添加



API
-------

有待添加



联系我
----------

- 知乎：`@egrcc <http://www.zhihu.com/people/egrcc>`_
- 微博：`@egrcc <http://weibo.com/u/2948739432>`_
- github：`@egrcc <https://github.com/egrcc>`_
- email：zhaolujun1994@email.com
