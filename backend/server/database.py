import os, sys, sqlite3

# Existenz feststellen
if os.path.exists("login.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

# Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("login.db")

# Datensatz-Cursor erzeugen
cursor = connection.cursor()

# Datenbanktabelle erzeugen
sql = "CREATE TABLE user(" \
      "username TEXT, " \
      "password TEXT, " \
      "info TEXT)"
cursor.execute(sql)

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Horst', " \
      "'#ananas.geschnetzeltes3', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('admin', " \
      "'admin', 'Admin')"
cursor.execute(sql)
connection.commit()


# Verbindung beenden
connection.close()