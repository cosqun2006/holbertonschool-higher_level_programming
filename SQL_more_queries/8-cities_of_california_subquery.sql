-- hygdstyfsjdfhsayigh
SELECT id,name FROM cities where state_id=(SELECT id FROM states where_name='California');
ORDER BY id ASC;

