
CREATE TABLE golstats_jugador_posicion (
    GOLSTATS_JUGADOR_POSICION_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    PACR INT,
    PNACR INT,
    BRD INT,
    BPD INT,

    PACP INT,
    PNCP INT,
    UNO_VS_UNO_DEF_EX INT,
    UNOS_VS_UNO_DEF_NEX INT,
    UNO_VS_UNO_OF_EX INT,
    UNO_VS_UNO_OF_NEX INT,
    BGAP INT,
    AREA_RIVAL INT,
    RECHACES INT,
    ASISTENCIAS INT,
    CENTROS_IZQUIERDA INT,
    CENTROS_DERECHA INT,
    TIRO_GOL INT,

    ID_JUGADOR_JORNADA NUMBER NOT NULL,

    PRIMARY KEY(GOLSTATS_JUGADOR_POSICION_ID),

    FOREIGN KEY(ID_JUGADOR_JORNADA) REFERENCES jugador_jornada(JUGADOR_JORNADA_ID)
);