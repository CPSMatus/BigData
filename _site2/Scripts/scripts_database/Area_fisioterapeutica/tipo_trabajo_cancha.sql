CREATE TABLE AF_TIPO_TRABAJO_CANCHA(
    TIPO_TRABJO_CANCHA_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_TRABAJO_CANCHA VARCHAR2(30),

    PRIMARY KEY(TIPO_TRABJO_CANCHA_ID)
);



INSERT INTO AF_TIPO_TRABAJO_CANCHA(NOMBRE_TRABAJO_CANCHA)
VALUES('COORDINACION');


INSERT INTO AF_TIPO_TRABAJO_CANCHA(NOMBRE_TRABAJO_CANCHA)
VALUES('FUERZA RESISTENCIA');


INSERT INTO AF_TIPO_TRABAJO_CANCHA(NOMBRE_TRABAJO_CANCHA)
VALUES('ESTABILIDAD');


INSERT INTO AF_TIPO_TRABAJO_CANCHA(NOMBRE_TRABAJO_CANCHA)
VALUES('EQUILIBRIO');


INSERT INTO AF_TIPO_TRABAJO_CANCHA(NOMBRE_TRABAJO_CANCHA)
VALUES('AEROBICOS');
