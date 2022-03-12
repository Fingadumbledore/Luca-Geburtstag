CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    userpassword varchar(32) NOT NULL,
    PRIMARY KEY (id)
);