
CREATE TABLE AN_JUGADOR_SUPLEMENTO (
    JUGADOR_SUPLEMENTO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,

    CONSUMO NUMBER,
    ID_SUPLEMENTO NUMBER NOT NULL,
    CUMPLIMEINTO NUMBER,

    PRIMARY KEY(JUGADOR_SUPLEMENTO_ID),
    FOREIGN KEY(ID_SUPLEMENTO) REFERENCES AN_SUPLEMENTO(SUPLEMENTO_ID)

);