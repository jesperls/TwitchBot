import sqlite3
import os

def create():
    if os.path.exists("drift.db"):
        os.remove("drift.db")
    with open("Database/database.sql", "r") as sql_file:
        sql_script = sql_file.read()
        con = sqlite3.connect("drift.db")
        cur = con.cursor()
        cur.executescript(sql_script)
        con.commit()
        con.close()

def execute(query, fetch = False):
    try:
        con = sqlite3.connect("drift.db")
        cur = con.cursor()
        res = cur.execute(query)
        res = res.fetchall()
        con.commit()
        con.close()
        if fetch:
            return res
    except sqlite3.IntegrityError:
        return -1
