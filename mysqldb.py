from decorators import execute_sql
from login import encrypt_password


# read tables
#------------
@execute_sql('read')
def read_table(*_, tb: str) -> str:
  return  f"""
  SELECT *
  FROM {tb}
  """

# check database fields
#----------------------
@execute_sql('read')
def show_field_names() -> str:
  sqlstr = f"""SELECT 
  m.name as table_name, 
  p.name as column_name
FROM 
  sqlite_master AS m
JOIN 
  pragma_table_info(m.name) AS p
ORDER BY 
  m.name, 
  p.cid"""
  return sqlstr

# create tables
# -------------
@execute_sql('write')
def create_table_users() -> str:
  sqlstr = """CREATE TABLE IF NOT EXISTS users (
    user_name VARCHAR(20),
    user_hash VARCHAR(255)
  )"""
  return sqlstr

# insert_users
#-------------
@execute_sql('write')
def insert_users(user: str, pw_hex: hex) -> str:
  return """
  INSERT INTO users
  VALUES (?,?)
  """

def enter_users_in_db():
  usr = input("user: ")
  pw = input("password (can be read, for internal use only: ")
  pw_hex = encrypt_password(pw)
  insert_users(usr,pw_hex)

# delete all entries
#-------------------
@execute_sql('write')
def clean_table(*_, tb: str) -> str:
  return f"""
DELETE FROM {tb}
"""

if __name__ == "__main__":
  pass
  read_table(tb='users')
  #show_field_names()
  #enter_users_in_db()