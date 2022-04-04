CREATE TABLE estudio_medico (
    ESTUDIO_MEDICO_ID NUMBER GENERATED BY DEFAULT AS IDENTITY,
    NOMBRE_ESTUDIO_MEDICO  VARCHAR(30),
    PRIMARY KEY(ESTUDIO_MEDICO_ID)
);


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('RESONANCIA MAGNETICA');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('ULTRASONIDO');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('ANTIGENO');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('TOMOGRAFIA');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('RAYOS X');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('ELECTROCARDIOGRAMA');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('ANALISIS CLINICO');

INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('PRUEBA DE ESFUERZO');


INSERT INTO estudio_medico(NOMBRE_ESTUDIO_MEDICO)
VALUES('ECOCARDIOGRAMA');
