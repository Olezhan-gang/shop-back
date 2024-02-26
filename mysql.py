import datetime
import time
import random
import string
import pymysql

from config import host, user, password, database

current_data = datetime.datetime.now()
adddata = time.mktime(current_data.timetuple())

def establish_connection():
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor)
    return connection
    
    
def add_article(name,price,img):
     connection = establish_connection()
     with connection:
        with connection.cursor() as cursor:
                insert_query = "INSERT INTO `article` (name,price,image,adddate) VALUES (%s,%s,%s,%s)"
                cursor.execute(insert_query,(name,price,img,adddata))
                connection.commit()
            
def get_all_articles():
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
                select_query = "SELECT name,price,image FROM article"
                cursor.execute(select_query)
                result = cursor.fetchall()
                return result

def get_article(uuid):
    connection = establish_connection()
    with connection:
        with connection.cursor() as cursor:
                select_query = "SELECT * FROM article WHERE image = %s "
                cursor.execute(select_query,(uuid))
                result = cursor.fetchall()
                return result

def generate_orderid():
    timestamp = int(time.time())
    random_part = str(random.randint(10000, 99999))
    current_date = datetime.datetime.now()
    day_letters = current_date.strftime('%A')[:2].upper()
    month_letters = current_date.strftime('%B')[:2].upper()
    first_part = day_letters + month_letters
    return f"{first_part}-{timestamp}-{random_part}" 


