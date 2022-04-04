CREATE TABLE AF_SESION_TERAPIA_FUERZA (
    SESION_TERAPIA_FUERZA NUMBER GENERATED BY DEFAULT AS IDENTITY,
    ID_SESION_FISIOTERAPIA NUMBER,


    PRIMARY KEY(SESION_TERAPIA_FUERZA),
    FOREIGN KEY(ID_SESION_FISIOTERAPIA) REFERENCES AF_SESION_FISIOTERAPIA(SESION_FISIOTERAPIA_ID),
    ID_TIPO_FORTALECIMIENTO NUMBER,
    ID_SUBTIPO_TRABAJO_FUERZA NUMBER,


    FOREIGN KEY(ID_SESION_POST_LESION) REFERENCES SESION_POST_LESION(SESION_POST_LESION_ID),
    FOREIGN KEY(ID_TIPO_FORTALECIMIENTO) REFERENCES AF_TIPO_FORTALECIMIENTO(TIPO_FORTALECIMIENTO_ID),
    FOREIGN KEY(ID_SUBTIPO_TRABAJO_FUERZA) REFERENCES AF_SUBTIPO_TRABAJO_FUERZA(SUBTIPO_TRABAJO_FUERZA_ID)
);
