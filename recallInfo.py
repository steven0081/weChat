import itchat

@itchat.msg_register('Notice')

def message(msg):
    print(msg)

def notice(message):
    print(message)

def main():
    itchat.auto_login(hotReload=True)
    itchat.run()





