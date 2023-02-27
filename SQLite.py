import sqlite3

#connect to database
# conn = sqlite3.connect("accounts.db")

#create a cursor
# c = conn.cursor()

#create a table
# c.execute(""" CREATE TABLE accounts (
#     username text,
#     password text
# )""")

#this code will input many accounts into the database
# many_accounts = [
#                     ('jake', 'state_farm'),
#                     ('kyle', 'monster_energy'),
#                     ('chad', 'protein')
#                 ]
#
# c.executemany("INSERT INTO accounts VALUES(?,?)", many_accounts)

# the username and password from the login page will be passed into the values parentheses
# c.execute("INSERT INTO accounts VALUES ('nicholas', 'test')")

#query the database, rowid is the unique id for every element
# c.execute("SELECT rowid, * FROM accounts")
# c.execute("SELECT * FROM accounts WHERE username = 'nicholas'") # the WHERE allows to search the db for certain items
# c.execute("SELECT * FROM accounts WHERE username LIKE 'ni%'") like combined with % finds text that closely matches it
# print(c.fetchall())  # this grabs all the items
# c.fetchone()  # this grabs the last item
# c.fetchmany(3)  # this allows the programmer how many items they want to grab

#update records
# c.execute("""UPDATE accounts SET username = 'joe'
#              WHERE rowid = 1
#
# """) # conn.commit will need to run after this command to commit changes

#orders the tables information
# c.execute("SELECT rowid, * FROM accounts ORDER BY rowid DESC") # replacing desc with username would order by alphabet

#delete records
# c.execute("DELETE from accounts WHERE rowid = 1")
# will also need to use conn.commit afterwards

#limit results
# c.execute("SELECT rowid, * FROM accounts LIMIT 2")

#delete a table
# c.execute("DROP TABLE accounts")
#will need to use conn.commit afterwards

#commit the command
# conn.commit()

#close the connection
# conn.close()
