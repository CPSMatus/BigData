CREATE TABLE CONVOCATORIA_SELECCION (
    CONVOCATORIA_SELECCION_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    FECHA_PARTIDO DATE,
    PARTIDO VARCHAR2(50),
    ID_JUGADOR NUMBER NOT NULL,
    ES_AMISTOSO NUMBER,


    PRIMARY KEY(CONVOCATORIA_SELECCION_ID),
    FOREIGN KEY(ID_JUGADOR) REFERENCES JUGADOR(JUGADOR_ID)
);