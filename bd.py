# @@@@@ IMPORTS @@@@@@
import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "pybank",
    user = "postgres",
    password = "post"
)

# create cursor
cur = con.cursor()


# close connection
con.close()