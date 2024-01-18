import pygame, sys  # sys是python的标准库，提供Python运行时环境变量的操控
from pygame.locals import *
from moviepy.editor import *
import time
import random

# 设置icon
# icon = pygame.image.load('E:\AS-workspace\pygameTest\drawable\icon.png').convert_alpha()
# pygame.display.set_icon(icon)

FPS = 30


def r():
    tmp = random.randint(1, 55)
    if tmp == 1:
        clip2 = VideoFileClip(r'./video/show/cjb.mp4')
    elif tmp == 2:
        clip2 = VideoFileClip(r'./video/show/ckx.mp4')
    elif tmp == 3:
        clip2 = VideoFileClip(r'./video/show/cwk.mp4')
    elif tmp == 4:
        clip2 = VideoFileClip(r'./video/show/cyz.mp4')
    elif tmp == 5:
        clip2 = VideoFileClip(r'./video/show/cyz2.mp4')
    elif tmp == 6:
        clip2 = VideoFileClip(r'./video/show/dsw.mp4')
    elif tmp == 7:
        clip2 = VideoFileClip(r'./video/show/fhz.mp4')
    elif tmp == 8:
        clip2 = VideoFileClip(r'./video/show/gjn.mp4')
    elif tmp == 9:
        clip2 = VideoFileClip(r'./video/show/gwt.mp4')
    elif tmp == 10:
        clip2 = VideoFileClip(r'./video/show/jjy.mp4')
    elif tmp == 11:
        clip2 = VideoFileClip(r'./video/show/jzq.mp4')
    elif tmp == 12:
        clip2 = VideoFileClip(r'./video/show/kgh.mp4')
    elif tmp == 13:
        clip2 = VideoFileClip(r'./video/show/khs.mp4')
    elif tmp == 14:
        clip2 = VideoFileClip(r'./video/show/kht.mp4')
    elif tmp == 15:
        clip2 = VideoFileClip(r'./video/show/khz.mp4')
    elif tmp == 16:
        clip2 = VideoFileClip(r'./video/show/klq.mp4')
    elif tmp == 17:
        clip2 = VideoFileClip(r'./video/show/ks.mp4')
    elif tmp == 18:
        clip2 = VideoFileClip(r'./video/show/kyf.mp4')
    elif tmp == 19:
        clip2 = VideoFileClip(r'./video/show/kyh.mp4')
    elif tmp == 20:
        clip2 = VideoFileClip(r'./video/show/kyq.mp4')
    elif tmp == 21:
        clip2 = VideoFileClip(r'./video/show/lcy.mp4')
    elif tmp == 22:
        clip2 = VideoFileClip(r'./video/show/lhn.mp4')
    elif tmp == 23:
        clip2 = VideoFileClip(r'./video/show/ljc.mp4')
    elif tmp == 24:
        clip2 = VideoFileClip(r'./video/show/ljy.mp4')
    elif tmp == 25:
        clip2 = VideoFileClip(r'./video/show/lmj.mp4')
    elif tmp == 26:
        clip2 = VideoFileClip(r'./video/show/lwh.mp4')
    elif tmp == 27:
        clip2 = VideoFileClip(r'./video/show/lwk.mp4')
    elif tmp == 28:
        clip2 = VideoFileClip(r'./video/show/lzh.mp4')
    elif tmp == 29:
        clip2 = VideoFileClip(r'./video/show/lzj.mp4')
    elif tmp == 30:
        clip2 = VideoFileClip(r'./video/show/mjc.mp4')
    elif tmp == 31:
        clip2 = VideoFileClip(r'./video/show/mq.mp4')
    elif tmp == 32:
        clip2 = VideoFileClip(r'./video/show/nlp.mp4')
    elif tmp == 33:
        clip2 = VideoFileClip(r'./video/show/qzy.mp4')
    elif tmp == 34:
        clip2 = VideoFileClip(r'./video/show/smh.mp4')
    elif tmp == 35:
        clip2 = VideoFileClip(r'./video/show/syc.mp4')
    elif tmp == 36:
        clip2 = VideoFileClip(r'./video/show/syf.mp4')
    elif tmp == 37:
        clip2 = VideoFileClip(r'./video/show/syy.mp4')
    elif tmp == 38:
        clip2 = VideoFileClip(r'./video/show/szr.mp4')
    elif tmp == 39:
        clip2 = VideoFileClip(r'./video/show/tmx.mp4')
    elif tmp == 40:
        clip2 = VideoFileClip(r'./video/show/wst.mp4')
    elif tmp == 41:
        clip2 = VideoFileClip(r'./video/show/wwb.mp4')
    elif tmp == 42:
        clip2 = VideoFileClip(r'./video/show/wxl.mp4')
    elif tmp == 43:
        clip2 = VideoFileClip(r'./video/show/xxq.mp4')
    elif tmp == 44:
        clip2 = VideoFileClip(r'./video/show/xxx.mp4')
    elif tmp == 45:
        clip2 = VideoFileClip(r'./video/show/ykh.mp4')
    elif tmp == 46:
        clip2 = VideoFileClip(r'./video/show/yrt.mp4')
    elif tmp == 47:
        clip2 = VideoFileClip(r'./video/show/zad.mp4')
    elif tmp == 48:
        clip2 = VideoFileClip(r'./video/show/zhj.mp4')
    elif tmp == 49:
        clip2 = VideoFileClip(r'./video/show/zqh.mp4')
    elif tmp == 50:
        clip2 = VideoFileClip(r'./video/show/zr.mp4')
    elif tmp == 51:
        clip2 = VideoFileClip(r'./video/show/zwx.mp4')
    elif tmp == 52:
        clip2 = VideoFileClip(r'./video/show/zzq.mp4')
    elif tmp == 53:
        clip2 = VideoFileClip(r'./video/show/zzt.mp4')
    elif tmp == 54:
        clip2 = VideoFileClip(r'./video/show/kjq.mp4')
    elif tmp == 55:
        clip2 = VideoFileClip(r'./video/show/zwy.mp4')
    return clip2


pygame.init()  # 内部各功能模块进行初始化创建及变量设置，默认调用
size = width, height = 1920, 1080  # 设置游戏窗口大小，分别是宽度和高度

screen = pygame.display.set_mode(size)  # 初始化显示窗口
pygame.display.set_caption("小游戏程序")  # 设置显示窗口的标题内容，是一个字符串类型
background = pygame.image.load(r"picture/bg.png")  # 图片位置

# 设置按钮的属性
x, y = 1520, 980
width1, height1 = 150, 50
button_rect = pygame.Rect(x, y, width1, height1)
button_color = (255, 255, 255)
text_color = (0, 0, 0)
button_font = pygame.font.SysFont('arial.ttf', 20)
button_text = button_font.render("Button", True, text_color)

# 设置按钮的属性
x2, y2 = 1816, 32
width2, height2 = 50, 50
button2_rect = pygame.Rect(x2, y2, width2, height2)
button2_color = (255, 255, 255)
text2_color = (0, 0, 0)
button2_font = pygame.font.SysFont('arial.ttf', 20)
button2_text = button_font.render("Button", True, text2_color)

# 设置视频
# clip2 = VideoFileClip(r'./video/show/ckx.mp4')

running = True

while running:  # 无限循环，直到Python运行时退出结束
    # 绘制按钮
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text,
                (button_rect.centerx - button_text.get_width() / 2, button_rect.centery - button_text.get_height() / 2))
    pygame.draw.rect(screen, button2_color, button2_rect)
    screen.blit(button2_text, (
        button2_rect.centerx - button2_text.get_width() / 2, button2_rect.centery - button2_text.get_height() / 2))

    screen.fill((0, 0, 0))  # 清空屏幕
    screen.blit(background, (0, 0))  # 对齐的坐标

    for event in pygame.event.get():  # 从Pygame的事件队列中取出事件，并从队列中删除该事件
        if event.type == pygame.QUIT:  # 获得事件类型，并逐类响应
            pygame.quit()
            sys.exit()  # 用于退出结束游戏并退出
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                clip1 = VideoFileClip(r'./video/抽卡素材/单抽出金~1.mp4')
                clip3 = r()
                clip4 = r()
                clip5 = r()
                clip6 = r()
                # 在这里执行按钮点击后的操作
                clip1.preview(fps=30)
                clip1.close()
                # 设置显示的文字
                clip3.preview(fps=30)
                clip3.close()
                while 1:
                    if event.type == MOUSEBUTTONDOWN:
                        break
                clip4.preview(fps=30)
                clip4.close()
                while 1:
                    if event.type == MOUSEBUTTONDOWN:
                        break
                clip5.preview(fps=30)
                clip5.close()
                while 1:
                    if event.type == MOUSEBUTTONDOWN:
                        break
                clip6.preview(fps=30)
                clip6.close()
                while 1:
                    if event.type == MOUSEBUTTONDOWN:
                        break


            if button2_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()  # 用于退出结束游戏并退出
                running = False

    pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
