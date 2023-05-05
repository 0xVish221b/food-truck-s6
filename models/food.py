import psycopg2
from models import common

def insert_food(name, image_url, price):
    common.common.sql_write("INSERT INTO food (name, image_url, price_in_cents) VALUES (%s, %s, %s);", [name, image_url, int(float(price)*100)])

def convert_to_dictionary(item):
    return {"id": str(item[0]), "name": item[1], "image_url": item[2], "price": "{:.2f}".format(item[3]/100)}

def get_food(id):
    item = common.sql_read("SELECT * FROM food WHERE id=%s;", [id])[0]
    return convert_to_dictionary(item)

def get_all_food():
    items = common.sql_read("SELECT * FROM food;")
    return [convert_to_dictionary(item) for item in items]

def update_food(id, name, image_url, price):
    common.sql_write(f"UPDATE food SET name=%s, image_url=%s, price_in_cents=%s WHERE id={id}", [name, image_url, int(float(price)*100)])

def delete_food(id):
    common.sql_write(f"DELETE FROM food WHERE id={id}", [id])