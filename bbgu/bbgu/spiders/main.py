import scrapy

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

from bs4 import BeautifulSoup

from bbgu.items import Check

class mainSpider(scrapy.Spider):
    name = "bbgu"
    start_urls = ['http://10.1.19.12/']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    def start_requests(self):
        return [scrapy.FormRequest('http://10.1.19.12/',headers=self.headers,callback=self.parse)]
    
    
    def parse(self,response):
        self.log('A response from %s just arrived!' %  response.url)
        #page1 login
        xrsf_input = response.xpath('//input[@name="__VIEWSTATE"]').extract()[0]
        soup = BeautifulSoup(xrsf_input,features='lxml')
        xrsf_code = soup.input['value']
        
        Check['code_img'] = scrapy.FormRequest('http://10.1.19.12/CheckCode.aspx',headers=self.headers,meta={'cookiejar':response.meta['cookiejar']})

        #page2 get sore

        
    
    def login(self,response):
        log_info = {
            'txtUserName':Check['username'],
            'TextBox2':Check['passwd'],
            'txtSecretCode':Check['secret_code'],
            '__VIEWSTATE':xrsf_code
        }
        return [scrapy.FormRequest("10.1.19.12",dont_filter=True,formdata=log_info,meta={'cookiejar':response.meta['cookiejar']},headerrs=self.headers,callback=self.parse)]