import datetime
import time

import pymysql

from config import host, user, password, database

current_data = datetime.datetime.now()
adddata = time.mktime(current_data.timetuple())

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor
    )
	
    
except Exception as ex:
    print(str(ex))
    
def add_article(name,price,img):
     with connection.cursor() as cursor:
        try:
            insert_query = "INSERT INTO `article` (name,price,image,adddate) VALUES (%s,%s,%s,%s)"
            cursor.execute(insert_query,(name,price,img,adddata))
            connection.commit()
        except Exception as ex:
            print(f"Error:{ex}")
            
def get_all_articles():
    with connection.cursor() as cursor:
        try:
            select_query = "SELECT name,price,image FROM article"
            cursor.execute(select_query)
            result = cursor.fetchall()
            return result

        except Exception as ex:
            print(f"Error:{ex}")
            
print(get_all_articles())