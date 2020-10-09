#coding:utf-8
"""
sql语句传参练习
"""
import pymysql

#　创建连接
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd = "mysql",
                     database='stu',
                     charset='utf8')

#　创建游标
cur = db.cursor()

while True:
    id = input("id:")
    name = input('Name:')
    age = input("Age:")
    sex = input("m or w:")
    score = input("Score:")

    # sql = "insert into myclass (name,age,gender,score) \
    #       values ('%s',%d,'%s',%f);"%(name,age,gender,score)

    sql = "insert into class_1 (id,name,age,sex,score) \
           values (%s,%s,%s,%s,%s);"

    try:
        #　列表中元素全是字符串，执行语句，自动识别类型
        cur.execute(sql,[id,name,age,sex,score])
        db.commit()
    except Exception as e:
        db.rollback()  #失败回滚到操作之前的状态
        print("Faild:",e)

cur.close()
db.close()
