from urllib import request,parse
from bs4 import BeautifulSoup as bs

def get_score(cookie):
    req = request.Request(r'http://10.1.19.12/xscjcx.aspx?xh=1705417129&xm=%C0%EE%B4%D4%C1%A2&gnmkdm=N121628')

    req.add_header('Referer',r'http://10.1.19.12/xs_main.aspx?xh=1705417129')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    req.add_header('Origin','http://10.1.19.12')
    req.add_header('Cookie',cookie)
    req.add_header('Host','10.1.19.12')
    with request.urlopen(req) as f:
        data = f.read()
        html = bs(data.decode('Windows 1252'),'lxml')
        xrsf = html.select('input[name="__VIEWSTATE"]')[0]['value']
        
    target = parse.unquote(r'%C0%FA%C4%EA%B3%C9%BC%A8')

    form_info = parse.urlencode([
        ('__VIEWSTATE',xrsf),
        ('btn_zcj',target),
        ('__EVENTTARGET',''),
        ('__EVENTARGUMENT',''),
        ('hidLanguage',''),
        ('ddlXN',''),
        ('ddlXQ',''),
        ('ddl_kcxz','')
        ])

    with request.urlopen(req,data=form_info.encode('utf-8')) as f:
        data = f.read()
        #status
        print('Status:', f.status, f.reason)
        html = bs(data.decode('Windows 1252'),'lxml')
        return html.select('table')