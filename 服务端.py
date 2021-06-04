# coding = utf-8
# @Time: 2021/6/4 16:32
# @Author: 任添宁
# @File: 服务端.py
# @Software: PyCharm

'''前提学习'''
'''
1.socket模块：要创建套接字，必须使用套接字模块中的socket.socket()函数，该函数具有一般语法s = socket.socket (socket_family, socket_type, protocol = 0)
2.socket_family: 它的值可以是：AF_UNIX或AF_INET
3.socket_type: 它的值可以是：SOCK_STREAM或SOCK_DGRAM。

1.s.bind()此方法将地址(主机名，端口号对)绑定到套接字。
2.s.recvfrom()此方法接收UDP消息，返回值是一对(字节， 地址) ，其中字节是代表接收到的数据的字节对象，而地址是发送数据的套接字的地址
3.s.sendto()此方法发送UDP消息，将数据发送到套接字。该套接字不应连接到远程套接字，因为目标套接字是由address指定的
4.s.close()此方法关闭套接字，套接字对象上所有以后的操作都将失败。远端将不再接收任何数据(在清除排队的数据之后)。套接字在被垃圾回收时会自动关闭
5.s.gethostname()返回主机名，返回一个字符串，其中包含当前正在执行Python解释器的计算机的主机名。
'''

#sever.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()

port = 8088

s.bind((host,port))
while True:
    try:
        receive_data, addr = s.recvfrom(1024)

        print("来自服务器" + str(addr) + "的消息:")

        print(receive_data.decode('utf-8'))

        msg = input('please input send to msg:')

        s.sendto(msg.encode('utf-8'), addr)

    except:
        s.close()













