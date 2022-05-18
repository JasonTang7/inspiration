import socket
target_host = "192.168.2.2" #服务器端地址
target_port = 8888  #必须与服务器的端口号一致
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))       # 连接服务器   
while True:
    data = input(">")
    if not data:
        break
    client.send(data.encode())      # 发送数据
    response = client.recv(1024)        # 接收回应
    print(response)
client.close()      # 关闭连接，释放资源