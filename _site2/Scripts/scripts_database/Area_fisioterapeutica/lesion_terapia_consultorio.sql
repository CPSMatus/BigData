CREATE TABLE AF_LESION_TERAPIA_CONSULTORIO (
    AF_LESION_TERAPIA_CONSULTORIO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,

    ID_SESION_POST_LESION NUMBER,
    ID_GRUPO_MUSCULAR NUMBER,
    ID_SUBTIPO_TERAPIA_CONSULTORIO NUMBER,

    PRIMARY KEY(AF_LESION_TERAPIA_CONSULTORIO_ID),
    FOREIGN KEY(ID_SESION_POST_LESION) REFERENCES AF_SESION_POST_LESION(SESION_POST_LESION_ID),
    FOREIGN KEY(ID_GRUPO_MUSCULAR) REFERENCES GRUPO_MUSCULAR(GRUPO_MUSCULAR_ID),
    FOREIGN KEY(ID_SUBTIPO_TERAPIA_CONSULTORIO) REFERENCES AF_SUBTIPO_TERAPIA_CONSULTORIO(SUBTIPO_TERAPIA_CONSULTORIO_ID)
);
