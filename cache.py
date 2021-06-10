import mysql.connector as c
db=c.connect(host='localhost',user='root',passwd='2580',database='SCHOOL')
cursor=db.cursor()
for i in range(3,11):
    sql=f'create table Class_{i} (Name varchar(50) ,Roll_number varchar(10),Section varchar(2),Optional varchar(20));'
    print(sql)
    cursor.execute(sql)
    db.commit()


