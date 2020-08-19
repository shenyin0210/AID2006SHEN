"""
"""
from socket import *
#创建udp套接字
udp_socket= socket(AF_INET,SOCK_DGRAM)

#绑定地址
udp_socket.bind(("0.0.0.0",1111))

#服务端先收
print("等待中。。。。。。")

while True:
    data,addr =udp_socket.recvfrom(1024)
    print("收到消息",data)
    #发送消息
    n=udp_socket.sendto(b"123",addr)
    print("发送了%d bytes"%n)


#关闭套接字
udp_socket.close()