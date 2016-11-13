__author__ = 'ZY'
'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
'''
import pymysql,iviationCode


    #获取一个数据库连接
conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='python',port=3306)
cur=conn.cursor()   #获取一个游标
listInviaCode=iviationCode.multiInviaCode(200)
try:
    for id in range(200):
        sql = "insert into new_table(code) values(\'%s\')"%listInviaCode[id]
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print("数据载入发生异常:",e)
    conn.rollback()
    cur.close()
    conn.close()


