#! /user/bin/python3

import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.concurrent import run_on_executor

import os
import json
import time
import random
import hashlib
import base64

import db
import setting

BOX = set()

class LoginHandler(tornado.web.RequestHandler):
    async def get(self):
        await self.write(json.dumps({"check_code":False}))

    async def post(self,user : str,passwd :str ,check_code :str )->None:
        if not self.get_secure_cookie("userI"):
            for i in BOX:
                if not await i.login_test():
                    self.write(json.dumps({"message":"登录失败"}))
                    return 
            self.set_secure_cookie("user",{"username":user,"passwd":passwd,"check_code":check_code})
        try:
            if await db.DB().add_user(user,passwd):
                self.write(json.dumps({"message":"登录成功"}))
        except:
            self.write(json.dumps({"message":"登录失败"}))
            return
        self.redirect('/')

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

@tornado.web.authenticated
class MainHandler(BaseHandler):
    #menu返回功能表
    def get(self):
        self.write(json.dumps({"user":[{"hello":"world"},{"is_server":True}]}))

@tornado.web.authenticated
class Score(BaseHandler):
    async def get(self):
        try:
            await self.write(db.DB().get_score(self.current_user()))
        except:
            self.write({"message":"查询出错"})
    async def post(self):
        for i in BOX:
            try:
                await i.write_message(json.dumps({"user":self.get_current_user,"command":"GET_SCORE"}))
                if await i.status():
                    self.write(json.dumps({"user":self.current_user['username'],"score":db.DB().get_score(self.current_user['username'])}))
                break
            except:
                pass
#ws连接#
class BackendHandler(tornado.websocket.WebSocketHandler):
    #获取可用的server
    #@tornado.web.authenticated
    def open(self):
        BOX.add(self)
        self.server = setting.user

    async def on_message(self,message : dict)->None:
        
        try:
            j = json.loads(message)
            if not j['server']:
               self.send(json.dumps({"server":False}))
               return
            await self.write_message(json.dumps({"connect":True}))
        except:
            return
        try:
            self.check_code = j['check_code']
        except:
            pass
        try:
            self.command_status = j["command_status"]
        except:
            pass
        try:
            self.login_status= j["login_status"]
        except:
            pass

    @run_on_executor()
    def status(self):
        while not self.command_status:
            time.sleep(1)
        return True
    @run_on_executor()
    def check_code_status(self):
        while not self.check_code:
            time.sleep(1)
        return True
    @run_on_executor()
    def login_test(self,user):
        self.write_message(json.dumps({"login":user}))
        i = setting.timeout
        while i and not self.login_status:
            time.sleep(1)
            i = i-1
        return False


    def on_close(self):
        print("closed")
        BOX.remove(self)

    def check_origin(self,origin):
        return True

def make_app():
    
    #create cookie_secret
    i = str(random.randint(1,8888))
    t = str(time.time())
    prefix = str('bbgu')
    entry = (prefix+i+t).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(entry)
    md5_value = md5.hexdigest()
    cookie_secret = base64.b64encode(md5_value.encode('utf-8')).decode('utf-8')

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": cookie_secret,
        "login_url": "/login",
        "xsrf_cookies": True,
        }

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/score",Score),
        (r"/login",LoginHandler),
        (r"/backend",BackendHandler)
    ],**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

