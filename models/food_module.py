import psycopg2
from models import common

# Create a class 'Food' with attributes

# - id
# - name
# - image_url
# - price

class Food:

    def __init__(self, id=0, name=None, image_url=None, price=0.0):
        self.id=id
        self.name=name
        self.image_url=image_url
        self.price=price
 
    def insert_food(self):
        # Use PriceUtility class to convert price into cents
        price_util=PriceUtility(self.price)
        price_in_cents=price_util.convert_price_to_cents()

        # Insert new record for the given values into the database
        # Note: If you run inser_food function for the same Food multiple times
        common.sql_write("INSERT INTO food (name, image_url, price_in_cents) VALUES (%s, %s, %s);", [self.name, self.image_url, price_in_cents])

    def convert_to_dictionary(self, item):
        return {
            "id": str(item[0]), 
            "name": item[1], 
            "image_url": item[2], 
            "price": "{:.2f}".format(item[3]/100)
            }

    def get_all_food(self):
        all_items = common.sql_read("SELECT * FROM food;")
        return [self.convert_to_dictionary(item) for item in all_items]

    def get_food(self):
        item = common.sql_read("SELECT * FROM food WHERE id=%s;", [self.id])[0]
        return self.convert_to_dictionary(item)
    
    def update_food(self, new_name, new_image_url, new_price):

        # Use PriceUtility class to convert price into cents
        price_util=PriceUtility(new_price)
        new_price_in_cents=price_util.convert_price_to_cents()

        # Since we want to update the existing data, 
        # we will use the existing id and update the name,image and the price 
        # for the same record (identified by it's database id) 
        # with the new values
        common.sql_write(f"UPDATE food SET name=%s, image_url=%s, price_in_cents=%s WHERE id={self.id}", [new_name, new_image_url, new_price_in_cents])
    

    # Deletes the current food
    def delete_food(self):
        common.sql_write(f"DELETE FROM food WHERE id={self.id}")

    # Converts the price from cents to Dollars and returns the formatted result
    def format_price(self):
        price_util=PriceUtility(self.price)
        return f"${price_util.convert_price_from_cents()}"


# Utility class for converting price from dollars to cents or the other way around
class PriceUtility:

    # Constructor that takes price as input
    def __init__(self, price):
        self.price=price

    # Converts the price value from Dollars into cents
    def convert_price_to_cents(self):
        return int(float(self.price)*100)        

    # Converts the price amount from cents to Dollars
    def convert_price_from_cents(self):
        return float(self.price/100)
