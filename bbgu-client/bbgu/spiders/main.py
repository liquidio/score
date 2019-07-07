import scrapy

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from bs4 import BeautifulSoup

from bbgu.items import Check

class mainSpider(scrapy.Spider):
    name = "bbgu"
    start_urls = ['http://10.1.19.12/']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Referer':r'http://10.1.19.12/xscjcx.aspx?xh=1705417129&xm=%C0%EE%B4%D4%C1%A2&gnmkdm=N121628',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.1.19.12',
        'Origin': 'http://10.1.19.12'}

    #def start_requests(self):
    #    return [scrapy.FormRequest('http://10.1.19.12/',headers=self.headers,callback=self.parse)]
    
    
    def parse(self,response):
        self.log('A response from %s just arrived!' %  response.url)
        #page1 login
        #xrsf_input = response.xpath('//input[@name="__VIEWSTATE"]').extract()[0]
        #soup = BeautifulSoup(xrsf_input,features='lxml')
        #xrsf_code = soup.input['value']
        
        #Check['code_img'] = scrapy.FormRequest('http://10.1.19.12/CheckCode.aspx',headers=self.headers,meta={'cookiejar':response.meta['cookiejar']})

        #page2 get score
        res = response.xpath('//html').extract()
        print(res)

    def start_requests(self):
        cookies = {'ASP.NET_SessionId':'slyfqz55qn2m3155rcijaq45'}
        btn_zcj ='%C0%FA%C4%EA%B3%C9%BC%A8'
        viewstate = 'dDwtMTg1OTAwOTY4Njt0PHA8bDxTb3J0RXhwcmVzO3NmZGNiaztkZzM7ZHlieXNjajtTb3J0RGlyZTt4aDtzdHJfdGFiX2JqZztjamN4X2xzYjt6eGNqY3h4czs%2BO2w8a2NtYztcZTtiamc7XGU7YXNjOzE3MDU0MTcxMjk7emZfY3hjanRqXzE3MDU0MTcxMjk7OzE7Pj47bDxpPDE%2BOz47bDx0PDtsPGk8ND47aTwxMD47aTwzMD47aTw0MD47aTw1Mj47aTw1OD47aTw2MD47aTw2Mj47aTw2ND47aTw2Nj47aTw2OD47aTw3MD47aTw3Mj47aTw3ND47aTw3OD47aTw4MD47aTw4Mj47PjtsPHQ8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxYTjtYTjs%2BPjs%2BO3Q8aTwzPjtAPFxlOzIwMTgtMjAxOTsyMDE3LTIwMTg7PjtAPFxlOzIwMTgtMjAxOTsyMDE3LTIwMTg7Pj47Pjs7Pjt0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs%2BO2w8a2N4em1jO2tjeHpkbTs%2BPjs%2BO3Q8aTwxND47QDzlhazlhbHor7476YCa6K%2BG5b%2BF5L%2Bu6K%2B%2BO%2BmAmuivhumAieS%2FruivvjvlhazlhbHlv4Xkv67or7475YWs5YWx6YCJ5L%2Bu6K%2B%2BO%2BS4k%2BS4muS7u%2BmAieivvjvnrKzkuozor77loII75LiT5Lia6K%2B%2BO%2BmZkOmAieivvjvku7vpgInor7475a6e6Le16K%2B%2BO%2BS4k%2BS4muW%2FheS%2FruivvjvkuJPkuJrpgInkv67or747XGU7PjtAPDE7MTA7MTE7MTI7MTM7MTQ7MTU7MjszOzQ7NTs3Ozg7XGU7Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaIkOe7qeWPiue7qeeCueS7heS%2Bm%2BWPguiAg%2B%2B8jOS7peaVmeWKoeeuoeeQhuerr%2BS4uuWHhuOAgjs%2BPjs%2BOzs%2BO3Q8cDxwPGw8VGV4dDs%2BO2w8XGU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7VmlzaWJsZTs%2BO2w85a2m5Y%2B377yaMTcwNTQxNzEyOTtvPHQ%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOWnk%2BWQje%2B8muadjuS4m%2BeriztvPHQ%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOWtpumZou%2B8muacuuaisOS4juiIueiItua1t%2Ba0i%2BW3peeoi%2BWtpumZojtvPHQ%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOS4k%2BS4mu%2B8mjtvPHQ%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOacuuaisOW3peeoiztvPHQ%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrmlrnlkJE6Oz4%2BOz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOihjOaUv%2BePre%2B8muacuuaisOacrDE3MTtvPHQ%2BOz4%2BOz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BOz47Ozs7Ozs7Ozs7Pjs7Pjt0PDtsPGk8MT47aTwzPjtpPDU%2BO2k8Nz47aTw5PjtpPDEzPjtpPDE1PjtpPDE3PjtpPDIxPjtpPDIzPjtpPDI1PjtpPDI3PjtpPDI5PjtpPDMxPjtpPDMzPjtpPDM1PjtpPDM3PjtpPDQ1PjtpPDUxPjtpPDUzPjtpPDU1PjtpPDU3Pjs%2BO2w8dDxwPHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BOz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BO3A8bDxzdHlsZTs%2BO2w8RElTUExBWTpub25lOz4%2BPjs7Ozs7Ozs7Ozs%2BOzs%2BO3Q8O2w8aTwxMz47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOiHs%2BS7iuacqumAmui%2Fh%2Bivvueoi%2BaIkOe7qe%2B8mjtvPHQ%2BOz4%2BOz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE%2BO2k8MT47aTwxPjtsPD47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOmJsb2NrOz4%2BPjs7Ozs7Ozs7Ozs%2BO2w8aTwwPjs%2BO2w8dDw7bDxpPDE%2BOz47bDx0PDtsPGk8MD47aTwxPjtpPDI%2BO2k8Mz47aTw0PjtpPDU%2BO2k8Nj47PjtsPHQ8cDxwPGw8VGV4dDs%2BO2w8MDUwMTIxMnkwNjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS6kuaNouaAp%2BS4juaKgOacr%2Ba1i%2BmHjzs%2BPjs%2BOzs%2BO3Q8cDxwPGw8VGV4dDs%2BO2w85LiT5Lia6K%2B%2BOz4%2BOz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDUyOz4%2BOz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4%2BOz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuJPkuJrlv4Xkv67or747Pj47Pjs7Pjs%2BPjs%2BPjs%2BPjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4%2BOzs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4%2BOzs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47cDxsPHN0eWxlOz47bDxESVNQTEFZOm5vbmU7Pj4%2BOzs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BO3A8bDxzdHlsZTs%2BO2w8RElTUExBWTpub25lOz4%2BPjs7Ozs7Ozs7Ozs%2BOzs%2BO3Q8QDA8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxWaXNpYmxlOz47bDxvPGY%2BOz4%2BO3A8bDxzdHlsZTs%2BO2w8RElTUExBWTpub25lOz4%2BPjs7Ozs7Ozs7Ozs%2BOzs%2BO3Q8QDA8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjtwPGw8c3R5bGU7PjtsPERJU1BMQVk6bm9uZTs%2BPj47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDtAMDw7O0AwPHA8bDxIZWFkZXJUZXh0Oz47bDzliJvmlrDlhoXlrrk7Pj47Ozs7PjtAMDxwPGw8SGVhZGVyVGV4dDs%2BO2w85Yib5paw5a2m5YiGOz4%2BOzs7Oz47QDA8cDxsPEhlYWRlclRleHQ7PjtsPOWIm%2BaWsOasoeaVsDs%2BPjs7Ozs%2BOzs7Pjs7Ozs7Ozs7Oz47Oz47dDxwPHA8bDxUZXh0O1Zpc2libGU7PjtsPOacrOS4k%2BS4muWFsTQz5Lq6O288Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFZpc2libGU7PjtsPG88Zj47Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOaIkOe7qeWPiue7qeeCueS7heS%2Bm%2BWPguiAg%2B%2B8jOS7peaVmeWKoeeuoeeQhuerr%2BS4uuWHhuOAgjs%2BPjs%2BOzs%2BO3Q8cDxwPGw8VGV4dDs%2BO2w8WkpVOz4%2BOz47Oz47dDxwPHA8bDxJbWFnZVVybDs%2BO2w8Li9leGNlbC8xNzA1NDE3MTI5LmpwZzs%2BPjs%2BOzs%2BOz4%2BO3Q8O2w8aTwzPjs%2BO2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjs%2BPjs%2BPjs%2BPjs%2Bw%2Fo4bjgdjINsi6cPaj9NoaRRa7Y%3D'
        Score_request = {'__VIEWSTATE': viewstate,
            'btn_zcj':btn_zcj,
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            'hidLanguage':'',
            'ddlXN':'',
            'ddlXQ':'',
            'ddl_kcxz':'',
             }
        return [scrapy.FormRequest(r'http://10.1.19.12/xs_main.aspx?xh=1705417129',method='post',formdata=Score_request,headers=self.headers,cookies=cookies,callback=self.parse)]

    """
    def login(self,response):
        log_info = {
            'txtUserName':Check['username'],
            'TextBox2':Check['passwd'],
            'txtSecretCode':Check['secret_code'],
            '__VIEWSTATE':xrsf_code
        }
        return [scrapy.FormRequest("10.1.19.12",dont_filter=True,formdata=log_info,meta={'cookiejar':response.meta['cookiejar']},headerrs=self.headers,callback=self.parse)]
    """