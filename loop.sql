DELETE FROM types
WHERE name LIKE('%Name%');

select * from types;

DO $$
DECLARE
	name types.name%TYPE;
	id types.id%TYPE;
	
BEGIN
	name:= 'Name';
	id:= 6;
	FOR num IN 1..5
		LOOP
			INSERT INTO types(id,name)
			VALUES(id+num,num||' '||name);
		END LOOP;
END;
$$

select * from types;
