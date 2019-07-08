from urllib import request,parse,error
import http.cookiejar
from bs4 import BeautifulSoup as bs
import time

#用于爬学校教务通
class Spider:
    '''not in __init
    self.cookie
    self.check_code
    '''
    def __init__(self):
        self.user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
        self.host = '10.1.19.12'
        self.headers ={'User-Agent':self.user_agent,
            'Host':self.host}
        self.serverIP = '127.0.0.1/'
    #登录后设置cookie#
    def login(self,username,passwd,checkcode):
        self.login_url = r'http://10.1.19.12/'
        if not self.cookie :
            response = self.__set_cookie(username)
            #登录表单#
            login_form = parse.urlencode([{
                ('__VIEWSTATE',self.__get_viewstate(response)),
                ('txtUserName',username),
                ('TextBox2',passwd),
                ('txtSecretCode',self.check_code),
                ('RadioButtonList1',parse.unquote(r'%D1%A7%C9%FA'))
            }])
            #尝试登录#
            try:
                req = request.Request(self.login_url+'deault2.aspx/',data=login_form, headers=headers)
                response = opener.open(req)
                if -1 == self.__check_form(response):
                    return 'cannot login'
                self.cookie.save(ignore_discard=True, ignore_expires=True)
                self.logged_in = True
            except error.URLError as e :
                print(e.reason)
            except :
                return 'error code 1'
        else:
            #验证cookie是否能用#
            try:
                req = request.Request(self.login_url+'xs_main.aspx?xh='+xh, headers=headers)
                response = request.urlopen(req)
                if -1 ==self.__check_logged_in(response):
                    return 'cookie not True'
            except :
                return 'cookie not True'

    #获取历年成绩 返回table标签html文本内容#
    def get_score(self,user):
        opener = self.__get_cookie(user)
        req = request.Request('http://10.1.19.12/xscjcx.aspx?xh='+user['xh']+'&xm='+user['xm']+'&gnmkdm=N121628',headers=self.headers)
        req.add_header('Referer','http://10.1.19.12/xs_main.aspx?xh='+user['xh'])

        btn_zcj = parse.urlencode([
            ('__VIEWSTATE',self.__get_viewstate(req)),
            ('btn_zcj',parse.unquote(r'%C0%FA%C4%EA%B3%C9%BC%A8')),
            ('__EVENTTARGET',''),
            ('__EVENTARGUMENT',''),
            ('hidLanguage',''),
            ('ddlXN',''),
            ('ddlXQ',''),
            ('ddl_kcxz','')
            ])
        try:
            with opener.open(req,data=btn_zcj.encode('utf-8')) as f:
                data = f.read()
                html = bs(data.decode('gb2312'),'lxml')
                return html.select('table')
        except:
            return 'Cannot get score'

    #获取验证码#
    def get_check_code(self):
        img = request.urlopen(self.login_url+'CheckCode.aspx')
        #生成图片地址#
        import random
        randomID =str(time.time())+str(random.randint(1,100000))+'.gif'
        seed = request.base64.b64encode(randomID)
        import hashlib
        randomID = hashlib.md5()
        randomID.update(seed)
        with open('./static/'+randomID.hexdigest()+'.gif','wb') as f:
            f.write(img)
        return self.serverIP+'static/'+randomID.hexdigest()+'.gif'
    
    def set_check_code(self,check_code):
        self.check_code = check_code

    #获取xrsf验证码#
    def __get_viewstate(self,req):
        with request.urlopen(req) as f:
            data = f.read()
            html = bs(data.decode('Windows 1252'),'lxml')
            viewstate = html.select('input[name="__VIEWSTATE"]')[0]['value']
        return viewstate
    #设置cookie，返回request#
    def __set_cookie(self,user):
        self.cookie = http.cookiejar.MozillaCookieJar(user['xh'])
        handler = request.HTTPCookieProcessor(self.cookie)
        opener = request.build_opener(handler)
        try :
            return opener.open(self.login_url)
        except error.URLError as e :
            print(e.reason)
    def __get_cookie(self,user):
        self.cookie = http.cookiejar.MozillaCookieJar(user['xh'])
        handler = self.cookie.load(user['xh'], ignore_discard=True, ignore_expires=True)
        return request.build_opener(handler)

    #检查表单填写是否正确，是否能登录#
    def __check_form(self,response):
        if  response.find('验证码不正确！！') :
            return 'checkCode not true'
        elif response.find('密码错误'):
            return 'cannot login'
    def __check_logged_in(self,response):
        return response.find('欢迎您')