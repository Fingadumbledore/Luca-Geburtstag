CREATE DATABASE main;

CREATE TABLE main.Items (
    Id int not null auto_increment,
    ItemName text not null,
    ItemDescription text
);

CREATE TABLE main.Users ( 
    Id int not null, 
    UserName text not null, 
    Password text not null 
);
