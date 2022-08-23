import sqlite3

conn = sqlite3.connect('SQLDatabase.db')

conn.execute('''CREATE TABLE STATES
         (ID INT PRIMARY KEY     NOT NULL,
            STATE           TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE CATEGORIES
            (ID INT PRIMARY KEY     NOT NULL,
            CATEGORY           TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE SUBCATEGORIES
          (ID INT PRIMARY KEY     NOT NULL,
            SUBCATEGORY           TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE COMPANYDETAILS
            (ID INT PRIMARY KEY     NOT NULL,
            COMPANYNAME           TEXT    NOT NULL,
            ABOUT          TEXT    NOT NULL,
            STATES            TEXT    NOT NULL,
            SUBCATEGORY           TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE JOBS
            (ID INT PRIMARY KEY     NOT NULL,
            COMPANYNAME           TEXT    NOT NULL,
            JOBPOSITION          TEXT    NOT NULL,
            LOCATION           TEXT    NOT NULL);''')
            

#run this code only for the first time.