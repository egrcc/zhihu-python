zhihu-python：获取知乎信息
============================

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

**注意** ：如果同时安装了 python3 和 python2 ， pip 命令可能默认安装的是 python3 版本的包，故需将上述命令中的 pip 换成
pip2 （比如在我的Ubuntu上）。

快速开始
---------

zhihu-python主要文件为zhihu.py

