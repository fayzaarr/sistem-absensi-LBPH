import pymysql


class connection(object):

    def __init__(self):
        super(connection, self).__init__()
        self.con = pymysql.connect(
            db='absensi', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        self.cur = self.con.cursor()

    def disconnect(self):
        if self.cur.connection:
            self.cur.close()
            self.con.close()
            print("MySQL connection is closed")