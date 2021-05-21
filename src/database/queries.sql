/* Table for userType */
CREATE TABLE userType
(
    id integer NOT NULL,
    type varchar(20) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT UC_userType UNIQUE (id,type)
);
 
/* Examples: */
INSERT INTO userType(id, type) VALUES(1,'admin');
INSERT INTO userType(id, type) VALUES(2,'operator');


/*  Table for User */

CREATE TABLE userDepth
(
    ID bigint NOT NULL,
    userType integer NOT NULL,
    name varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    state boolean NOT NULL,
    phone bigint NOT NULL,
    email varchar(75) NOT NULL,
    password varchar(25) NOT NULL,
    PRIMARY KEY (ID),
    CONSTRAINT "UC_user" UNIQUE (ID, phone, email),
    CONSTRAINT "FK_id_userType" FOREIGN KEY (userType) REFERENCES userType (id)
);
/* Examples */
INSERT INTO userDepth(ID, userType, name, lastname, state, phone, email, password) VALUES(1088597617, 1, 'Jaime', 'Aza', true, 3164277879,'userjjat00@gmail.com','jjatjjat');