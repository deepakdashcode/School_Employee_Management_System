import mysql.connector as c
db=c.connect(host='localhost',user='your_username',passwd='your_password',database='SCHOOL')
cursor=db.cursor()


# Creating Database

sql=f'create database School'
print(sql)
cursor.execute(sql)
db.commit()


# Using Database


sql=f'use School'
print(sql)
cursor.execute(sql)
#db.commit()


# Creating Table for class LKG and UKG


sql=f'create table Class_LKG (Name varchar(50) ,Roll_number varchar(10));'
print(sql)
cursor.execute(sql)
db.commit()


sql=f'create table Class_UKG (Name varchar(50) ,Roll_number varchar(10));'
print(sql)
cursor.execute(sql)
db.commit()

# Creating Table for class 1 to 10


for i in range(1,11):
    sql=f'create table Class_{i} (Name varchar(50) ,Roll_number varchar(10),Section varchar(2),Optional varchar(20));'
    print(sql)
    cursor.execute(sql)
    db.commit()



# Creating table for teachers

sql=f'create table teachers (Subject varchar(25),Name varchar(50),Class varchar(5));'
print(sql)
cursor.execute(sql)
db.commit()




