"""
"""
from socket import *
import pymysql
#创建udp套接字

udp_socket= socket(AF_INET,SOCK_DGRAM)

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='dict',
    charset='utf8'
)
cur = db.cursor()

#绑定地址
udp_socket.bind(("0.0.0.0",1112))

#服务端先收
print("等待中。。。。。。")

while True:
    data,addr =udp_socket.recvfrom(1024)
    sql01 = "select mean from words where word=%s"
    cur.execute(sql01,[data])
    meaning=cur.fetchone()


    print("收到消息",data)
    #发送消息
    udp_socket.sendto(meaning[0].encode(),addr)
    # print("发送了%d bytes"%n)
db.commit()

#关闭套接字
udp_socket.close()
cur.close()
db.close()
