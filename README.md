# Genshin-Roll-Call-Simulator
A custom card drawing simulator based on pygame.基于pygame的自定义抽卡模拟器

------

### **实现原理：**

没啥技术含量，单纯的用pygame为基础，然后添加几个按钮，并且被bg盖住，然后按钮按下播放视频。

就这么点……

注：素材来源于游戏《Genshin Impact》，仅做学习参考使用

------

### **使用方法（保姆级教程）：**

**1.在右上角code中，选择“Download ZIP”**

![image-20240119001550882](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119001550882.png)

**2.将其解压，并放到一个随便创建的文件夹里，或者你自己命一个有意义的名字的文件夹。**

~~*不会解压的去问问百度罢！*~~

**3.下载python：[Download Python | Python.org](https://www.python.org/downloads/)**

![image-20240119001929799](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119001929799.png)

点击“Download Python x.xx.x”，下载后安装就行啦！

==*已经安装python 的可以跳过这一步~*==

​				★★★★★★★★★★★★★★★★★★

**另外，我们还需要安装Adobe Premiere Pro 2021（最好是2021版本的）**

​				★★★★★★★★★★★★★★★★★★

*~~这个的话，大家自行搜索（可以去B站找找怎么下载和安装，这里就不过多赘述）~~*

==*已经安装Premiere的可以跳过这一步~*==

**4.打开cmd命令窗口（win键+R，并输入cmd，点击允许）安装依赖**

输入pip install pygame，然后点击回车，等待安装……

![image-20240119002453115](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119002453115.png)

![image-20240119002510322](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119002510322.png)

**5.右键“main.py”，找到"Edit with IDLE"**

![image-20240119002138829](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119002138829.png)

~~当然，你可以选择你喜欢的版本，我自己nt安了俩~~

**6.找到函数def r()**

![image-20240119002625581](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119002625581.png)

现在可以看到您应该修改的部分了。接下来才是重点中的重点！

**7.制作出金视频**

打开video，找到 “GenshinImpact.prproj” 文件

*注：Premiere俗称Pr*

使用Pr打开它，可以看到如下界面：

![image-20240119003213058](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119003213058.png)

（如果有**“脱机现象”**，请您手动将show.mp4定位在video中文件夹中的show.mp4）

双击**"字幕02"**，接下来就可以自己改名字了

![image-20240119003359443](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119003359443.png)

单击show**（不是show.mp4！！！）**，然后左上角-文件-导出-媒体，可以看到如下界面：

![image-20240119003554831](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240119003554831.png)

**单击右上角”输出名称“**可以来改名字和位置，位置一定要放在/video/show/里面！！！然后点击导出即可。



**8.修改程序**★★★

找到刚刚的“def r()”的地方

*修改范例：*

```python
def r():
    tmp = random.randint(1, 55)#这个是随机数，有多少个人，第二个参数就填多少
    if tmp == 1:
        clip2 = VideoFileClip(r'./video/show/cjb.mp4')
    elif tmp == 2:
        clip2 = VideoFileClip(r'./video/show/ckx.mp4')#多余的可以删掉
    ...
    return clip2#这个不要删，如果你学过对象编程，你应该知道它的重要性
```

假如我前面输出了一个视频，名字叫“cxk.mp4”和“jmr.mp4”，则可以改成：

```python
def r():
    tmp = random.randint(1, 2)#<----就两个人，所以这里填2，有几个人填几好嘛？！
    if tmp == 1:
        clip2 = VideoFileClip(r'./video/show/ckx.mp4')
    elif tmp == 2:
        clip2 = VideoFileClip(r'./video/show/jmr.mp4')
    
	return clip2
```

**9.双击运行**

接下来关闭文件，双击“main.py”即可运行！
