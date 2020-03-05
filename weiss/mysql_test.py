import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='root', host='localhost', database='test')
    cursor = conn.cursor()
    # cursor.execute('create table user(id int primary key,name varchar(64))')
    # cursor.execute('insert into user values(4,"siwei")')
    # print(cursor.rowcount)
    cursor.execute('insert into user(id,name) values(%s,%s)', (5,'mike'))

except BaseException as e:
    print('exception: ', e)
finally:
    print('finally..')
    if cursor:
        cursor.close()
    if conn:
        conn.commit()

try:
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()

    execute = cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)

except BaseException as e:
    print('exception: ', e)
finally:
    print('finally..')
    if cursor:
        cursor.close()
    if conn:
        conn.commit()
