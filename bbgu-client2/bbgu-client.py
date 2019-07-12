
import pymysql
import websocket

from urllib import request
import json
import os
import threading
import time

import spider
import setting

#事件表#
users = set()
handler_user = set()
###########main##############################
def handler(ws):
    if users :
        for i in users:
            if i in handler_user:
                continue
            #handler接收未处理的消息#
            dispose(ws,i)
            #处理后删除#
            handler_user.remove(i)
            users.remove(i)

def dispose(ws,res):
    try:   
        if res['command'] == 'GET_SCORE':
        
            #获取成绩
            score = spider.Spider().get_score(res)
            score.update_score({"user":res['user'],"score":score})
            ws.send(jsno.dumps({"command":"GET_SCORE","result":True}))
    except :
        try:
                #登录#
            if not res['check_code']:
                s = spider.Spider()
                check_code_bs4 = s.get_check_code()
                ########验证码图片的base4格式返回给服务器#
                ws.send(json.dumps({'username':res['username'],'check_code_bs4':check_code_bs4}))
                #####使用用户信息和验证码登录#
            s.login(res['username'],res['passwd'],res['check_code'])
        except:
            raise
        return res
    try:
        if res['login_test']:
            s = spider.Spider()
            #####使用用户信息和验证码登录#
            s.login(res['username'],res['passwd'],res['check_code'])
            if s.check_logged_in():
                try:
                    db.DB().add_user(res['username'],res['passwd'])   
                except:
                    pass
                ws.send(json.dumps({"login_test":True}))
    except:
        return res

####################websocket####################
def on_open(ws):
    try :
        j = json.dumps({'server':True,'suser':setting.user,'spasswd':setting.passwd})
        ws.send(j)
    except:
        raise
def on_message(ws, message):
    try:
        print(message)
        res = json.loads(message)
    except:
       return
    try:
        if not res['server']:
            print("connect failed")
            ws.close()
            os._exit()
        if re['user']:
            users.add(res)
            handler(ws)
    except:
        return

def on_error(ws, error):
    print("websocket:",error)


def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    wsr = websocket.WebSocketApp('ws://'+setting.server_ip+'/backend',on_message=on_message,on_close=on_close,on_error=on_error)
    wsr.on_open = on_open
    wsr.run_forever()