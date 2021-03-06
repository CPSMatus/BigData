
CREATE TABLE jugador_jornada (
    JUGADOR_JORNADA_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    CALIFICACION NUMBER,
    GOLES_ANOTADOS NUMBER,
    MINUTOS_JUGADOS NUMBER,
    ENTRA NUMBER,
    SALE NUMBER,
    TARJETAS_AMARILLAS NUMBER,
    TARJETAS_ROJAS NUMBER,
    FALTAS_COMETIDAS NUMBER,
    FALTAS_RECIBIDAS NUMBER,

    ID_JUGADOR NUMBER NOT NULL,
    ID_JORNADA NUMBER NOT NULL,

    PRIMARY KEY(JUGADOR_JORNADA_ID),
    FOREIGN KEY(ID_JUGADOR) REFERENCES jugador(JUGADOR_ID),
    FOREIGN KEY(ID_JORNADA) REFERENCES jornada(JORNADA_ID)
);
