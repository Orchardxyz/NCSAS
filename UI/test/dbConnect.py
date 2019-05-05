# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 17:12
# @Author  : JackeyChen
# @FileName: dbConnect.py
# @Software: PyCharm

import pymysql

# 连接数据库



def dbConnect(tableName):
    try:
        db = pymysql.connect("localhost", "root", "Xg123456", "preprocessing", charset='utf8')
        # db = pymysql.connect("localhost", "root", "123456", "preprocessing", charset='utf8')
        cur = db.cursor()
        cur.execute("SELECT * FROM "+tableName+" WHERE id BETWEEN 1 AND 100")
        data = cur.fetchall()
        print('SUCCESS: 数据库连接成功！')
        cur.close()
        db.close()
        return data
    except:
        print('ERROR: 数据库连接失败！')
        return None

# if __name__ == "__main__":
#     data = dbConnect("lenovoscoreneg")
#     print(data[2])

