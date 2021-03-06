CREATE TABLE AF_SESION_TRABAJO_CANCHA (
    SESION_TRABAJO_CANCHA NUMBER GENERATED BY DEFAULT AS IDENTITY,

    ID_SESION_FISIOTERAPIA NUMBER,
    ID_SUBTIPO_TRABAJO_CANCHA NUMBER,


    PRIMARY KEY(SESION_TRABAJO_CANCHA),
    FOREIGN KEY(ID_SESION_FISIOTERAPIA) REFERENCES AF_SESION_FISIOTERAPIA(SESION_FISIOTERAPIA_ID),
    FOREIGN KEY(ID_SUBTIPO_TRABAJO_CANCHA) REFERENCES AF_SUBTIPO_TRABAJO_CANCHA(SUBTIPO_TRABAJO_CANCHA_ID)
);
