#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#适用于一次发送对应一次接收，且接收数据较大的情况

import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:
s.connect(('192.168.2.2', 8888))

# 发送数据:
s.send(bytes(input('>'),'utf-8'))

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

# 关闭连接:
s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# 把接收的数据写入文件:
with open('GMXW1.html', 'branson') as f:
    f.write(data)