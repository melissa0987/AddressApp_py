
-- TABLE CREATION
DROP TABLE IF EXISTS flask_addresses;

CREATE TABLE flask_addresses (
    name VARCHAR(150) PRIMARY KEY,
    street VARCHAR(150) NOT NULL,
    city VARCHAR(150) NOT NULL,
    province VARCHAR(150) NOT NULL
);


-- INSERTS
INSERT INTO FLASK_ADDRESSES VALUES ('Ayy', '1st street','One city', 'Quebec' );
INSERT INTO FLASK_ADDRESSES VALUES ('Bee', '2nd street','Two city', 'Ontario' );
INSERT INTO FLASK_ADDRESSES VALUES ('See', '3rd street', 'Three city', 'British Columbia');
INSERT INTO FLASK_ADDRESSES VALUES ('Di', '4th street', 'Fourth city', 'Manitoba');
INSERT INTO FLASK_ADDRESSES VALUES ('Eeh', '5th street', 'Fifth city', 'Winnipeg');
INSERT INTO FLASK_ADDRESSES VALUES ('Eff', '6th street', 'Sixth city', 'Alberta');

COMMIT;

select name, street, city, province from FLASK_ADDRESSES ;
-- SELECT version();