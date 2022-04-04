CREATE TABLE AF_TIPO_TERAPIA_CONSULTORIO (
    TIPO_TERAPIA_CONSULTORIO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_TTC VARCHAR2(20),

    PRIMARY KEY(TIPO_TERAPIA_CONSULTORIO_ID)
);



INSERT INTO AF_TIPO_TERAPIA_CONSULTORIO(NOMBRE_TTC)
VALUES('AGENTES FISICOS');


INSERT INTO AF_TIPO_TERAPIA_CONSULTORIO(NOMBRE_TTC)
VALUES('ELECTROTERAPIA');


INSERT INTO AF_TIPO_TERAPIA_CONSULTORIO(NOMBRE_TTC)
VALUES('TERAPIA INVASIVA');


INSERT INTO AF_TIPO_TERAPIA_CONSULTORIO(NOMBRE_TTC)
VALUES('TERAPIA MANUAL');


INSERT INTO AF_TIPO_TERAPIA_CONSULTORIO(NOMBRE_TTC)
VALUES('ESTIRAMIENTO');
