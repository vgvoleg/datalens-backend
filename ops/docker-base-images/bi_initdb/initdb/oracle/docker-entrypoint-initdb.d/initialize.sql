CREATE USER datalens IDENTIFIED BY qwerty;
GRANT CREATE SESSION TO datalens;
GRANT CREATE TABLE TO datalens;
GRANT CREATE VIEW TO datalens;
GRANT SELECT ON sys.V_$SESSION TO datalens;
ALTER USER datalens QUOTA UNLIMITED ON USERS;
