import hashlib
import logging
import sqlite3
import os


def generate_salt():
    """
    Function that generates salt for hashing
    """
    # generating salt
    salt = os.urandom(16)
    return salt


def check_password():
    """
    Function that verifies users password in database
    """
    print("Verifying password.")
    log = input("Write your login: ")
    pas = input("Write your password: ")
    # connecting to database
    con = sqlite3.connect('login.db')
    cursor = con.cursor()
    # cheking users hashed password
    cursor.execute("SELECT hash FROM login WHERE username = ?", [log])
    hashcheck = cursor.fetchone()[0]
    # cheking users salt
    cursor.execute("SELECT salt FROM login WHERE username = ?", [log])
    saltcheck = cursor.fetchone()[0]
    # hashing password from user
    new_hash = hashlib.pbkdf2_hmac('sha256', pas.encode('utf-8'), saltcheck, 10000)
    # veryfing both passwords
    if hashcheck == new_hash:
        print("Password is correct.")
    else:
        logging.error("Password is not correct")


class login:
    """
    A class that allows registering password in database using salt and pbkdf2_hmac

    ...

    Atributes
    ---------
    log : str
        login of user
    pas : str
        users password

    Methods
    -------
    set_log(str)
        Sets login to certain string
    get_log
        Returns login
    set_pas(str)
        Sets password to certain string
    get_pas
        Returns password
    register
        Registers user with login, hashed password and salt into database
    """
    def __init__(self, log: str, pas: str):
        """
        Constructs all necessary attributes for the Cezar object

        log : str
            users login
        pas : str
            users password
        """
        self._log = log
        self._pas = pas

    def set_log(self, l):
        """
        Sets log to certain string

        l : str
            New login string
        """
        # login can only be string type
        if isinstance(l, str):
            self._log = l
        else:
            raise TypeError("Login must be string type.")

    def get_log(self):
        """
        Returns log string
        """
        return self._log

    def set_pas(self, p):
        """
        Sets pas to certain string

        p : str
            New password string
        """
        # login can only be string type
        if isinstance(p, str):
            self._pas = p
        else:
            raise TypeError("Password must be string type.")

    def get_pas(self):
        """
        Returns pas string
        """
        return self._pas

    def register(self):
        """
        Registers user in database with login, hashed password and salt using sha256 hashing
        """
        # generating salt
        s = generate_salt()
        # hashing
        h = hashlib.pbkdf2_hmac('sha256', self._pas.encode('utf-8'), s, 10000)
        # connecting to database
        con = sqlite3.connect('login.db')
        cursor = con.cursor()
        # making new record with username, salt and hashed password
        cursor.execute("INSERT INTO login (username, hash, salt) VALUES (?, ?, ?)", (self._log, h, s))
        con.commit()

    # property
    pas = property(get_pas, set_pas)
    log = property(get_log, set_log)
