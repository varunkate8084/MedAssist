import pymysql as MySql
import pymysql.cursors
def ConnectionPooling():
    DB=MySql.connect(host='localhost',passwd='varun',port=3306,user='root',database='medassist_com',cursorclass=MySql.cursors.DictCursor)
    CMD=DB.cursor()
    return DB,CMD