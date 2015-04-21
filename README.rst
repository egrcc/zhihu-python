zhihu-python：获取知乎信息
===============================

介绍
----

zhihu-python 采用 python2.7 编写，用来方便地获取知乎上各种内容的信息，并且可以方便地将答案备份导出为 txt 或 markdown 文件。由于知乎官方目前没有提供 api，所以有了此项目的存在。

使用 python3 的类似项目可以参见：`zhihu-py3 <https://github.com/7sDream/zhihu-py3>`_ 。

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

或者使用

.. code-block:: bash

    $ pip install -r requirements.txt

**注意** ：如果同时安装了 python3 和 python2 ， pip 命令可能默认安装的是 python3 版本的包，故需将上述命令中的 pip 换成pip2 （比如在我的Ubuntu上）。

快速开始
---------

zhihu-python 主要文件为 zhihu.py ，配置文件为 config.ini , 将这两个文件下载到你的工作目录，并修改
config.ini 文件中的 email 为你的知乎账户邮箱，修改 password 为你的知乎账户密码（用作模拟登录）。

(2015.2.1更新)由 `@Eureka22 <https://github.com/Eureka22>`_ 添加了cookies支持，若由于验证码原因出现登录失败，请查看浏览器的cookies，填写 config.ini 文件中的 cookies 项后重试（当然，你的cookies可能与  cogfig.ini 文件中的某些项不同，比如没有“c_c”，可能会多出“_ga”，把你的补充上去即可）。如能正常登录，cookies 项可以不填写。

**注意** ：一定记得修改config.ini文件，否则无法正常使用。

 
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
    

综合实例
~~~~~~~~~~~~~~~

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



联系我
----------

- 知乎：`@egrcc <http://www.zhihu.com/people/egrcc>`_
- 微博：`@egrcc <http://weibo.com/u/2948739432>`_
- github：`@egrcc <https://github.com/egrcc>`_
- email：zhaolujun1994@gmail.com
