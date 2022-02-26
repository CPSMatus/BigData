CREATE TABLE lesion_medica (
    LESION_MEDICA_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    FECHA_ALTA DATE,
    FECHA_BAJA DATE,
    TRATAMIENTO VARCHAR2(5000),
    OBSERVACIONES VARCHAR2(1000),


    ID_MEDICAMENTO NUMBER  ,
    ID_ESTUDIO_MEDICO NUMBER ,
    ID_JUGADOR NUMBER NOT NULL ,
    ID_LUGAR_DIAGNOSTICO NUMBER NOT NULL ,
    ID_SUBTIPO_LESION NUMBER NUMBER NOT NULL,

    PRIMARY KEY(LESION_MEDICA_ID),

    FOREIGN KEY(ID_JUGADOR) REFERENCES jugador(JUGADOR_ID),
    FOREIGN KEY(ID_LUGAR_DIAGNOSTICO) REFERENCES lugar_entrenamiento(LUGAR_ENTRENAMIENTO_ID),
    FOREIGN KEY(ID_SUBTIPO_LESION) REFERENCES subtipo_lesion_medica(SUBTIPO_LESION_ID),
    FOREIGN KEY(ID_MEDICAMENTO) REFERENCES medicamento(MEDICAMENTO_ID),
    FOREIGN KEY(ID_ESTUDIO_MEDICO) REFERENCES estudio_medico(ESTUDIO_MEDICO_ID)
);
