import pymysql
import spider
import setting

class DB:
    def __init__(self):
        try:
            self.connect = pymysql.connect(host=setting.address,port=setting.DB_PORT,user=setting.user,passwd=setting.passwd,db=setting.DB,charset='utf8mb4')
            self.cursor = self.connect.cursor()
        except:
            raise
    def __del__(self):
        try:
            self.cursor.close()
            self.connect.close()
        except:
            raise

    def add_user(self,username,passwd):
        sql = '''insert into user values(%s,%s)'''%(username,passwd)
        self.cursor.execute(sql)
    def update_score(self,score,name):
        sql = '''update user set score=%s where name=%s'''%(score,name)
        self.cursor.execute(sql)
    def get_score(self,name):
        sql = '''select score from user where name=%s'''%(name)
        self.cursor.execute(sql)
