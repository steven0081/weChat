import itchat


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print(msg)

@itchat.msg_register(itchat.content.PICTURE)
def reply_pic(pic):
    pass

def main():
    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__ == '__main__':
    main()




