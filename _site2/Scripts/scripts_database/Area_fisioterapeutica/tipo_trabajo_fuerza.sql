CREATE TABLE AF_TIPO_TRABAJO_FUERZA(
    TIPO_TRABJO_FUERZA_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_TRABAJO_FUERZA VARCHAR2(30),

    PRIMARY KEY(TIPO_TRABJO_FUERZA_ID)
);



INSERT INTO AF_TIPO_TRABAJO_FUERZA(NOMBRE_TRABAJO_FUERZA)
VALUES('FUERZA ANALITICA');


INSERT INTO AF_TIPO_TRABAJO_FUERZA(NOMBRE_TRABAJO_FUERZA)
VALUES('FUERZA LIGA RESISTENCIA');
