import mysql.connector
con = mysql.connector.connect(host = 'localhost', user='root', password='vinit123')
cur = con.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS username_pass;')
print('Database Created')
cur.execute('USE username_pass;')
print('Database Selected')
cur.execute('CREATE TABLE data (Username varchar(20), Password varchar(20));')
print('Table Created')
