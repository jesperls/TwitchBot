import pymysql

def get_connection():
    connection = pymysql.connect(host='localhost', user='drift', password='', db='drift')
    return connection

def create():
    with open("Database/database.sql", "r") as sql_file:
        ret = sql_file.read().split(';')
        ret.pop()
        for query in ret:
            execute(query+";")

def execute(query):
    con = get_connection()
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    con.commit()
    con.close()
    return res

if __name__ == "__main__":
    create()
