CREATE DATABASE main;

CREATE TABLE main.Items (
    Id int not null,
    ItemName text not null,
    ItemBeschreibung text
);

CREATE TABLE main.Users ( 
    Id int not null, 
    UserName text not null, 
    Password text not null 
);


-- Der befehl muss ausgeführt werden, um diese datei auf dem server auszuführen, wenn der server läuft:
-- mysql -u root -h localhost -P 3306 --password=password < main.sql 

-- oder beim starten:
-- docker exec mysql 'mysql -u root -h localhost -P 3306 --password=password < main.sql'