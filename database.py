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
      "info TEXT);"
cursor.execute(sql)

sql = "create table Items(\
       ItemId int not null,\
       ItemName text not null,\
       ItemBeschreibung text not null);"
cursor.execute(sql)

def iv(id, name, besch):
      sql = f"INSERT INTO Items VALUES({id},\'{name}\',\'{besch}\');"
      connection = sqlite3.connect("login.db")

      # Datensatz-Cursor erzeugen
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      connection.close()

iv(0, 'KALLAX', 'Regal, 77x147 cm')
iv (1, 'ALEX', 'Schreibtisch, 120x60 cm')
iv(2, 'MICKE', 'Schreibtisch, 142,50 cm')
iv(3, 'BEKANT', 'Ecktisch links, 160x110 cm')
iv(4, 'MALM', 'Bettgestell mit Aufbewahrung, weiss, 140x200 cm')
iv(5, 'IDASEN', 'Hochschr. m Schublade und Türen, 45x172 cm')
iv(6, "RASKOG", "Servierwagen, gelb, 35x45x78 cm")
iv(7, "MALM", "Schreibtisch mit Ausziehplatte, weiss, 151x65 cm")
iv(8, "BYGGET", "Recamiere/Bettsofa, Knisa/Dunkelgrau mit Stauraum")
iv(9, "IDASEN", "Schubladenelement auf Rollen, dunkelgrau, 42x61")
iv(23, "ILLUMINATEN", "eine kurzlebige Geheimgesellschaft")
iv(42, "ANTWORT", "ultimative Frage nach dem Leben, dem Universum und dem ganzen Rest")
# iv()



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

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.J.Limburg', " \
      "'Ananaskopf', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('T.Zimmer', " \
      "'Affe', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Behmke', " \
      "'Fahradhelm', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('D.Welsch', " \
      "'Deano', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Scholze', " \
      "'Walnuss', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Lenin', " \
      "'IchMarxs', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Morgen', " \
      "'rdr2', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Sonic', " \
      "'Hedgehog', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Pac-Man', " \
      "'hunger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Mario', " \
      "'Spagetti', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Link', " \
      "'Zelda', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.Croft', " \
      "'.T.R.A.I.D.E.R.', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('D.Kong', " \
      "'Affen-Auflauf', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Dr.Jones', " \
      "'Peitsche', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.Skywalker', " \
      "'Lichtschwert', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Sparrow', " \
      "'Zopf', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Krueger', " \
      "'Handschuh', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Gump', " \
      "'laufen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Bond', " \
      "'geschüttelt', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Lecter', " \
      "'Das Schweigen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.McFly', " \
      "'Zeitreisen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Spencer', " \
      "'Bohnen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('D.Khan', " \
      "'1162', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Polo', " \
      "'Reisen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Gutenberg', " \
      "'Buchdruck', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Kolumbus', " \
      "'Amerika', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.d.Vici', " \
      "'Mahlen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('V.d.Gama', " \
      "'Segeln', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('N.Kopernikus', " \
      "'Sonnensystem', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Magellan', " \
      "'Seeweg nach Indien', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Luther', " \
      "'Reformation', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.Galilei', " \
      "'Fernrohr', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('W.Shakespeare', " \
      "'Langweilig', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Kepler', " \
      "'Sterne', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('I.Newton', " \
      "'Apfel', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.W.Leibniz', " \
      "'Mathe', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Vivaldi', " \
      "'Musik', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.S.Bach', " \
      "'Orgel', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.F.Händel', " \
      "'Haleluja', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Spencer', " \
      "'Bohnen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Cook', " \
      "'Reisen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.Washingon', " \
      "'1. Präsident Amerika', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.W.v.Goethe', " \
      "'Langweilig', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('W.A.Mozart', " \
      "'Musik', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()
# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Schiller', " \
      "'Geschichten', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('N.Bonaparte', " \
      "'Franzose', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.v.Humboldt', " \
      "'Entdecker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.v.Beethoven', " \
      "'Taub', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.F.Gauß', " \
      "'Rechnen', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Heine', " \
      "'Dichter', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Wilhelm 1', " \
      "'Deutscher Kaiser', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Lincoln', " \
      "'Bürgerkrieg', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Darwin', " \
      "'Evolution', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Chopin', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.Verdi', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('O.v.Bismarck', " \
      "'Reichskanzler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('K.Marx', " \
      "'Egal was du kochst ich marxs', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Victoria', " \
      "'Russland', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Verne', " \
      "'in 80 Tagen um die Welt', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Twain', " \
      "'Tom Sawyer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('P.Tschaikowski', " \
      "'Komponist', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('W.C.Röntgen', " \
      "'X-Ray', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('T.A.Edison', " \
      "'Glühbirne', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('V.V.Gogh', " \
      "'Maler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Freud', " \
      "'Psyche', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Wilhelm II', " \
      "'Letzter Deuscher Kanzler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Curie', " \
      "'Radioaktivität', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Gandhi', " \
      "'Inder', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Lenin', " \
      "'Sozialismus', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('W.Churchill', " \
      "'2WW England', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('K.Adenauer', " \
      "'Erster Bundeskanzler nach 2ww', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Einstein', " \
      "'E=MC²', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('P.Picasso', " \
      "'Maler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Christie', " \
      "'Tod auf dem Niel', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('E.Hemingway', " \
      "'Schriftsteller', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Walt Disney', " \
      "'Micky Maus', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.Armstrong', " \
      "'Trompeter', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Lindgren', " \
      "'Schriftstellerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('W.Brandt', " \
      "'Politiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.F.Kennedy', " \
      "'US Präsident', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('N.Mandela', " \
      "'Politiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Scholl', " \
      "'Wiederstandskämpferin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Monroe', " \
      "'Schauspielerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Guevara', " \
      "'WIederstandskämpfer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.L.King', " \
      "'Bürgerrechtler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Frank', " \
      "'Tagebuch', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('N.Armstrong', " \
      "'Apollo 11', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Kohl', " \
      "'Bundeskanzler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('E.Presley', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Lennon', " \
      "'Beatles', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Ali', " \
      "'Boxer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Marley', " \
      "'Singer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Jackson', " \
      "'Singer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Merkel', " \
      "'Bundeskanzlerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('K.Zuse', " \
      "'1 Computer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Nixdorf', " \
      "'Computer Pionier', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Turing', " \
      "'Enigma', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Castro', " \
      "'Kuba', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.Fröbe', " \
      "'Goldfinger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.G.S.v.Staufenberg', " \
      "'Hitler Attentat', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('D.Bonhoeffer', " \
      "'Theologe', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Beatles', " \
      "'yellow submarine', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Dylan', " \
      "'Nobelpreisträger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Rolling Stones', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Berry', " \
      "'RockMusik', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Hendrix', " \
      "'E Gitarre', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Brown', " \
      "'Tänzer', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('L.Richard', " \
      "'Rock n Roll', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Franklin', " \
      "'Pianistin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('R.Charles', " \
      "'Sänger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The beatch boys', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Holly', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Led Zeppelin', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Wonder', " \
      "'Pop sänger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Cooke', " \
      "'Sänger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Waters', " \
      "'Bluesmusiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('M.Gaye', " \
      "'R&B Sänger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Tge Vevelet Underground', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Diddley', " \
      "'Rock n Roll', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('O.Redding', " \
      "'Flugzeugabsturz', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('U2', " \
      "'Irische Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.Springsteen', " \
      "'60MioAlben', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.L.L', " \
      "'Country Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('F.Domino', " \
      "'Piano Blues', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Ramones', " \
      "'NewYork', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Prince', " \
      "'Schauspieler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Clash', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Who', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Nirvana', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Cash', " \
      "'Country Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Robison & the miracles', " \
      "'soulgruppe', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Everly Brothers', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('N.Young', " \
      "'Amerikanischer Staatsbürger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Madonna', " \
      "'Autorin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('R.Orbison', " \
      "'Pop Country', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('D.Bowie', " \
      "'schauspieler', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Simon & Garfunkel', " \
      "'Folk Rock Duo', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Doors', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Van Morrison', " \
      "'Komponist', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Sly & the Family Stone', " \
      "'Funk Soul band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Public Enemy', " \
      "'HipHop', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Byrds', " \
      "'Pioniere', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Joplin', " \
      "'Blues Sängerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('P.Smith', " \
      "'Lyrikerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Run-D.M.C', " \
      "'HipHop', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Elton John', " \
      "'Sänger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Band', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Pink Floyd', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Queen', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Allman Brothers Band', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Wolf', " \
      "'Blues Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('E.Clapton', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Dr Dre', " \
      "'Rapper', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Grateful Dead', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Parliament', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Aerosmith', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('S.Pistols', " \
      "'Punk Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Metallica', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Mitchell', " \
      "'Malerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('T.Turner', " \
      "'Sängerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('P.Specor', " \
      "'Musikproduzent', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The kinks', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('A.Green', " \
      "'Prediger', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Cream', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Temptations', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Wilson', " \
      "'Sängerin', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Police', " \
      "'Wave Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('B.F.Zappa', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('AC/DC', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Radiohead', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('H.Williams', " \
      "'Country Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Eagles', " \
      "'Country Rock Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Shirelles', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Beastie Boys', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Stoogers', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Four Tops', " \
      "'Soul Gesang', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('E.Costello', " \
      "'Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Drifters', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Creedence Clearwater Revival', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Eminem', " \
      "'Rapper', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('J.Taylor', " \
      "'Gitarist', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Black Sabbath', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('T.Shakur', " \
      "'Rapper', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('G.Parsons', " \
      "'Komponist', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Jay-Z', " \
      "'Rapper', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Yardbirds', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Santana', " \
      "'Gitarist', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('T.Pretty', " \
      "'Musik', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Guns n Roses', " \
      "'Hard Rock Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Booker T & the M.G.s', " \
      "'R&B Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Nine Inch Nail', " \
      "'Musik Projekt', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Lynrd Skynyrd', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('The Supremes', " \
      "'Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('R.E.M', " \
      "'Rockband', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Mayfield', " \
      "'SoulMusiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('C.Perkins', " \
      "'Country Musiker', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO user VALUES('Talking Heads', " \
      "'Rock Band', 'Standard Nutzer')"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()