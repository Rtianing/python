# coding = utf-8
# @Time: 2021/6/4 16:48
# @Author: 任添宁
# @File: 客户端.py
# @Software: PyCharm

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    try:
        host = socket.gethostname()

        port = 8088

        send_data = input('please input msg:')

        s.sendto(send_data.encode('utf-8'), (host, port))

        msg, addr = s.recvfrom(1024)

        print("来自服务器" + str(addr) + "的消息:")

        print(msg.decode('utf-8'))

    except:
        s.close()





