import psycopg2

stringa_connessione = "host='localhost' dbname='data_science' user='postgres' password='postgres'"

connection = psycopg2.connect(stringa_connessione)
cursor = connection.cursor()

#Elimino la tabella se già esiste
cursor.execute("DROP TABLE IF EXISTS accidents1")

#Creo la tabella 
cursor.execute("""
CREATE TABLE accidents1 (
    Data VARCHAR(50),
    Countries VARCHAR(50),
    Local VARCHAR(50),
    Industry_Sector VARCHAR(50),
    Accident_Level VARCHAR(50),
    Potential_Accident_Level VARCHAR(50),
    Genre VARCHAR(50),
    Employee_OU_Terceiro VARCHAR(50),
    Risco_Critico VARCHAR(50)
);
""")




# Apro il file CSV
with open(r'C:\Users\Marti\Desktop\Progetto Data\archive\IHMStefanini_industrial_safety_and_health_database.csv', 'r') as file:
    # Salta la prima riga (intestazione)
    next(file)

    # Itera su ogni riga del file
    for line in file:
        # Dividi la riga in base al separatore (virgola nel nostro caso)
        values = line.strip().split(',')
        # Inserisco i valori nella tabella
        cursor.execute("INSERT INTO accidents1 (Data, Countries, Local, Industry_Sector, Accident_Level, Potential_Accident_Level, Genre, Employee_OU_Terceiro, Risco_Critico) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", values)

# Salvo le modifiche
connection.commit()


connection.commit()
cursor.close()
connection.close()
