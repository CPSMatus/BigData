CREATE TABLE pais (
    PAIS_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE VARCHAR2(50),
    PRIMARY KEY(PAIS_ID)
);


INSERT INTO pais (NOMBRE)
VALUES('Paraguay');


INSERT INTO pais (NOMBRE)
VALUES('Mexico');

INSERT INTO pais (NOMBRE)
VALUES('Uruguay');


INSERT INTO pais (NOMBRE)
VALUES('Brasil');


INSERT INTO pais (NOMBRE)
VALUES('Ghana');


INSERT INTO pais (NOMBRE)
VALUES('Chile');


INSERT INTO pais (NOMBRE)
VALUES('Venezuela');


INSERT INTO pais (NOMBRE)
VALUES('Argentina');
