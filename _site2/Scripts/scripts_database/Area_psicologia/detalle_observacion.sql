CREATE TABLE detalle_observacion (
    DETALLE_OBSERVACION_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    CALIFICACION NUMBER,
    ID_OBSERVACION_PSICOLOGICA NUMBER,
    ID_SESION_PSICOLOGICA NUMBER,

    FOREIGN KEY(ID_OBSERVACION_PSICOLOGICA) REFERENCES observacion_psicologica(OBSERVACION_PSICOLOGICA_ID),
    FOREIGN KEY(ID_SESION_PSICOLOGICA) REFERENCES sesion_psicologica(SESION_PSICOLOGICA),
    PRIMARY KEY(DETALLE_OBSERVACION_ID)
);
