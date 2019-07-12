import itchat
import time
import os

itchat.auto_login(hotReload=True)

#发送信息给好友
result = itchat.search_friends(name='董黎')
#发送信息给群
#result = itchat.search_chatrooms(name='疯狂摩的司机群')

user_name = result[0]['UserName']

itchat.send_msg('撸起，帅多！', user_name)




