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