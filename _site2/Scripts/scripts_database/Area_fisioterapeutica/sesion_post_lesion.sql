CREATE TABLE AF_SESION_POST_LESION (
    SESION_POST_LESION_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,

    FECHA DATE,
    ID_HORARIO NUMBER,
    ID_LUGAR_SESION NUMBER,
    ID_LESION_MEDICA NUMBER,
    PERCEPCION_DOLOR NUMBER(2,0),
    OBSERVACIONES VARCHAR(100)

    PRIMARY KEY(TRABAJO_FUERZA_ID),
    FOREIGN KEY(ID_HORARIO) REFERENCES HORARIO(HORARIO_ID),
    FOREIGN KEY(ID_LUGAR_SESION) REFERENCES LUGAR_ENTRENAMIENTO(LUGAR_ENTRENAMIENTO_ID),
    FOREIGN KEY(ID_LESION_MEDICA) REFERENCES LESION_MEDICA(LESION_MEDICA_ID)
);
