CREATE TABLE AF_TIPO_FORTALECIMIENTO (
    TIPO_FORTALECIMIENTO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_TIPO_FORTALECIMIENTO VARCHAR2(30),

    PRIMARY KEY(TIPO_FORTALECIMIENTO_ID)
);



INSERT INTO AF_TIPO_FORTALECIMIENTO(NOMBRE_TIPO_FORTALECIMIENTO)
VALUES('ISOCINERCIAL');


INSERT INTO AF_TIPO_FORTALECIMIENTO(NOMBRE_TIPO_FORTALECIMIENTO)
VALUES('CONCENTRICO');


INSERT INTO AF_TIPO_FORTALECIMIENTO(NOMBRE_TIPO_FORTALECIMIENTO)
VALUES('EXCENTRICO');


INSERT INTO AF_TIPO_FORTALECIMIENTO(NOMBRE_TIPO_FORTALECIMIENTO)
VALUES('ISTONICO');

INSERT INTO AF_TIPO_FORTALECIMIENTO(NOMBRE_TIPO_FORTALECIMIENTO)
VALUES('ISOMETRICO');
