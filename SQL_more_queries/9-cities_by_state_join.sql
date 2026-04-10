-- uhyudsjdsugihjdskglsdzv
SELECT cities.id, cities.name, states.name
FROM cities JOIN states ON cities.state_id=state_id
ORDER by cities.id ASC;
