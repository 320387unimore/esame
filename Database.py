import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

stringa_connessione = "host='localhost' user='postgres' password='postgres'"

connection = psycopg2.connect(stringa_connessione)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cursor = connection.cursor()

#Assegno il nome del database che voglio creare alla variabile db_name
db_name = "data_science"
#Elimino il database se già esiste
cursor.execute("DROP DATABASE IF EXISTS "+db_name)
#Creo il database 
cursor.execute("CREATE DATABASE "+db_name)

connection.commit()

cursor.close()

connection.close()
