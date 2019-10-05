# @@@@@ IMPORTS @@@@@@
import mysql.connector
import socket

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pybank"
)

# create cursor
mysqli = conexao.cursor()

# close connection
mysqli_close = conexao.close()