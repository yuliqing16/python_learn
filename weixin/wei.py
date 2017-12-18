import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content333(msg):
    try:
        print(msg['Text'])
        itchat.send("你和我说" + msg['Text'] + "干嘛",msg['FromUserName'])
        print(msg)
    except:
        return

itchat.auto_login(hotReload=True)
itchat.run()
