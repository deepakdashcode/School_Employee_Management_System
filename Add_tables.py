import mysql.connector as c
db=c.connect(host='localhost',user='root',passwd='2580',database='SCHOOL')
cursor=db.cursor()
sql=input('Enter sql query\n')
cursor.execute(sql)

