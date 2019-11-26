import pymysql
class Conn(object):

    def __init__(self,host,user,passwd,db):
        self.conn=pymysql.connect(host,user,passwd,db)
        self.cur=self.conn.cursor()

    def queryOne(self,sql):
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.fetchall()

    def dropConn(self):
        self.conn.close()

    def insertMany(self,sql,values):
        self.cur.executemany(sql,values)
        self.conn.commit()

