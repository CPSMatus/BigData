CREATE TABLE AN_PLIEGUES (
    PLIEGUES_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    ID_JUGADOR NUMBER NOT NULL,
    FECHA_MEDICION DATE,
    SUMATORIA_6_PLIEGUES FLOAT,
    SUMATORIA_8_PLIEGUES FLOAT,
    GC_DUMIN FLOAT,
    GC_YUHASZ FLOAT,
    GC_PROMEDIO FLOAT,
    GC_EXACTO FLOAT,
    ESTIMACION_PESO_IDEAL FLOAT,
    MASA_MUSCULAR_TOTAL FLOAT,
    ID_INTERPRETACION_MASA_MUSCULAR NUMBER,
    FOTOGRAFIA_JUGADOR_ BLOB,
    ID_JUGADOR NUMBER NOT NULL,

    PRIMARY KEY(PLIEGUES_ID),
    FOREIGN KEY(ID_JUGADOR) REFERENCES JUGADOR(JUGADOR_ID),
    FOREIGN KEY(ID_INTERPRETACION_MASA_MUSCULAR) REFERENCES AN_INTERPRETACION_MASA_MUSCULAR(INTERPRETACION_MASA_MUSCULAR_ID)

);
