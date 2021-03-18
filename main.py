from Logging import login, check_password
import sqlite3
import logging


def create_table():
    """
    Function that creates database
    """
    # creating database
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    # creating table login
    query = "CREATE TABLE login(username VARCHAR UNIQUE, hash VARCHAR, salt VARCHAR)"
    cursor.execute(query)


def display_elements():
    """
    Function that displays elements in database to check if everything is working fine
    """
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    # printing all elements
    query = "SELECT * FROM login"
    cursor.execute(query)
    print(cursor.fetchall())


if __name__ == '__main__':
    # asking for login and password twice
    l = input("Login: ")
    p1 = input("Password: ")
    p2 = input("Password again: ")
    # checking if passwords are the same
    if p1 == p2:
        log = login(l, p1)
        # registering
        log.register()
    else:
        logging.error("Passwords are not the same.")

    check_password()

    display_elements()

