CREATE TABLE AN_SUPLEMENTOS (
    SUPLEMENTOS_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_SUPLEMENTO VARCHAR2(30),
    CANTIDAD NUMBER NOT NULL,

    PRIMARY KEY(SUPLEMENTOS_ID)
);

INSERT INTO AN_SUPLEMENTOS(NOMBRE_SUPLEMENTO,CANTIDAD)
VALUES('CREATINA', );