import tornado.ioloop
import tornado.web

import json

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({"logged_in":False}))
    def post(self,user,passwd,wxID):
        if not self.get_secure_cookie("userID"):
            self.set_secure_cookie("userID",userID)
        pass


class BaseHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def initialize(self):
        if not self.get_secure_cookie("userID"):
            self.set_secure_cookie("userID",userID)

    def get_current_user(self):
        return self.get_secure_cookie("user")
    def get_check_code(self):
        pass

class MainHandler(BaseHandler):
    #menu返回功能表
    def get(self):
        self.write(json.dumps({"user":[{"hello":"world"},{"is_server":True}]}))

class BackendHandler(tornado.web.websocket.WebSocketHandler):
    #获取可用的server
    @tornado.web.authenticated
    def open(self):
        self.write_message("connect successful")
    def on_message(self,message):
        print("message")
    def on_close(self):
        pass
    def check_origin(self):
        return True

class ScoreHandler(BaseHandler):
    def get(self,userinfo):
        pass
        
def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        "login_url": "/login",
        "xsrf_cookies": True,
        }

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login",LoginHandler),
        (r"/backend",BackendHandler)
    ],**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()