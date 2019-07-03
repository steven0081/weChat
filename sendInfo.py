import itchat
import time
import os

itchat.auto_login(hotReload=True)

result = itchat.search_friends(name='董黎')
user_name = result[0]['UserName']

path= 'I:\\PycharmProjects\\paChong\\mzitu'
file_list = os.listdir(path)
print(len(file_list))
for f in file_list:
    itchat.send_image(path+'\\'+f, user_name)
    time.sleep(1)




