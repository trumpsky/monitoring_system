import pymysql
from DBUtils.PooledDB import PooledDB
from config import settings


DB_HOST = settings.DB_HOST
DB_USER = settings.DB_USER
DB_PWD = settings.DB_PWD
DB_NAME = settings.DB_NAME

POOL = PooledDB(
    creator=pymysql,
    maxconnections=6,
    mincached=2,
    blocking=True,
    ping=0,

    host=DB_HOST,
    port=3306,
    user=DB_USER,
    password=DB_PWD,
    database=DB_NAME,
    charset="utf8"
)

# def fetchall():
conn = POOL.connection()
cursor = conn.cursor()

cursor.execute("select * from test_table")
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()