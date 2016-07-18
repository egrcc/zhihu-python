zhihu-python：获取知乎信息
===============================

**注意: 本项目不再维护更新！**

.. contents::


介绍
----

zhihu-python 采用 Python2.7 编写，用来方便地获取知乎上各种内容的信息，并且可以方便地将答案备份导出为 txt 或 markdown 文件。由于知乎官方目前没有提供 api，所以有了此项目的存在。

使用 Python3 的类似项目可以参见：`zhihu-py3 <https://github.com/7sDream/zhihu-py3>`_ 。使用 PHP 的类似项目可以参见：`zhihu-php <https://github.com/ahonn/zhihu-php>`_ 。使用 Go 的类似项目可以参见：`zhihu-go <https://github.com/DeanThompson/zhihu-go>`_ 。

**注: 本项目代码均在 Ubuntu14.04 上使用 python2.7.6 编写和测试通过，其他环境可能存在一定问题。**

获取某个问题下的全部回答并导出，很简单：

.. code-block:: python

    from zhihu import Question
    
    url = "http://www.zhihu.com/question/24269892"
    question = Question(url)
    answers = question.get_all_answers()
    for answer in answers:
        answer.to_txt()
        answer.to_md()
 
会在当前目录下新建text，markdown两个文件夹，并将所有txt文件保存到text文件夹，所有markdown文件保存到markdown文件夹。

备份某大V的全部回答，也很简单：

.. code-block:: python
    
    from zhihu import User
    
    user_url = "http://www.zhihu.com/people/jixin"
    user = User(user_url)
    answers = user.get_answers()
    for answer in answers:
        answer.to_txt()
        answer.to_md()
        
导出的markdown，txt文件示例请见该项目的markdown，text文件夹。当然，想要知道某大V关注了那些人，提了什么问题也不在话下，详情请见：快速开始。        



快速开始
---------

准备
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Tips** :

1.  确保你的系统里面已经安装了 `Python2.7 <https://www.python.org/>`_ ，不同作业系统如何安装不再赘述。
2.  检查你系统中 `python` 和 `pip` 的版本, 如果不属于 `python2.7` , 请在执行代码范例时，自行将 `python` 和 `pip` 分别替换成 `python2.7` 和 `pip2` 。
3.  确保你的系统中安装了 `git` 程序 以及 `python-pip` 。


**克隆本项目**


.. code:: bash

  git clone git@github.com:egrcc/zhihu-python.git
  cd zhihu-python


**解决依赖**

* `Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>`_
* `requests <https://github.com/kennethreitz/requests>`_
* `html2text <https://github.com/aaronsw/html2text>`_
* `termcolor <https://pypi.python.org/pypi/termcolor>`_
* `lxml <https://github.com/lxml/lxml>`_

.. code:: bash

  sudo pip install -r requirements.txt


or

.. code:: bash

  sudo pip2 install -r requirements.txt



**登录知乎**


登录 `知乎` 生成身份信息, 保存在当前目录的 `cookies` 文件中。

.. code:: bash
  
  python auth.py


**执行测试**


.. code:: bash

  python test.py

不出意外，一切应该完美运行 :))



Question：获取问题信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    answers_num = question.get_answers_num()
    # 获取关注该问题的人数
    followers_num = question.get_followers_num()
    # 获取该问题所属话题
    topics = question.get_topics()
    # 获取该问题被浏览次数
    visit_times = question.get_visit_times()
    # 获取排名第一的回答
    top_answer = question.get_top_answer()
    # 获取排名前十的十个回答
    top_answers = question.get_top_i_answers(10)
    # 获取所有回答
    answers = question.get_all_answers()

    print title  # 输出：现实可以有多美好？
    print detail
    # 输出：
    # 本问题相对于“现实可以多残酷？传送门：现实可以有多残酷？
    # 题主：       昨天看了“现实可以有多残酷“。感觉不太好，所以我
    # 开了这个问题以相对应，希望能够“中和一下“。和那个问题题主不想
    # 把它变成“比惨大会“一样，我也不想把这个变成“鸡汤故事会“，或者
    # 是“晒幸福“比赛。所以大家从“现实，实际”的角度出发，讲述自己的
    # 美好故事，让大家看看社会的冷和暖，能更加辨证地看待世界，是此
    # 题和彼题共同的“心愿“吧。
    print answers_num  # 输出：2441
    print followers_num  # 输出：26910
    for topic in topics:
        print topic,  # 输出：情感克制 现实 社会 个人经历
    print visit_times  # 输出: 该问题当前被浏览的次数
    print top_answer  
    # 输出：<zhihu.Answer instance at 0x7f8b6582d0e0>
    # Answer类对象
    print top_answers  
    # 输出：<generator object get_top_i_answers at 0x7fed676eb320>
    # 代表前十的Answer的生成器
    print answers  
    # 输出：<generator object get_all_answer at 0x7f8b66ba30a0>
    # 代表所有Answer的生成器

   
Answer：获取答案信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    # 获取该答案所属问题被浏览次数
    visit_times = answer.get_visit_times()
    # 获取所有给该答案点赞的用户信息
    voters = answer.get_voters()
    # 把答案输出为txt文件
    answer.to_txt()
    # 把答案输出为markdown文件
    answer.to_md()

    print question
    # <zhihu.Question instance at 0x7f0b25d13f80>
    # 一个Question对象
    print question.get_title()  # 输出：现实可以有多美好？
    print author
    # <zhihu.User instance at 0x7f0b25425b90>
    # 一个User对象
    print voters 
    # <generator object get_voters at 0x7f32fbe55730>
    # 代表所有该答案点赞的用户的生成器
    print author.get_user_id()  # 输出：田浩
    print upvote  # 输出：9320
    print visit_times  # 输出: 改答案所属问题被浏览次数


User：获取用户信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    # 获取用户性别
    user_gender = user.get_gender()
    # 获取该用户的关注者人数
    followers_num = user.get_followers_num()
    # 获取该用户关注的人数
    followees_num =user.get_followees_num()
    # 获取该用户提问的个数
    asks_num = user.get_asks_num()
    # 获取该用户回答的个数
    answers_num = user.get_answers_num()
    # 获取该用户收藏夹个数
    collections_num = user.get_collections_num()
    # 获取该用户获得的赞同数
    agree_num = user.get_agree_num()
    # 获取该用户获得的感谢数
    thanks_num = user.get_thanks_num()
    # 获取该用户的头像url
    head_img_url = user.get_head_img_url()
    
    # 获取该用户关注的人
    followees = user.get_followees()
    # 获取关注该用户的人
    followers = user.get_followers()
    # 获取该用户提的问题
    asks = user.get_asks()
    # 获取该用户回答的问题的答案
    answers = user.get_answers()
    # 获取该用户的收藏夹
    collections = user.get_collections()
    
    print user_id # 黄继新
    print followers_num # 614840
    print followees_num # 8408
    print asks_num # 1323
    print answers_num # 786
    print collections_num # 44
    print agree_num # 46387
    print thanks_num # 11477
    print head_img_url  # https://pic2.zhimg.com/0626f4164009f291b26a79d96c6962c5_l.jpg
    
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    # 获取该收藏夹下的前十个答案
    top_answers = collection.get_top_i_answers(10)
    # 获取该收藏夹下的所有答案
    answers = collection.get_all_answers()
    
    print creator 
    # <zhihu.User instance at 0x7fe1296f29e0>
    # 一个User对象
    print creator.get_user_id() # 稷黍
    print name # 给你一个不同的视角
    print top_answers
    # <generator object get_top_i_answers at 0x7f378465dc80>
    # 代表前十个答案的生成器对象
    print answers 
    # <generator object get_all_answer at 0x7fe12a29b280>
    # 代表所有答案的生成器对象


Column：获取专栏信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Column 代表一个专栏，处理专栏相关操作。创建一个 Column 对象需传入该专栏的 url ，如：

.. code-block:: python

    from zhihu import Column
    
    url = "http://zhuanlan.zhihu.com/daily"
    column = Column(url)

得到 Column 对象后，可以获取该专栏的一些信息：

.. code-block:: python

    # -*- coding: utf-8 -*-
    from zhihu import Column
    
    url = "http://zhuanlan.zhihu.com/daily"
    column = Column(url)

    # 获取该专栏的标题
    title = column.get_title()
    # 获取该专栏的描述
    description = column.get_description()
    # 获取该专栏的作者
    creator = column.get_creator()
    # 获取该专栏的文章数
    posts_num = column.get_posts_num()
    # 获取该专栏的所有文章
    posts = column.get_all_posts()

    print title  # 输出：知乎日报
    print description
    # 输出：
    # 知乎日报启动画面接受所有摄影师朋友们的投稿，将作品链接
    #（如 Flickr、LOFTER 等等），发至邮箱 qidong (at) zhihu.com，
    # 并附上您的知乎个人页面地址即可。
    # 
    # 详细投稿要求: http://t.cn/zQyEpN5

    print creator  
    # 输出：<zhihu.User instance at 0x75e33eb8>
    # User类对象
    print posts_num # 150 
    print posts
    # 输出：<generator object get_all_posts at 0x75e33bc0>
    # Post类对象


Post：获取专栏文章信息
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Post 代表一个专栏文章，处理专栏文章相关操作。创建一个 Post 对象需传入该文章的 url ，如：

.. code-block:: python

    from zhihu import Post
    
    url = "http://zhuanlan.zhihu.com/p/20235601"
    post = Post(url)

得到 Post 对象后，可以获取该文章的一些信息：

.. code-block:: python

    # -*- coding: utf-8 -*-
    from zhihu import Post
    
    url = "http://zhuanlan.zhihu.com/p/20770968"
    post = Post(url)

    # 获取该文章的标题
    title = post.get_title()
    # 获取该文章的内容
    content = post.get_content()
    # 获取该文章的作者
    author = post.get_author()
    # 获取该文章的所属专栏
    column = post.get_column()
    # 获取该文章所属话题
    topics = post.get_topics()

    print title  # 输出：夜读书|四月十九日
    print content
    # 输出：
    # <p>各位，晚上好。<br> ...
    # ......
    print author
    # 输出： <zhihu.User instance at 0x75ec0fd0>
    for topic in topics:
        print topic,  # 输出：阅读
    print column  
    # 输出：<zhihu.Column instance at 0x75eb3eb8>
    # Column类对象
    

综合实例
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

将 Question ， Answer ， User ， Collection 结合起来使用。实例如下：

.. code-block:: python

    # -*- coding: utf-8 -*-
    from zhihu import Question
    from zhihu import Answer
    from zhihu import User
    from zhihu import Collection
    
    url = "http://www.zhihu.com/question/24269892"
    question = Question(url)
    # 得到排名第一的答案
    answer = question.get_top_answer()
    # 得到排名第一的答案的作者
    user = answer.get_author()
    # 得到该作者回答过的所有问题的答案
    user_answers = user.get_answers()
    # 输出该作者回答过的所有问题的标题
    for answer in user_answers:
        print answer.get_question().get_title()
    # 得到该用户的所有收藏夹
    user_collections = user.get_collections()
    for collection in user_collections:
	# 输出每一个收藏夹的名字
        print collection.get_name()
	# 得到该收藏夹下的前十个回答
        top_answers = collection.get_top_i_answers(10)
	# 把答案内容转成txt，markdown
        for answer in top_answers:
            answer.to_txt()
            answer.to_md()

以上示例均可以在test.py文件中找到。

虽然是单线程，但速度不算太慢。抓取 `哪些东西买了之后，会让人因生活质量和幸福感提升而感觉相见恨晚？ <http://www.zhihu.com/question/20840874>`_ 下前200个回答，91秒；抓取 `有哪些 100 元以下，很少见但高大上的物件？ <http://www.zhihu.com/question/23054572>`_ 下前50个回答，48秒；抓取 `现实可以有多美好？ <http://www.zhihu.com/question/24269892>`_ 下前200个回答，69秒。生成的文件请见markdown，text文件夹。所有匿名用户的回答放在一个文件里面。


API
-------

zhihu.Question ---- 知乎问题操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **Question** (*url, title = None*)

 Question 以 url 为唯一标识，创建一个 Question 对象实例必须传入一个代表知乎问题的 url （如：         http://www.zhihu.com/question/26611428），需包含“http://”。如果传入的不是代表问题的 url ，程序会报错。通过调用 Question 类的一系列方法，获得该问题的一些信息。
 
 **Parameters**：
  * **url** -- 该问题的链接，字符串
  * **title** -- 该问题的标题，字符串，可选
 
 **Returns**： 一个 Question 实例对象
 
 **get_title** ()
 
  得到该问题的标题。
  
  **Returns**： 代表标题的字符串
 
 **get_detail** ()
 
  得到该问题的详细描述。原问题的描述可能带有图片或视频，这里得到的是纯文字。
  
  **Returns**： 代表详细描述的字符串
 
 **get_answers_num** ()
 
  得到该问题的回答个数。
  
  **Returns**： 代表回答个数的 int 型整数
 
 **get_followers_num** ()
 
  得到关注该问题的人数。
  
  **Returns**： 代表人数的 int 型整数
 
 **get_topics** ()
 
  得到该问题所属的话题。
  
  **Returns**： 一个 list ，每一个元素为代表一个话题的字符串
  
  注：以后可能会添加一个 Topic 类，到时候每一个元素为代表一个话题的 Topic 类对象。
 
 **get_all_answers** ()
 
  得到该问题的所有回答。
  
  **Returns**： 包含所有答案的 generator 对象。其中每一个元素为代表一个答案的 Answer 对象 
 
 **get_top_i_answers** (n)
 
  得到该问题的前 n 个回答。
  
  **Parameters**： **n** -- int 型整数
  
  **Returns**： 包含前 n 个答案的 generator 对象。其中每一个元素为代表一个答案的 Answer 对象
 
 **get_top_answer** ()
 
  得到目前排名第一的回答。
 
  **Returns**： 代表该答案的 Answer 对象
  
 **get_visit_times** ()
 
  得到该问题被浏览次数。该方法由 `@lufo816 <https://github.com/lufo816>`_ 添加。
 
  **Returns**： 代表浏览次数的 int 型整数
 

zhihu.User ---- 知乎用户操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **User** (*user_url, user_id = None*)

 User 以 url 为唯一标识，创建一个 User 对象实例必须传入一个代表知乎用户的 url （如：         http://www.zhihu.com/people/egrcc），需包含“http://”。如果传入的不是代表用户的 url ，程序会报错。通过调用 User 类的一系列方法，获得该用户的一些信息。
 
 **Parameters**：
  * **user_url** -- 该用户的链接，字符串
  * **user_id** -- 该用户的 ID ，字符串，可选
  
 **Returns**： 一个 User 实例对象

 **get_user_id** ()
 
  得到该用户的ID。
  
  **Returns**： 代表 ID 的字符串

 **get_gender** ()
 
  得到该用户的性别。
  
 **Returns**： 代表 性别 的字符串(male/female)  
  
 **get_followees_num** ()
 
  得到该用户关注的人的个数。
  
  **Returns**： 代表人数的 int 型整数
 
 **get_followers_num** ()
 
  得到关注该用户的人的个数。
  
  **Returns**： 代表人数的 int 型整数
 
 **get_agree_num** ()
 
  得到该用户获得的赞同数。
  
  **Returns**： 代表赞同数的 int 型整数
 
 **get_thanks_num** ()
 
  得到该用户获得的感谢数。
  
  **Returns**： 代表感谢数的 int 型整数

 **get_head_img_url** (scale)

  获取用户头像url。该方法由 `@liuwons <https://github.com/liuwons>`_ 添加。

  **Parameters**： **scale** int 型整数，代表尺寸: 1(25×25), 3(75×75), 4(100×100), 6(150×150), 10(250×250)

  **Returns**： 对应尺寸头像的图片链接, 字符串
 
 **get_asks_num** ()
 
  得到该用户提问题的个数。
  
  **Returns**： 代表问题数的 int 型整数 
 
 **get_answers_num** ()
 
  得到该用户回答问题的个数。
  
  **Returns**： 代表问题数的 int 型整数 
 
 **get_collections_num** ()
 
  得到该用户收藏夹的个数。
  
  **Returns**： 代表收藏夹数的 int 型整数 
 
 **get_followees** ()
 
  得到该用户关注的人。
  
  **Returns**： 包含所有该用户关注的人的 generator 对象。其中每一个元素为代表一个用户的 User 对象
 
 **get_followers** ()
 
  得到关注该用户的人。
  
  **Returns**： 包含所有关注该用户的人的 generator 对象。其中每一个元素为代表一个用户的 User 对象
 
 **get_asks** ()
 
  得到该用户提的所有问题。
  
  **Returns**： 包含所有问题的 generator 对象。其中每一个元素为代表一个问题的 Question 对象
 
 **get_answers** ()
 
  得到该用户回答的所有问题的答案。
  
  **Returns**： 包含所有回答的 generator 对象。其中每一个元素为代表一个回答的 Answer 对象
 
 **get_collections** ()
 
  得到该用户的所有收藏夹。
  
  **Returns**： 包含所有收藏夹的 generator 对象。其中每一个元素为代表一个收藏夹的 Collection 对象
 

zhihu.Answer ---- 知乎回答操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **Answer** (*answer_url, question = None, author = None, upvote = None, content = None*)

 Answer 以 url 为唯一标识，创建一个 Answer 对象实例必须传入一个代表知乎回答的 url （如：         http://www.zhihu.com/question/19878575/answer/14776495），需包含“http://”。如果传入的不是代表回答的 url ，程序会报错。通过调用 Answer 类的一系列方法，获得该回答的一些信息。一般不自己创建Answer对象。
 
 **Parameters**：
  * **answer_url** -- 该答案的链接，字符串
  * **question** -- 该答案回答的问题， Question 对象，可选
  * **author** -- 该答案的作者， User 对象，可选
  * **upvote** -- 该答案获得的赞同数， int 型整数，可选
  * **content** -- 该答案的内容， BeautifulSoup 对象，可选
  
 **Returns**： 一个 Answer 实例对象

 **get_question** ()
 
  得到该答案回答的问题。
  
  **Returns**： 一个 Question 对象
 
 **get_author** ()
 
  得到该答案的作者 。
  
  **Returns**： 一个 User 对象
 
 **get_upvote** ()
 
  得到该答案获得的赞同数。
  
  **Returns**： 一个 int 型整数
 
 **get_content** ()
 
  得到该答案的内容。
  
  **Returns**： 一个 BeautifulSoup 对象
  
 **get_visit_times** ()
 
  得到该答案所属问题被浏览次数。该方法由 `@lufo816 <https://github.com/lufo816>`_ 添加。
 
  **Returns**： 代表浏览次数的 int 型整数
  
 **get_voters** ()
 
  得到给该答案点赞的用户。该方法由 `@lufo816 <https://github.com/lufo816>`_ 添加。
 
  **Returns**： 包含所有给该答案点赞的用户的 generator 对象。其中每一个元素为代表一个用户的 User 对象
 
 **to_txt** ()
  
  将该答案转成txt文件，并会在当前目录下创建一个text文件夹，所生成的txt文件均保存在该文件夹。
 
 **to_md** ()
 
  将该答案转成markdown文件，并会在当前目录下创建一个markdown文件夹，所生成的markdown文件均保存在该文件夹。


zhihu.Collection ---- 知乎收藏夹操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **Collection** (*url, name = None, creator = None*)

 Collection 以 url 为唯一标识，创建一个 Collection 对象实例必须传入一个代表知乎收藏夹的 url （如：         http://www.zhihu.com/collection/27053469），需包含“http://”。如果传入的不是代表收藏夹的 url ，程序会报错。通过调用 Collection 类的一系列方法，获得该收藏夹的一些信息。
 
 **Parameters**：
  * **url** -- 该收藏夹的链接，字符串
  * **name** -- 该收藏夹的名字，字符串，可选
  * **creator** -- 该收藏夹的创建者，User 对象，可选
  
 **Returns**： 一个 Collection 实例对象

 **get_name** ()
 
  得到该收藏夹的名字。
  
  **Returns**： 代表名字的字符串
 
 **get_creator** ()
 
  得到该收藏夹的创建者。
  
  **Returns**：代表创建者 User 对象
 
 **get_all_answers** ()
 
  得到该收藏夹收藏的所有回答。
  
  **Returns**： 包含该收藏夹下所有回答的 generator 对象。其中每一个元素为代表一个回答的 Answer 对象
 
 **get_top_i_answers** (n)
 
  得到该收藏夹收藏的前 n 个回答。
  
  **Parameters**： **n** -- int 型整数
  
  **Returns**： 包含该收藏夹下前 n 个回答的 generator 对象。其中每一个元素为代表一个回答的 Answer 对象


zhihu.Column ---- 知乎专栏操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **Column** (*Column_url*)

 Column 以 url 为唯一标识，创建一个 Column 对象实例必须传入一个代表知乎专栏的 url （如：http://zhuanlan.zhihu.com/daily），需包含“http(s)://”。如果传入的不是代表专栏的 url ，程序会报错。通过调用 Column 类的一系列方法，获得该专栏的一些信息。该类由 `@johnnyluck <https://github.com/johnnyluck>`_ 添加。
 
 **Parameters**：
  * **column_url** -- 该专栏的链接，字符串
  
 **Returns**： 一个 Column 实例对象

 **get_title** ()
 
  得到该专栏的题目。
  
  **Returns**： 一个代表题目的字符串 
 
 **get_creator** ()
 
  得到该专栏的创建者。
  
  **Returns**： 一个 User 对象
 
 **get_description** ()
 
  得到该专栏的描述。
  
  **Returns**： 一个专栏描述的字符串

 **get_followers_num** ()

  得到该专栏的关注人数。

  **Returns**： 一个 int 型的整数
 
 **get_posts_num** ()

  得到该专栏的所有文章数。

  **Returns**： 一个 int 型的整数
 
 **get_content** ()
 
  得到该答案的内容。
  
  **Returns**： 一个字符串

 **get_posts** ()

  得到该专栏的所有文章。

  **Returns**：包含所有文章的 generator 对象。其中每一个元素为代表一个文章 Post 对象
 

zhihu.Post ---- 知乎专栏文章操作类
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*class* zhihu. **Post** (*Post_url*)

 Post 以 url 为唯一标识，创建一个 Post 对象实例必须传入一个代表知乎文章的 url （如：http://zhuanlan.zhihu.com/p/20235601），需包含“http(s)://”。如果传入的不是代表文章的 url ，程序会报错。通过调用 Post 类的一系列方法，获得该文章的一些信息。该类由 `@johnnyluck <https://github.com/johnnyluck>`_ 添加。
 
 **Parameters**：
  * **post_url** -- 该文章的链接，字符串
  
 **Returns**： 一个 Post 实例对象

 **get_title** ()
 
  得到该文章的题目。
  
  **Returns**： 一个代表题目的字符串 
 
 **get_author** ()
 
  得到该文章的作者。
  
  **Returns**： 一个 User 对象
 
 **get_content** ()
 
  得到该文章的内容。
  
  **Returns**： 一个文章描述的字符串

 **get_topics** ()
 
  得到该文章的话题。
  
  **Returns**： 一个列表

 **get_column** ()

  得到该文章的所属专栏。

  **Returns**：一个 Column 的实例对象
 

