import bcrypt
from models import common


class User:

  # Constructor accepting name, email and plain_text_password for user
  # If we were to do update and delete operations like we do on Food, 
  # we would need the id as well, it is not required in this case
  def __init__(self, name=None, email=None, plain_password=None):
    self.name=name
    self.email=email
    self.plain_password=plain_password

  def get_user_if_valid(self):
    results = common.sql_read(f"SELECT * FROM users WHERE email=%s;", [self.email])
    if len(results):
      user = results[0]
      user_formatted = { "id": user[0], "email": user[1], "name": user[2], "password_hash": user[3]}
      # return user only if password matches
      if bcrypt.checkpw(self.plain_password.encode(), user_formatted["password_hash"].encode()):
        return user_formatted
      return None
    return None

  def add_user(self):
    password_hash = bcrypt.hashpw(self.plain_password.encode(), bcrypt.gensalt()).decode()
    common.sql_write("INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s);", [self.email, self.name, password_hash])
