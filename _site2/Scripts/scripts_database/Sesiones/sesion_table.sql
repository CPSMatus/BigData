CREATE TABLE  "SESION"
   (	"SESION_ID" VARCHAR2(10) COLLATE "USING_NLS_COMP" NOT NULL ENABLE,
	"NOMBRE" VARCHAR2(10) COLLATE "USING_NLS_COMP" NOT NULL ENABLE,
	 CONSTRAINT "SESION_PK" PRIMARY KEY ("SESION_ID")
  USING INDEX  ENABLE
   )  DEFAULT COLLATION "USING_NLS_COMP"
/


CREATE OR REPLACE EDITIONABLE TRIGGER  "BI_SESION"
  before insert on "SESION"
  for each row
begin
  if :NEW."SESION_ID" is null then
    select "SESION_SEQ".nextval into :NEW."SESION_ID" from sys.dual;
  end if;
end;

/
ALTER TRIGGER  "BI_SESION" ENABLE
/