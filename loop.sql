DELETE FROM types
WHERE type_name LIKE('%Name%');

select * from types;

DO $$
DECLARE
	type_name types.type_name%TYPE;
	type_id types.type_id%TYPE;
	
BEGIN
	type_name:= 'Name';
	type_id:= 6;
	FOR num IN 1..5
		LOOP
			INSERT INTO types(type_id, type_name)
			VALUES(type_id+num,num||' '||type_name);
		END LOOP;
END;
$$

select * from types;
