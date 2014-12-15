# Excel 有哪些可能需要熟练掌握而很多人不会的技能？
## 作者: Yumeng Guo  赞同: 3049
2014-12-10更新  

函数、VBA、图表是Excel的三把利器，希望这篇关于图表的回答能给大家一些启迪。但我最擅长的其实还是前两者。在这我就不放函数和VBA的笔记了。因为，我相信
，要想熟练掌握函数与VBA，最好的办法还是借一本入门书，夯实基础，循序渐进。今天这里学一招，明天那里记住一个公式，会只见树木不见森林。

  

比如，Vlookup函数似乎成了新手迈向Excel初学者的第一步，但你可知Vlookup有很大的局限性？如果你借了本书从基础抓起，就会同时掌握Hlookup
和lookup，还有更加灵活的Index与Match。

  

就像学了英语之后会发现更大的世界，自从掌握了函数与初步VBA，我也发现了更大的世界，处理数据会有全新的思路，不曾想到过的功能变成现实，像一个程序员一样做出些
人机交互的”Excel app”。你会发现，配合函数与VBA，任何重复性工作都可以一键化实现。

  

因为工作中离不开Excel，经常使用，掌握的技能就不会生疏，而是越发触类旁通，稳步提升。

所以，如果在可见的未来，你的工作中会用到Excel，我建议你集中一段时间花上100～150个小时玩一玩Excel，乐趣无穷。

  
  
2014-12-9更新  
图表制作方面的技巧我大多自学于刘万祥的资料，这个回答中的某些图片也来自刘老师。在此一并感谢。  

> 刘老师出的书 [ Excel图表之道 (豆瓣) _ _ ](http://book.douban.com/subject/4326057/)  
刘老师的博客 [ ExcelPro的图表博客 _ _ ](http://excelpro.blog.sohu.com/)

  
2014-12-8更新  
感谢大家的赞，但我也知道这回答长了点，所以为节约大家的时间，我选取了一个经典案例，辅以详细的说明（中文版Excel2013）放在开头，供各位参考。  
  
看完这个案例之后，我们也可以尝试绘制这种商务风格的表格。  
![](http://pic1.zhimg.com/e9b5120c07e98b0c48cf59e5dd0d5178_b.jpg)
![](http://pic4.zhimg.com/e879dedf06688d97062ce9c944722c56_b.jpg)  
下图是我做的，看完详细的绘制步骤，你将深刻体会到“ **用Excel的元素辅助作图** ”的含义。  
![](http://pic4.zhimg.com/6e04876bf42a98f9abb8df24951547cd_b.jpg) 首先选中源数据，A到F列  
![](http://pic1.zhimg.com/61f694871ab87aac1b237f08238c56b5_b.jpg)
绘制散点图，得到经典的Excel风格图表  
![](http://pic3.zhimg.com/21142c096a41d1f83190114dcccd655e_b.jpg)

将利润率设为次坐标：选中橙色那根线，右键-设置数据系列格式-次坐标轴

![](http://pic3.zhimg.com/3305c5b49118e7bd29fc010004779026_b.jpg)

删去图表标题、图例，调节横坐标、两个纵坐标的上下限，删去纵网格线，删去两个纵坐标的轴线，得到这样一张图

  
![](http://pic1.zhimg.com/7c27bf696143671c22b554572f938c86_b.jpg)

下一步称为“锚定”，鼠标光标移动到下图所示的图表左上角的顶点处，按住Alt，随后按住鼠标进行拖动，发现这样调节图表的尺寸，限定于Excel的网格点。

  
  
![](http://pic1.zhimg.com/6a9be351f0cdc9ec60ca2ee2ea9f2c3f_b.jpg)

四个角都这样进行调节，分别“锚定”于N7, V7, N15, V15

![](http://pic1.zhimg.com/4ba38536e6b7f102ffe91a8b2998116a_b.jpg)

选中图表区域，右键-设置图表区域格式，在属性中选择“大小固定，位置随单元格而变”，这样，在调整Excel行距和列宽时，图表就不会随之而动。

![](http://pic3.zhimg.com/5d1d03627d70545bfe7f068993131457_b.jpg)  

在第4~6行输入内容，设置填充色

![](http://pic1.zhimg.com/23b031f67804cafbefd7bdfc9cbe742b_b.jpg)

调节7~15行行距，使得Excel网格线与我们做的图表的横向网格线一一重叠；

调节O列和U列列宽，使得O列左侧网格线恰好经过图表横向网格线的起点，U列右侧这根网格线也是一样的道理，如下图所示。

![](http://pic3.zhimg.com/842ea4b5ba7443895b1b2d607f0b9917_b.jpg)

选中图表区，填充色改为无色，外轮廓也删去，这样图表就变成“透明”的了

![](http://pic2.zhimg.com/4d86ffc83fb3969634060e9b5098b5e7_b.jpg)

随后对N7:V15这个区域的单元格进行填充色。

（选中这些单元格的方法：

先选中图表区域外的一个单元格，如M7，按键盘的→键，移动到N7，然后按住Shift，再按→键或↓键调节即可，选中后进行单元格填充。）

![](http://pic1.zhimg.com/701e75eb66b31c50908e160f4a0032fc_b.jpg)  

在Excel“视图”中取消勾选网格线

![](http://pic2.zhimg.com/5c8861351672c291504ebbfefe409f9e_b.jpg)

最后添加一些图例即可

![](http://pic3.zhimg.com/b7223dbfc833cca2b70be4475eb93f7b_b.jpg)  
  
怎么样？相信你已体会到了如何将Excel的元素融入图表设计中。  
  
======================原回答=========================  
我曾在大三寒假闭关三周，自学Excel,
PowerPoint和Word，一年后又花了一个月的时间研习VBA。楼上关于函数和操作技巧已经分享很多了，我在这分享一些图表设计的技巧。  
  

一流的Excel函数和VBA水平，自然要以一流的图表设计呈现出来。

  

我相信看完这个回答后，你再也不会将图做成这样。

![](http://pic2.zhimg.com/1e18c630f9843e0fbe7dc9b6dd5e77e0_b.jpg)

好奇商业杂志上的这些高端大气的图是用什么特殊软件做出来的吗？

![](http://pic3.zhimg.com/e879dedf06688d97062ce9c944722c56_b.jpg)

答案就是Excel。

  

滑珠图、子弹图、瀑布图……一切都可以用Excel最基本的操作搞定。

![](http://pic3.zhimg.com/b49f624a8dfc75990dbc20315f54baab_b.jpg)  

我会先介绍一些设计的核心理念和方法，然后列举16个“商务范”图表制作实例，包含详细的制作步骤，最后分享一些配色方案。

  

==================================================================

_目录_

  

**一、商务图表制作核心理念和方法**

  1. 突破Excel的图表元素   

  2. 突破Excel的图表类型   

  3. 布局与细节 

**二、“商务范”图表制作实例**

  1. 柱状图横坐标以时间间隔比例分布   

  2. 簇状和堆积柱状图合用（Clustered & Stacked Column）   

  3. 漏斗图-利用辅助列占位   

  4. 自定义Y轴刻度间距   

  5. 含加粗边缘的面积图   

  6. 横网格线覆盖于Area图之上 
  7. 为Pie图加背景图片   

  8. 仪表盘   

  9. 多数量级的几组数据同时比较   

  10. 手风琴式折叠bar图   

  11. Water Fall瀑布图  

  12.不等宽柱形图  

  13.滑珠图  

  14. 动态图表1   

  15.动态图表2  

  16. Bullet图-竖直 

**三、配色方案**

  1. Nordri设计公司分享的配色方案   

  2. ExcelPro分享的方案 
**四、自学参考书目和资料**   
  
  

==================================================================

_正文_

  

**一、商务图表制作核心理念和方法**

  
(这一章节的笔记整理自刘万祥老师的博客 [ ExcelPro的图表博客 _ _ ](http://excelpro.blog.sohu.com/) )  
  

**1\. 突破Excel的图表元素**

不要仅用“图表”去做图表，而是用“图表＋所有Excel元素（如单元格）”去做图表。

![](http://pic1.zhimg.com/e113e24f4df3df43a77515c60a334c52_b.jpg)

左上图，只有B4单元格是图表区域，标题利用的是B2；B3－B5填充浅色，"index"和"data"分别在B3、B5。

右上图，B2为图表序号，C2为图表标题，填深绿色，B3为副标题，图例放在C4，图表在C5，B2到C5填充淡色，B6、C6合并填写注释。

![](http://pic4.zhimg.com/e90d6c7322949b0509d186d95e5c1dbf_b.jpg)

左上图，标题在C2－H2居中，图表在C3－H3，表格在C6－H8。

右上图，B2填红色装饰，标题和副标题分别在B2、B3，图表在D4－F4，数据来源在D5，标号2为矩形框，整个区域有边框。

  

经常用来配合图表制作的其他excel元素主要有单元格、文本框、线条、箭头等。

  * **单元格DIY图表标题**

上面四例都是

  * **单元格填色替代图表区和绘图区填色**   

将图表区和绘图区设置无色透明，将单元格设置相应的填充色（在我开头举的案例中有详尽的说明）

  * **单元格控制图表的大小和排列**   

将图表对齐在某个单元格（锚定，上面有说明），则可以通过调整单元格的列宽行高，方便地控制图表的大小。

选中图表区域，右键-设置图表区域格式，在属性中设置图表是否随单元格变而变。

当多个图表都锚定在某一列/行的单元格上时，就可精确实现图表的对齐，更可方便的批量快速的调整图表大小。

  * **单元格表格DIY数据表**
上面第三例  

  * **矩形框或线条绘图对象来DIY图例**   

  

**2\. 突破Excel的图表类型**   

![](http://pic2.zhimg.com/a002de8f2b35dda0d077cbb45c33740f_b.jpg)  

左上图，先用所有数据做曲线图或柱形图，然后选中相应的序列，更改图表类型，有时还需要用到次坐标轴。

右上图，先做好面积图，然后将该数据序列再次加入图表，修改新序列的图表类型为曲线图，调粗线型。

  

**3\. 布局与细节**

  

  * **布局**

下图从上到下可以分为5个部分： **主标题区、副标题区、图例图、绘图区、脚注区** 。

特点有： **完整的图表要素；突出的标题区；从上到下的阅读顺序** 。

**标题区** 非常突出，占到整个图表面积1/3以上，其中主标题用大号字和强烈对比效果，副标题提供详细信息。 

![](http://pic4.zhimg.com/2d66425a20b1f4313589fca8a2f15b39_b.jpg)

  * **竖向构图方式**   

整个图表外围高宽比例在2:1到1:1之间，图例一般在绘图区上部或融入绘图区里面

  * **使用更为简洁醒目的字体**   

商业图表多选用 **无衬线类字体**

图表和表格的数字中使用 **Arial** **字体、** **8~10** **磅大小，中文使用黑体**

  * **注意图表的细节处理**
1\. 脚注区写上数据来源  
2\. 图标注释：对于图表中需要特别说明的地方，如指标解释、数据口径、异常数据等，使用上标或*等进行标记，在脚注区说明  
3\. 坐标轴截断标识  
4\. 四舍五入：在脚注区写明：由于四舍五入，各数据之和可能不等于总额(或100%)  
5\. 简洁的坐标轴标签：如2003、’04、’05  
6\. 让Line图从y轴开始：双击x轴，Axis Options-最下-Position Axis-on tick marks  
7\. 作图数据的组织技巧: 原始数据不等于作图数据；作图前先数据排序；将数据分离为多个序列，每个序列单独格式化  
8\. 其他: 去除绘图区的外框线，去除纵坐标轴的线条色，将网格线使用淡灰色予以弱化，bar间距小于bar宽度，饼图分块用的白色线  

—————————————————————————————————————

  

**二、“商务范”图表制作实例**

（这一章节的16个案例均出自刘万祥老师的 [ Excel图表之道 (豆瓣) _ _
](http://book.douban.com/subject/4326057/) ，该书基于Excel2003）  
  
这一部分摘自我的笔记，当时用的是2010版本，虽说2013版本具体的操作方法变掉了，但制作的步骤是没变的。也就是说，如果你使用的是其他版本，“【】”里的操作
方法会不同，但“【”前面的步骤和思路是没有问题的。  
  
但对于新手来说可能参照起来有些困难，所以，如果有兴趣，我建议你阅读刘老师的这本深入浅出的书。集中时间和力量搞定公式、初步VBA、图表制作，受益是终生的。因为
工作离不开Excel，所以大多技巧只要掌握了，就不会忘。  
  
仪表盘、滑珠图、子弹图、瀑布图、动态图表我有自作的模板。需要的请留下邮箱。  
  
**1\. 柱状图横坐标以** **时间间隔比例分布**   

例如要展示利率（Y轴）随时间（X轴）的变化，通常情况下做出的是左下所示的样子，横坐标均匀分布，但如何做出右下图这样的以时间间隔比例分布的图呢？

![](http://pic1.zhimg.com/423fecb96d7ff77319db761801ddb293_b.jpg)

_原始数据与辅助列_

![](http://pic2.zhimg.com/998f4cb6d209486657bd06f531d3b5b1_b.jpg)

_绘制方法_

A2:B5做Column图（左下）发现横坐标不是希望的3、6、12、24

将横坐标转化成右下的样子【**选中图表** **-Chart Tools-Design-Select Data-HorizontalAxis
Label-Edit-A2:A5 ** 】

![](http://pic2.zhimg.com/db77e2e14592f11dba5b3b86b6ff90dc_b.jpg)

将横坐标转化为Date Axis（左下） **【双击横坐标** **\- Axis Options-Axis Type-Date Axis** **
】 ** 然后删去横坐标

  

选中C2:C5添加进图表 **【** **Ctrl+C Ctrl+V** **】**

（这里提示一下，很多地方用到了“将数据添加进已有图表”这一操作。操作方法是：选中需要添加的数据，Ctrl+C，然后选中图表，Ctrl+V）

  

将其转换为Line图 **【选中图表** **-Chart Tools-Format** -最左侧- **Series2** **
】【Chart Tools-Design-Change Chart Type-Line ** **】**

![](http://pic1.zhimg.com/99c1e80b2b36173b24a0931de03c54d7_b.jpg)

显示Line图标签 **【选中红线** **-Chart Tools-Layout-Data Labels-Below**
】单独修改这些0，看起来正是Column图标签，选中单个标签进行修改即可。

![](http://pic2.zhimg.com/2b00e5a00ee01a3b4afd069bc1b9f54f_b.jpg)  

**2\.** **簇状和堆积柱状图合用（Clustered & Stacked Column** **）**

_源数据_

![](http://pic3.zhimg.com/fa45b8d00e6eb9cd09e700c1ae41feb3_b.jpg)

_最终效果_  

![](http://pic4.zhimg.com/0d9a074f7948707b0fa38f5cc5e27124_b.jpg) _绘制方法_

利用错行和空行

![](http://pic1.zhimg.com/6b3d62536e899215fdb7ea22bd0ad7b5_b.jpg)

选中这些数据，直接做成 Stacked Column

  

**3\.** **漏斗图-** **利用辅助列占位**

_最终效果与源数据_  

![](http://pic2.zhimg.com/3f59e6ae6cd751fc291a8cb456330d2d_b.jpg)

_绘制方法_

添加辅助序列

确认前提是“指标列”从大到小排列  

假设<342>这个值在D3单元格，在C3中输入公式 =($D$3-D3)/2 然后拉到底。

![](http://pic2.zhimg.com/42c3ad27215a41346aa596eded3a78fd_b.jpg)

选中<公司1>这个单元格到<152>这个单元格区域，做Stacked Bar图

![](http://pic2.zhimg.com/f446dd893f4c9069c59b316e435e6f44_b.jpg)

反转纵坐标 **【双击纵轴** **-Axis Options-Category in reverse order** **】**

![](http://pic1.zhimg.com/48a5c8bd4a07ecb30bea89edf37fa95a_b.jpg)

将红色Bar隐藏 **【右击红色** **bar-Format Data Series-Fill-No Fill** **】**

  

**4\.** **自定义Y** **轴刻度间距**

以股价随时间变化为例，重要的是涨跌幅度，且幅度很大，我们希望Y轴间距可以自己设定，这里我们实现对数坐标。  

_最终效果与源数据_  

![](http://pic3.zhimg.com/2919473ff2fd6fc580711fd0221b38f5_b.jpg)
![](http://pic2.zhimg.com/c3ecee5d1e9c94ee06a18135e3cbfbd4_b.jpg) _绘制方法_

上图，C列为B列对数 =log10(Number) ， F列为我们希望的Y轴刻度，G列为F列取对数。即F列是B列的刻度，而G列是F列的刻度  

先用C2:C12列Line图（下左）

加入G2:G7（下中） **【** **Ctrl+C Ctrl+V** **】**

将红色Line改为Scatter图（下右） **【选中红色** ** Line-Chart Tools-Design-Change Chart
Type-Scatter ** **】**

![](http://pic1.zhimg.com/f4237cb09cacc5e18fbddc7b6a6c21ed_b.jpg)

更改红线横纵轴分别为E2:E7、G2:G7 **【选中图表-Chart Tools-Design-Select data-Series2-Edit**
**】**

让Y轴从1开始 **【双击纵轴** **-Axis Options-Minimum** **设置】** 并删去网线，删去纵轴

让曲线与Y轴相交（左下） **【双击横轴** **-Axis Options-** ** 最下Position Axis-On tick Marks
** **】**

采用误差线的方法添加横网线（右下）

**【选中红线-Chart Tools- Layout-Error Bars-** **最下More Error Bars Options-Close** **】** 此时图表中出现横纵误差线 

在图表选中竖向误差线，删除

设置横向误差线 **【右击横向误差线** ** -Format Error Bars-Horizontal Error Bars-Direction-
Plus **

**-Error Amount-Fixed Value -10** **】**

将红点变小 **【右击红线** **-Format Data Series-Marker Options** **】**

为红点标上数据 **【选中红线** **-Chart Tools-Layout-Data Labels-Left** **】**

依次选中各个标签，更改为Y列数值

![](http://pic2.zhimg.com/7674971d6bee154012a1c16d437e9543_b.jpg)  

**5\. 含加粗边缘** **面积图**

_最终效果与源数据_

![](http://pic4.zhimg.com/3f17acf670ee130b972adb35559a8d21_b.jpg)

_绘制方法_

选中数据做Line图（左下）

再将数据添入图表中 **【** **Ctrl+C Ctrl+V** **】** （右下）

![](http://pic4.zhimg.com/f317ea1ebc87b48854210b90ec1efac1_b.jpg)

更改红线为Area图 **【选中红线** **-Chart Tools-Design-Change Chart Type-Area** ** 】
**

![](http://pic1.zhimg.com/41150ca07051bf8c64c41da9260e1d9f_b.jpg)

去除Area图Border（否则无法自由修改Line颜色） ** 【右击红色Area-Format Data Series- Border Color-No
Line ** **】**

设置两者颜色

  

让Area图从Y轴开始 **【双击横轴** **-Axis Options-** ** 最下-Position Axis-On Tick Marks
** **】**

**注意：最开始要做两个line图，而不能两个area图**   

  
下面这个图是我做的~ ![](http://pic2.zhimg.com/465f29383a03f38e29b0cb337cd8c370_b.jpg)  

**6\.** **横网格线覆盖于Area** **图之上**

_最终效果_

![](http://pic4.zhimg.com/12fb1e14c32e57e05b5ad25727ac2c76_b.jpg)

_绘制方法_

正常做完一个图后，将第一张图锚定，复制粘贴得到另一个一样的图

![](http://pic4.zhimg.com/00e7626866e2238265334a299c4bc4e5_b.jpg)

第二张图Chart area、Plot Area及柱子设为No fill （即只保留Gridline）

将第一张图的Gridline删去

按住Alt移动第二张图覆盖于第一张图之上

可选中Gridline右击，在Format Gridline里改其颜色、粗细

![](http://pic2.zhimg.com/0aa14b6bc2f4c70987c411f9147df88b_b.jpg)  

**7\. 为Pie** **图加背景图片**

_最终效果与原始数据_  

_ ![](http://pic3.zhimg.com/acd054d55248ec5fc00963b9b8b71b8c_b.jpg)绘制方法_

先用A1:A5做Pie图，得到下图，此系列数据为Series1

![](http://pic3.zhimg.com/660656cddf827be02074b272ab89d440_b.jpg)

选中任意一个单元格（如A3）添入 **【** **Ctrl+C -Paste-Paste Special-New Series** **】**

此时无法看到也无法选择该Series （为Series2），看到的仍然是上图的样子

将Series1改为次坐标轴 **【选中大饼右键** ** -Format Data Series-Series Options-Plot Series
on-Secondary Axis ** 】

（此时在Chart Tools-Format里就可选择Series1或series2）

将Series1设为无填充 **【右击大饼** **-Chart Tools-Formatdata Series-Fill-No Fill **
**】**

（此时看到的正是Series2，如下图）

![](http://pic1.zhimg.com/acb815562efc8922d05b1dc1dfd2e692_b.jpg)

将Series2填充自定义图片 **【选中图表** **-Chart Tools-Format-** **最左边-** **
下拉框Series2- **

\- **Format Selection-Fill-Picture** **】**

将Series1切割处改为白色 **【选中图表** **-Chart Tools-Format-** **最左边-** **
下拉框Series1- **

\- **Format Selection-Border Color** 】

  

**//另一个办法//**

在PPT里画一个圆形，Shape Fill一个图片，去掉Outline，得到一个圆形图片，另存。直接画Pie图，在Plot Area
（下图所示，正方形和Pie图直接的白色区域）右击 **Format Plot Area-Fill-Picture** 即可

![](http://pic2.zhimg.com/fdb5f2c48a03379f32d0f1515f9845f1_b.jpg)  

**8\. 仪表盘**   

_最终效果_  

_(在某个单元格中输入数值（0-100），红色的指针会随之而动)_

_ ![](http://pic2.zhimg.com/2f917b1eae7c5bd1f4ef8e1027465001_b.jpg)绘制方法_

E2 =D2/D4*270 E4 =360-E2 用E2:E4作图，得指针图（Series1，左下）

将A2:A24添入 **【** **Ctrl+C-** **选中图- Paste Special-New Series** **】**
得到仪表图（Series2，右下，目前看不到）

![](http://pic3.zhimg.com/07be62682ce93b68fa05130f62bdb33b_b.jpg)

将Series1转为次坐标轴并爆炸、旋转 **【选中右击** ** -Foramt data series-Series Options-Plot
Series on-Secondary Axis **

**-Pie explosion-20**

\- **Angle of first Slice-225** **】**

先鼠标拖动红色的尖到圆心，然后将蓝色和绿色的拖到中心

蓝色、绿色slice设为白色，红色slice换为好看的红色 **【单独选中右击** ** -Format Data Point-Fill-Solid
Fill ** **】**

E3单元格调节为2

![](http://pic1.zhimg.com/5524935f262fa25a005227622c77812e_b.jpg)
将Series2旋转、变颜色 **【** ** Format data series-Series Options- Angle of first
Slice-225 **

\- **Fill-Solid fill-White**

\- **Border Color-Border line-Black** **】**

![](http://pic1.zhimg.com/d370a077ce553fd4446f08f8b28e887f_b.jpg)

加刻度 **【选中** **Series2-Layout-Labels-Data labels-outside end** **】**

将27删除，0依次改为10、20……

仪表盘上加显示器 **【插入单元格，选中单元格，在公式编辑栏输入** **=$D$2** **回车】**

![](http://pic4.zhimg.com/3e06d421948d62a8eee2325efb8c51a7_b.jpg)

随后可调节颜色

选中仪表图（Series2），在公式编辑栏末尾单击一下，按F9，回车。图表便不再依赖于A列数据。

  

**9\. 多数量级的几组数据同时比较**   

_最终效果_

_![](http://pic2.zhimg.com/0040f7166ac3e5d9d72cb5291092563d_b.jpg) 原始数据与处理数据
_

![](http://pic4.zhimg.com/4ed159c43143f219f7a90362c985d2d8_b.jpg)

_绘制方法_

F3单元格 =B3/MAX($B$3:$B$8)*0.8 即将用户数最大值基准转化为0.8

G3单元格=1-F3 为占位列

后几列公式类似

F3:J8作Stacked Bar图（左下）

红色、紫色为占位列，设为白色（右下） **【选中右击** **-Format Data Series-Fill** **】**

（如果基准为1 则最大值会和下一条接壤）

![](http://pic3.zhimg.com/782868f5e53db48c56ca70d2652b3087_b.jpg)  

**10\. 手风琴式折叠bar图**   

_最终效果_  

_（突出前三个和后三个）_

![](http://pic1.zhimg.com/2c8d4e89d52abeb3e0ef005bc6643cf9_b.jpg)

_原始数据（左下）和作图数据（右下）_

第一列 ：前三、空格、后三单元格数做成1:1:1  

第二列：中间的数据若有6个，则前后各留5个

两列首行要对齐

![](http://pic1.zhimg.com/c8155d83b1653e649874919b2500b1d4_b.jpg)

_绘制方法_

以作图数据第一列做Stacked Bar图，第二列复制粘贴进去（红色，左下图）

将红条改为次坐标轴（右下图） **【选中红色右击** ** -Format Data Series-Plot Data on-Secondary
Axis ** **】**

注意上下两个轴，一个是Primary axis一个是Secondary axis，将Maximum调为一样

![](http://pic3.zhimg.com/a854a915d7cf39b80e29ed12f9cb3949_b.jpg)

将次坐标轴在右边显示出来 **【选中图表** ** -Layout-Axes-Secondary Vertical Axis-Show right to
left Axis ** **】**

![](http://pic2.zhimg.com/810f94ba9dce96503eb16a58ea446a9f_b.jpg)

将左边主坐标轴反转 **【双击** **-Axis Options-Category in reverse order** **】**

删去横竖两个Secondary Axis

![](http://pic4.zhimg.com/900f53a91d680c6277564e7c3be6e713_b.jpg)  

**11\. Water Fall** **瀑布图**

_最终效果_  

![](http://pic2.zhimg.com/84a8e726f65d26326328a76ec7d19270_b.jpg)

_绘制方法_

D4 =SUM($B$3:B4) F4 =IF(B4<0,D4,D3) G4 =IF(B4>=0,B4,0)

H4 =IF(B4>=0,0,ABS(B4))

![](http://pic4.zhimg.com/886fc97af1757220ded76db582076be1_b.jpg)

用蓝色框线区域作图。如果要添加横线。可将“累计”列贴入到图表，改为Scatter图，添加Error Bars

![](http://pic1.zhimg.com/6295c288d57e30773c36976a0e24e8fa_b.jpg)

**12\.** **不等宽柱形图**

_最终效果与原始数据_  

_（_ 高度反映ARPU值，宽度反映用户规模）

![](http://pic2.zhimg.com/535ae0b799326b0ad52ee3d07f131fb9_b.jpg)

_绘制方法_

**//分组细分法-Column图//**

处理数据如下。每个ARPU数据重复次数为“用户规模”（柱子宽度）数

![](http://pic3.zhimg.com/015d27cbc20a6a9daf6a535966715c26_b.jpg)

第二~五列作图 （左下） 修改宽度和间距 **【选中右击** ** -Format data series-Series Options-Series
Overlap-100 **

**-Gap** **Width-0** **】**

![](http://pic4.zhimg.com/59c6317c02ff746ba73e5ab52aee94a7_b.jpg)

**//时间刻度法-Area图//**

原始数据依旧（左下图）

作图数据（右下图）

第一列最大值20（8+4+2+6）。第一列的数据对应于“用户规模”（每个柱子宽度）。除0和20外 ，其他每个数据固定为3个（无论如何都是3个）

注意其他几列数字位置

![](http://pic3.zhimg.com/e401a9a9d08ffdfb83f0ca23952c528f_b.jpg)

以第一~五列作Area图

![](http://pic2.zhimg.com/20b419fd2414821ead3a4ffe631d0be8_b.jpg)

横轴改为需要的 **【选中图表** **-Chart Tools-Design-Select Data-Horizontal** **
改为A9:A19 ** **】**

删去图中无关的深蓝色图形

横轴改为时间刻度（左下）**【选中横坐标右击** **-Format Axis-Axis Type-Date Axis** **】**

柱子外框设为白色，粗一点（右下）

![](http://pic2.zhimg.com/db6c0af64fcb3cdc0054924c4a2028e0_b.jpg)  

**13\.** **滑珠图**

_最终效果（右图是我仿照原图画的） _  

蓝色奥巴马支持率，红色麦凯恩支持率。纵坐标为不同人群

两种滑珠为Scatter图，横梁为Bar图

![](http://pic3.zhimg.com/464a7f89b97f8a339a60c7a6c9df788c_b.jpg)

_绘制方法_

数据（左下） E列为Scatter图Y轴数据。以A、D列作Clustered Bar图，纵轴Category in reverse order

![](http://pic4.zhimg.com/ed7f1133e3c2538f76cd66d73476fce9_b.jpg)

贴入B列，改为Scatter图（左下），选中红点，Select data-X轴改为B列，Y轴改为E列

同样方法添加C列并处理

![](http://pic1.zhimg.com/f1fac26bedadf7f993b3094dc7429ee1_b.jpg)  

**14\. 动态图表1**   

  

**File-Options-Customize Ribbon** -右边框内勾选 **Developer** 这样面板就有Developer栏，单击 **Developer-Controls-Insert** -第一排第五个 **List Box** 添加到工作表中 

  

右击该List Box， **Format Control-Input range** $B$8:$B$13

**Cell link** $B$5 

B5就会显示在List Box里选择了第几个数值

  

B3单元格 =INDEX(B8:B13,$B$5) 横向拉到N3

这样当在List Box里选择时，B5单元格显示选择结果，B3:N3就会跟着显示选择结果对应各月的数值

以B3:N3作图

![](http://pic4.zhimg.com/2622f94b738b16c620ceba85bde512d3_b.jpg)  

**15\.** **动态图表2**

以下图为例。B5设置Data Validation 只可选择07年、08年或09年。

B7单元格 =CHOOSE(IF(B5="08年",2,IF(B5="07年",1,3)),1,2,3)

B8单元格 =INDEX(B1:B3,$B$7) 拉到F8

![](http://pic2.zhimg.com/bcf28612774f3d8ee0c3be8296c1a573_b.jpg)

先以B1:F3作Line图，选择B8:F8 Ctrl+C Ctrl+V到图表中即可

![](http://pic1.zhimg.com/96b66e228ebb9ef3aa9e8c0d15d8be3c_b.jpg)
![](http://pic4.zhimg.com/7b331f9a69ae449c9cb42131f59c5512_b.jpg)  

**16\. Bullet** **图-** **竖直**

_最终效果与原始数据 _  

_ ![](http://pic2.zhimg.com/e032d9b299aad6a55cf0b9ab17cd046e_b.jpg)绘制方法_

以A2:F6做Stacked Column图（左下），Swith Row/Column（右下）

![](http://pic3.zhimg.com/e2066ec0ca234a0570791ea00c38c98e_b.jpg)

更改最下蓝色柱子（实际）为次坐标轴并变窄(左下) ** 【右击蓝柱-Format Data Series-Series Options-Secondary
Axis **

**-GapWith-300 ** **】**

更改最下红色柱子（目标）为次坐标轴（右下） **【右击红柱** ** -Format Data Series-Series Options-
Secondary Axis ** **】**

更改红柱为Line图 **【选中红柱** **-Chart Tools-Design-Change Chart Type** **】**

![](http://pic4.zhimg.com/2a8651f56d1669843b21f885e5ea8372_b.jpg)

去掉红色连线并将方块改为红短线 **【选中红线右击** **-Format Data Series-Line Color-No Line**

**-Marker Option-** **横线】**

然后设置其他颜色等

![](http://pic4.zhimg.com/363afc369d4d363d729129efd882764f_b.jpg)  

—————————————————————————————————————  

**三、配色方案**

  
配色主题设置方法 （以Excel2013做示范，其他版本大同小异）  
  
Step1. <页面布局 - 颜色- 自定义颜色>  
![](http://pic4.zhimg.com/f70fe0653f679e7e2609e760c47a43d3_b.jpg)  
Step2. 总共12个颜色可自定义，单击任意一个颜色下拉菜单，选择“其他颜色”，输入RGB值，全部完后命名，保存即可。这样，在<页面布局 -
颜色>下拉菜单中就可以选择自定义的主题。  
  
![](http://pic1.zhimg.com/d2c9eba2b964d5366020ee4ab0027807_b.jpg)  
  
以下每个配色方案都提供了这12种颜色的RGB值  
  

**1\. Nordri设计公司分享的配色方案**

[ Nordri 商业演示设计 _ _ ](http://www.nordridesign.com/)  

1-碧海蓝天  

![](http://pic3.zhimg.com/8b2b37e5770466cf412031f60524f39c_b.jpg)  
![](http://pic4.zhimg.com/d00521cf25628bd1599a8ac5d89641c8_b.jpg)  

2-达芬奇的左手  

![](http://pic2.zhimg.com/4bf163b526d63c35ec5bf07e97ae7ace_b.jpg)  
![](http://pic1.zhimg.com/0e08bb9de75de1e68a4892cfd0a4225f_b.jpg)  

3-老男孩也有春天  

![](http://pic4.zhimg.com/2440404f663123a65371b3d1b78ef75f_b.jpg)  
![](http://pic1.zhimg.com/f654180396adee5a1a8d77426a2452b4_b.jpg)  

4-路人甲的秘密  

![](http://pic3.zhimg.com/84cdc48f1506b4d675471907dea608fc_b.jpg)  
![](http://pic4.zhimg.com/0460af4177f026c38b8c6ba783e689e4_b.jpg)  

5-旅人的脚步  

![](http://pic4.zhimg.com/119635873714daa91ac6195f38b04904_b.jpg)  
![](http://pic1.zhimg.com/ceee04e9bc073ea728505a89bf77661b_b.jpg)  

6-那拉提草原的天空  

![](http://pic1.zhimg.com/8da0e9175b4da0e7d186a18b2241f270_b.jpg)  
![](http://pic4.zhimg.com/76786838cd867e7e15552693385ca876_b.jpg)  

7-香柠青草  

![](http://pic2.zhimg.com/b485dc83f9da52f310f6c599af2f72cc_b.jpg)  
![](http://pic4.zhimg.com/f33375de6a7ad3b2ce7de333f3af72c2_b.jpg)  

8-热季风  

![](http://pic2.zhimg.com/8257f69a70d9ff4c66df9df772fe20ea_b.jpg)  
![](http://pic4.zhimg.com/31862a7483f906fb181c3f9f612f75de_b.jpg)  

9-软件人生  

![](http://pic1.zhimg.com/af8bd59fa1447a6b891d4ab9b76af049_b.jpg)  
![](http://pic3.zhimg.com/122237490e332436bae7e4214720f322_b.jpg)  

10-商务素雅  

![](http://pic1.zhimg.com/f3c48aac3789fa7753b85a54a390c3f8_b.jpg)  
![](http://pic4.zhimg.com/c07f952ca62786267520d1da920542e3_b.jpg)  

11-商务现代  

![](http://pic3.zhimg.com/77a4f5e96d8bfe6f14227e1f6636130f_b.jpg)  
![](http://pic2.zhimg.com/a7e51f6cde5b5575da5a519cc4df624c_b.jpg)  

12-数据时代

![](http://pic4.zhimg.com/1d4f6f5e1b7243d1c04c36c157043ecf_b.jpg)  
![](http://pic2.zhimg.com/5acce1fbbfc93a4526a03f79ee0204e9_b.jpg)  

13-素食主义

![](http://pic2.zhimg.com/d54cfcea4a89607cb0f8776abaad67ec_b.jpg)  
![](http://pic4.zhimg.com/fa398feb6aa01cbd5d9ada152d85204d_b.jpg)  

14-岁月经典红  

![](http://pic2.zhimg.com/0403cef745259232668cf0eae97af957_b.jpg)  
![](http://pic3.zhimg.com/dd97ff240e402e225812e26fe521b40f_b.jpg)  

15-夏日嬷嬷茶  

![](http://pic1.zhimg.com/ac90979e715795db32e89a97b63703d1_b.jpg)  
![](http://pic1.zhimg.com/7c93dffebbfd9e30550dd7eab78b921d_b.jpg)  

16-邮递员的假期  

![](http://pic4.zhimg.com/0951bb0d2bd4c53c48841552fbb58206_b.jpg)  
![](http://pic4.zhimg.com/0fa014719f08c4e0ba16dcce0163342b_b.jpg)  

17-毡房里的夏天夏天  

![](http://pic1.zhimg.com/5e8cc8c4d881a182b7dbdb0f36c3feb5_b.jpg)  
![](http://pic1.zhimg.com/5198d01b2a461d86512acb7f822b85d3_b.jpg)  
  

**2\.ExcelPro分享的方案 **

![](http://pic1.zhimg.com/cc401d89c2ce168f69db27f1b9e43228_b.jpg)
![](http://pic2.zhimg.com/5b605d0ab46b4d91bc335070fc3a125a_b.jpg)
![](http://pic1.zhimg.com/f059d68233edf552b3ccf54f7e176374_b.jpg)
![](http://pic1.zhimg.com/c29c625ab69ed935d9012455a04926e7_b.jpg)
![](http://pic4.zhimg.com/8bbd3af5579b78dc2b43d03ba4882df5_b.jpg)
![](http://pic3.zhimg.com/17379a8213cd369b6435d58dcb00ee71_b.jpg)  

**四、自学参考书目和资料**

[ ExcelPro的图表博客 _ _ ](http://excelpro.blog.sohu.com/)  

[ Excel图表之道 (豆瓣) _ _ ](http://book.douban.com/subject/4326057/)  

[ Nordri 商业演示设计 _ _ ](http://www.nordridesign.com/)  

[ 用地图说话 (豆瓣) _ _ ](http://book.douban.com/subject/10435804/)  

[ 演说之禅 (豆瓣) _ _ ](http://book.douban.com/subject/3313363/)  

[ 说服力 让你的PPT会说话 (豆瓣) _ _ ](http://book.douban.com/subject/4604592/)  

[ 别怕，Excel VBA其实很简单 (豆瓣) _ _ ](http://book.douban.com/subject/19952184/)

#### 原链接: http://www.zhihu.com/question/21758700/answer/34705774