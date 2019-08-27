import threading
import datetime
import itchat
import time
from itchat.content import *

itchat.auto_login() #登陆
print('\n')
print('\n')
print('测试脚本完全免费，版权归Brick Republic所有，\n请勿用作商业用途，违者必究！\n请关注微信公众号：Brick Republic，你的中文抢购群组！')


def YeezyCity(city, username):
    while datetime.datetime.now() < d_time:
        s = time.asctime()
        print(s[11:19], end="")
        time.sleep(0.05)
        print("\r", end="", flush=True)
    itchat.send_msg('YEEZY' + city, toUserName=username)

if len(itchat.search_mps(name='Brick Republic')) != 0:
    print('\n')
    print('\n')
    city = input("请输入城市：")
    while True:
        try:
            use_time = input("请输入预约时间，例如：15:00：")
            d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + str(use_time), '%Y-%m-%d%H:%M')
            break
        except ValueError:
            print('时间格式错误！请使用半角 : ')
    while True:
        idnum = input("请输入18位身份证：") #18位
        if len(idnum) == 18:
            break
        print("长度不对请检查后重新输入")
    while True:
        phnum = input("请输入11位电话号码：") #11位
        if len(phnum) == 11:
            break
        print("长度不对请检查后重新输入")
    while True:
        size = input("请输入一个尺码字母注大小写：") #18位
        if len(size) == 1:
            break
        print("长度不对请检查后重新输入")
    threading.Thread(target=YeezyCity,
                     args=(city, itchat.search_mps(name="adidasOriginals")[0]['UserName'])).start()
    @itchat.msg_register(TEXT, isMpChat=True)
    def text_reply(msg):
        try:
            rtext = ''
            for i in msg['Content'].split("例如：")[1].split("\n")[0].split("，"):
                if len(i) == 18:
                    rtext = rtext + idnum + "，"
                elif len(i) == 11:
                    rtext = rtext + phnum + "，"
                elif len(i) == 1:
                    rtext = rtext + size + "，"
                else:
                    rtext = rtext + i + "，"
            # info=msg['Content'].split("\n")[1].split("\n")[0].replace("身份证号",str(idnum)).replace("尺码代码",str(size)).replace("手机号",str(phone))
            if "例如：" in msg['Content']:
                msg.user.send(rtext.rstrip("，"))
        except:
            pass


else:
    print("\n\n请先关注Brick Republic公众号之后在重登!")
    print("█████████████████████████████████████████")
    print("█████████████████████████████████████████")
    print("████ ▄▄▄▄▄ ██▀▀ ██▄▀ █▀▄  █▄ █ ▄▄▄▄▄ ████")
    print("████ █   █ █  █▄▄█▄ ██▀ ▄ ▄ ▀█ █   █ ████")
    print("████ █▄▄▄█ █  █▄▀▀ ▄▄▀▀▀▄█ ▀▀█ █▄▄▄█ ████")
    print("████▄▄▄▄▄▄▄█ ▀ █▄█▄█ █ ▀ ▀▄▀▄█▄▄▄▄▄▄▄████")
    print("████ ▀▄   ▄▀██▀██▀▄█▀   ██  ▄▀ ▄▄  █▀████")
    print("█████▀▀▄█▀▄▄▄ ▄   ▄▄█ ▀█ █▄█▀ ▀█ ▀ ▄▀████")
    print("████ ▄ ▄▄▄▄▀ █▄▀▀█▄▀▄▀▀▄▄ ▄▄ ▀▀▄█▄▀ ▀████")
    print("████▀█▀ ▄▀▄▄█ ▄ █▀  ▄▄██▄ ▀██ ▀ ▀█▀▄█████")
    print("█████ █▀ ▀▄▀  ▀█▄▄▀  █▀▀▀▀  ▄▄▀ ▄ ▀█ ████")
    print("████ █ █▀ ▄▄▀ █▀▀▄▄ ▄█▄▀  ▀█ ▀▄█ ▀  █████")
    print("████ ▄▄█▄▄▄▀   █▄▄▀▀▀▀▄▄▀ ▀  ▀▀▀▄▄▀█ ████")
    print("████ ██▀▀▀▄▀▀ █▄█▄▄█▀█▀ ▀ ▀▀█ ███▀▀ ▀████")
    print("████▄██▄▄▄▄▄ ▀▀▄█▄ █▄▀█ ▀██▀ ▄▄▄ ▄▀█ ████")
    print("████ ▄▄▄▄▄ █▀█▄  ▄▄ ▄ ▀▀▄█▄  █▄█ █  █████")
    print("████ █   █ █ █▀▀▀█  ▄█▀█▄▄▄▀  ▄  ▄▀▄▀████")
    print("████ █▄▄▄█ █▄ ▄▀ ▄  ▄▄ █▄▀▄███▄ ▀▀▀██████")
    print("████▄▄▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄███▄▄▄██▄▄██▄█████")
    print("█████████████████████████████████████████")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("\n\n请先关注Brick Republic公众号之后在重登!")




itchat.run()

