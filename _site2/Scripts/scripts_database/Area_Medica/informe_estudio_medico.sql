

CREATE TABLE informe_estudio_medico (
    INFORME_ESTUDIO_MEDICO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    ID_ESTUDIO_MEDICO  NUMBER,
    ID_LESION_MEDICA  NUMBER,
    OBSERVACIONES VARCHAR2(2000),

    FOREIGN KEY(ID_ESTUDIO_MEDICO) REFERENCES estudio_medico(ESTUDIO_MEDICO_ID),
    FOREIGN KEY(ID_LESION_MEDICA) REFERENCES lesion_medica(LESION_MEDICA_ID),
    PRIMARY KEY(INFORME_ESTUDIO_MEDICO_ID)
);