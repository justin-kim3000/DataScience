import pymysql as db
import pandas as pd

con = None
cursor = None
def connectDB():
    global con
    global cursor
    try:
        con = db.connect('test/1234@127.0.0.1/XE')
        print('ORA 버전:', con.version)
        cursor = con.cursor()
    except db.DatabaseError as e:
        err_msg(e)

def closeDB():
    try:
        con.close()
        print('오라클 DB 해제!')
    except db.DatabaseError as e:
        err_msg(e)

def err_msg(e):
    err_obj, = e.args
    print('------------------------')
    print('에러 코드:', err_obj.code)
    print('에러 메시지:', err_obj.message)
    print('------------------------')

def create_tbl():
    try:
        sql = """
            create table student_addr (
                id number,
                name varchar(20),
                age number,
                addr varchar(80))"""
        cursor.execute(sql)
        con.commit()
        print('테이블 생성 성공!')
    except db.DatabaseError as e:
        print("err 발생!")

def drop_tbl():
    try:
        sql = "drop table student_addr"
        cursor.execute(sql)
        con.commit()
        print('테이블 삭제 성공!')
    except db.DatabaseError as e:
        err_msg(e)

def insert_db(id=1, name='홍길동',
              age=100, addr='조선 한양 홍대감댁'):
    try:
        sql = f"insert into student_addr values " \
              f" ({id}, '{name}', {age}, '{addr}')"
        cursor.execute(sql)
        con.commit()
    except db.DatabaseError as e:
        err_msg(e)

def insert_db2():
    data = [1000, '김유신', 100, '조선 한양 홍대감댁']
    try:
        # binding
        sql = f"insert into student_addr values (:1,:2,:3,:4)"
        cursor.execute(sql, data)
        con.commit()
    except db.DatabaseError as e:
        err_msg(e)

def insert_db3():
    df = pd.DataFrame({'id': [1111, 2222, 3333],
                    'name': ['박길동','이길동', '최길동'],
                    'age': [100, 200, 300],
                    'addr': ['한양', '광주', '대구']})
    try:
        rows = [tuple(x) for x in df.values]
        cursor.executemany("insert into student_addr values (:1,:2,:3,:4)",
                          rows)
        con.commit()
    except db.DatabaseError as e:
        err_msg(e)

def select_db():
    sql = 'select * from student_addr order by id'
    try:
        cursor.execute(sql)
        for row in cursor:
            for i in range(len(row)):
                print(row[i], end='\t')
            print()
    except db.DatabaseError as e:
        err_msg(e)

def select_db2():
    sql = 'select * from student_addr order by id'
    try:
        cursor.execute(sql)
        df = pd.read_sql(sql, con)
        print(type(df))
    except db.DatabaseError as e:
        err_msg(e)















