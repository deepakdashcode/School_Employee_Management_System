import mysql.connector as c
db=c.connect(host='localhost',user='your_username',passwd='your_password',database='SCHOOL')
cursor=db.cursor()


def add_teacher():
    try:
        name=input('Enter the name of the teacher\n').strip()
        Class=input('Enter the class\n').strip().lower()
        subject=input('Enter the subject\n').strip().lower()
        sql=f'insert into teachers values("{subject}","{name}","{Class}");'
        print(sql)
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('Failed to add teacher')


    
def display_teacher():
    try:
        Class=input('Enter the class\n').strip()
        subject=input('Enter the subject\n').strip().lower()
        sql=f'select * from teachers where Class = "{Class}" and subject="{subject}"'
        #print(sql)
        cursor.execute(sql)
        for i in cursor:
            print(i[1])
    except:
        print('Some Error Occurred\n')



def add_student():
    try:
        CLASS=input('Enter the class\n').strip().lower()
        if CLASS=='lkg' or CLASS == 'ukg':
            Name=input('Enter the name\n').strip().lower()
            Roll_number=input('Enter the roll_number: ').strip().lower()
            sql=f'insert into class_{CLASS} values("{Name}","{Roll_number}")'
            cursor.execute(sql)
            db.commit()
        elif 1<=int(CLASS)<=10:
            name=input('Enter name\n')
            roll_number=input('Enter the roll number: ')
            section=input('Enter the section: ')
            optional=input('Enter the optional_subject\n').strip().lower()
            sql=f'insert into class_{CLASS} values ("{name}","{roll_number}","{section}","{optional}")'
            cursor.execute(sql)
            db.commit()
        else:
            print('Invalid Class')
    except:
        print('Some Error OCCURRED!!!')


def display_student():
    try:

        roll_number=input('Enter the roll_number\n').strip().lower()
        CLASS=input('Enter the class\n').strip().lower()
        section=input('Enter the section\n').strip().lower()
        sql=f'select * from class_{CLASS}  where Roll_number="{roll_number}" and section="{section}"'
        cursor.execute(sql)
        for i in cursor:
            print(i)
    except:
        print('Some error occurred')
display_student()