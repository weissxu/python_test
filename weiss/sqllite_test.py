import sqlite3

try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user(id int primary key,name varchar(64))')
    cursor.execute('insert into user values(1,"siwei")')
    print(cursor.rowcount)
    cursor.execute('insert into user values(?,?)', (2, 'mike'))

except BaseException as e:
    print('exception: ', e)
finally:
    print('finally..')
    if cursor:
        cursor.close()
    if conn:
        conn.commit()


try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    execute = cursor.execute('select * from user')
    fetchall = execute.fetchall()
    print(fetchall)

except BaseException as e:
    print('exception: ', e)
finally:
    print('finally..')
    if cursor:
        cursor.close()
    if conn:
        conn.commit()
