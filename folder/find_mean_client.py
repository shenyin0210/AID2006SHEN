"""
    udp客户端示例
    重点代码！
"""

from socket import *
#创建UDP套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
address=("127.0.0.1",1112)
#输入什么发送什么
while True:
    msg=input(">>")
    if msg=='':
        break
    udp_socket.sendto(msg.encode(),address)

    data,addr=udp_socket.recvfrom(1024)
    print("从服务端收到",data.decode())

udp_socket.close()