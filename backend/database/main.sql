CREATE TABLE db.Items (
    Id int not null,
    ItemName text not null,
    ItemBeschreibung text
);

CREATE TABLE db.Users ( 
    Id int not null, 
    UserName text not null, 
    Password text not null 
);