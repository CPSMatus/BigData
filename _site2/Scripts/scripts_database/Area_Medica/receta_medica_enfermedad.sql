CREATE TABLE receta_medica_enfermedad (
    RECETA_MEDICA_ENFERMEDAD_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    PROPORCIONADO NUMBER (2),
    ID_MEDICAMENTO NUMBER,
    ID_ENFERMEDAD NUMBER,

    PRIMARY KEY(RECETA_MEDICA_ENFERMEDAD_ID),


    FOREIGN KEY(ID_MEDICAMENTO) REFERENCES medicamento(MEDICAMENTO_ID),
    FOREIGN KEY(ID_ENFERMEDAD) REFERENCES ENFERMEDAD(ENFERMEDAD_ID)
);
