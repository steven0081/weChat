import itchat
import time
import os

itchat.auto_login(hotReload=True)

#发送信息给好友
result = itchat.search_friends(name='董黎')
#发送信息给群
#result = itchat.search_chatrooms(name='疯狂摩的司机群')

user_name = result[0]['UserName']

path = '..\\paChong\\mzitu'
file_list = os.listdir(path)
print(len(file_list))
for f in file_list:
    file = path+'\\'+f
    if os.path.isfile(file):
        itchat.send_image(file, user_name)
        time.sleep(1)



