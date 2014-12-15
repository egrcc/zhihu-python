# Excel 有哪些可能需要熟练掌握而很多人不会的技能？
## 作者: 呆萌青年杨二傻  赞同: 307
上个视频：

![](http://g1.ykimg.com/0100641F4652FB7368B17813A354679FB7679E-F435-612D-
1C88-FC1F67243FEF)__

Excel虚拟钟表

http://v.youku.com/v_show/id_XNjcyMjc3NTQ4.html


撸了一天VBA……实在是按耐不住啊……开机来回答
[@未央之末](http://www.zhihu.com/people/b29d7985efa61866fdf25da24f65b736)
的回答很赞……完全勾起了我的回忆…………
最开始的时候用Excel完全是当做Word那种用法……偶尔敲个公式还局限于四则运算
上班之后需求就多了，身边有一位大神，用Excel把试验所有的计算都写成了板子，造福人类
亲眼目睹之后我深深的表示震惊…
==================以上背景=================
未央之末的回答已经很完美了，平时注意排版，注意数据维护
我再说说其他的几个方面的

**定义名称：**
在公式引用的时候A1法是最常引用的，形如：



=sum(A1:A10)



公式下拉的时候某些变量不用更改相对索引，但是Excel会自动的更改相对索引，这时候使用F4可以固定维度



=$A$2+B2


这样即使下拉，也只有B2会变化。PS：连续按F4会切换锁定的维度
还有一种更便捷的方法就是定义变量
在单元格上右键选择自定义名称，如图：
![](http://pic3.zhimg.com/647e001763b2a1608f7f575d4cf8c850_b.jpg)
Excel会智能的识别出目标单元格的名称，当然，如果冲突还需要更改，可以写入备注
![](http://pic2.zhimg.com/389665c0c8471f7faffe2ea07d814b78_b.jpg)
当你自定义名称之后，再次引用这个单元格的时候只需要输入名称就可以了，在你输入名称的时候你所添加的备注也会实时出现，甚至没有拼写完你都可以使用Tab
自动补齐：
![](http://pic2.zhimg.com/33ae9d2a86b24589dbff06d0dccbfc19_b.jpg)
数组也可以定义为名称，感觉应该和Range对象一样
VBA有时需要引用表格内容，不论是A1法还是用Cells
引用，一旦单元格出现增删行列，VBA引用的目标就会发生变化。这使得后期维护难度增大，使用名称可以避免这个问题，增删行列的时候Excel会自动更改。
需要注意的是在VBA中使用名称需要用中括号括起来。这时候自定义名称相当于一个全局变量(真正地全局……对整个workbook
全局)，可以引用，甚至可以赋值，对比之下A1法和Cells则相当不美观也不利于阅读。
随手拷贝了几行，一个简单的例子。[PowerLevel]和[BULevel]是数组，你们感受一下：



RowNum=WorksheetFunction.Match(P,[PowerLevel],-1)+4
ColumnNum=WorksheetFunction.Match([BU],[BULevel],1)+2
[KME]=PthAvg(T,Dt)


我定义的名称，你们感受一下：
![](http://pic1.zhimg.com/e87ef7ca36621c70f42db6a968db36ef_b.jpg)
**函数以及自定义函数：**
Excel的函数真的很牛x，第一的答案写的很详尽了，不表。输入的时候即时提醒做的很赞~
有时候需要一些特定的计算，如果全部用公式的话略显繁琐，并且公式会很长很长很长很长……
我曾经就写过很长很长很长很长很长的公式…(插一句，Excel公式输入的地方是可以拉来的，结合Alt+Enter
可以实现换行和缩进等等，我来上个图……）
![](http://pic2.zhimg.com/02c3faa7965c95f8f30552e86abdee4c_b.jpg)
自定义函数方便维护，花样繁多，玩大的还可以去直接导入其他语言开发的库
直接上列子……



FunctionRho(P1AsDouble,P0AsDouble)AsDouble
'根据功率变化计算反应性
Rho=[beta_eff]/[lambda]/60*Log(P1/P0)
EndFunction



然后你就可以愉快的使用了
![](http://pic1.zhimg.com/43a92dd199cd25c33fb07eadbb17aa7f_b.jpg)
唯一的遗憾是无法在Excel界面中即时提示……在VBE里面可以即时提示……顺便打车求解决方法……好像说注册DLL欺骗Excel
可以做到……求少折腾的方法


**VBA：**
VBA我就不多说了，能干的事情太多了，虽然速度有点慢，但是合理的优化，关闭刷新，处理日常的工作还是可以的。
不会写代码刚开始学可以直接录，录完了好好读一读，删掉无用的就好。经常看看自带的帮助文档，干货很多。不会了就慢慢地google，百度……

**界面：**
严格说起来界面应该属于VBA，这部分和VB类似，不过貌似不支持控件数组，当然旁门左道也能实现控件数组。在Workbook_Open事件里面写上：



Application.Visible=False
xxx窗体.show


让Excel伪装成一个程序……完全看不到Excel的界面~
PS：请不要看不起我们这些拖控件的……
![](http://pic1.zhimg.com/3000fdf710b663bb271f1511aea748ba_b.jpg)
**引用与库函数：**
这里的引用特质VBA的工程引用，这时候可以绑定一些封装好的库文件，个人偏爱MatrixVB，最早是我用来增强VB的运算的，后来玩Excel
发现也能在VBA里跑，不过参考文档很屎，老古董了。
大型计算忍不了VBA的渣速度的也可以用其他语言做库然后让Excel来用，不过我用的不是很好，尝试过用FORTRAN写，只局限于实验阶段……

**自定义界面：**
如果自己用，直接在选项里面添加就可以了，如果是给别人用，可以做成含有Ribbon界面的加载项，一般后缀是xla和xlam。
Ribbon可以指定快捷键，指定ScreenTip和SuperTip，XML语言就好，喜欢折腾的不要错过。
半途而废的东西：在Excel中打开其他软件……用的是
Shell……做不下去了，因为完全没需求，从来都单手盲开任何常用软件网站……要问我为何这么屌，因为我有AutoHotKey呀
![](http://pic2.zhimg.com/6f5a6fbf6750a117cee7027e5d09cdc9_b.jpg)
还有高大上的就不跟你们秀了…………

**其他：**
下面这些东西就有点奇葩了，**FileDialog，Shell，API**
这就属于瞎折腾了，不表~

另外两个：

![](http://g2.ykimg.com/0100641F4652FB7225800713A35467317FC110-9382-8D0F-
0C97-83E30F166644)__

Excel绘制李萨茹图

http://v.youku.com/v_show/id_XNjcyMjc1Mzk2.html

![](http://g1.ykimg.com/0100641F4652FB740C8A2A13A354676EAFF1FD-B793-6AAD-6550-
7183730CC525)__

Excel随机游动小球

http://v.youku.com/v_show/id_XNjcyMjc4NjU2.html

#### 原链接: http://www.zhihu.com/question/21758700/answer/22411057