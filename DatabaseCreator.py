import mysql.connector
con = mysql.connector.connect(host = 'localhost', user='root', password='root')
cur = con.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS username_pass')
cur.execute('USE username_pass')
cur.execute('CREATE TABLE data (Username varchar(20), Password varchar(20)')
