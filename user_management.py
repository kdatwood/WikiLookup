import sqlite3


def create_user(un, pw, c):
    c.execute("INSERT INTO accounts VALUES (?, ?)", un, pw)


def update_info(pw, c):

    c.execute("""UPDATE accounts SET password = ?""", pw)


def check_user(un, pw):
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()

    c.execute(""" CREATE TABLE accounts (
            username text,
            password text
        )""")

    if c.execute("SELECT * FROM accounts WHERE username = ?", un) and \
       c.execute("SELECT * FROM accounts WHERE username = ?", pw):
        return True
    return False


# def main():
#     conn = sqlite3.connect("accounts.db")
#     c = conn.cursor()
#
#     c.execute(""" CREATE TABLE accounts (
#         username text,
#         password text
#     )""")
#
#
# if __name__ == "__main__":
#     main()
