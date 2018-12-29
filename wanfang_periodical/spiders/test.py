# import pymysql
#
# client = pymysql.connect(host='localhost',port=3307,user='root',password='root',database='test',charset='utf8')
# cursor = client.cursor()
#
# sql = "insert into student(name)value('%s'),('%s'),('%s')" % ('带鱼','西瓜','披萨')
#
# cursor.execute(sql)
# client.commit()
# print('插入成功！')
# query_sql="select*from student"
# cursor.execute(query_sql)
# res=cursor.fetchall()
# for row in res:
# 	print(row)
# print('一共%d行数据' % len(res))
# s = [
#     "CSTPCD",
#     "CSSCI",
#     "北大核心"
# ]
# a = isinstance(s,list)
# print(a)
# b = '&'.join(s)
# print(b)
# import random
# print(random.random()*0.7)
# 
# 
# s = '123%d' % 123
# print(type(s))