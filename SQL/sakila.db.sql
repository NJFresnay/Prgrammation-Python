SELECT title, release_year, length
FROM film
ORDER BY release_year DESC, title ASC;


SELECT *
FROM actor 
where last_name IS 'JACKMAN'


SELECT count(name)
FROM category
-- group by actor
select first_name, last_name  FROM actor GROUP BY last_name


-- Moyenne des prêts
SELECT AVG(rental_duration) as 'Moyenne', min(rental_duration) as 'min', max(rental_duration) as 'max'
FROM film

SELECT timediff(return_date, rental_date)
from rental


-- nombre de film par année 

SELECT address || ' ' || postal_code as 'Adresse concatenée' from address
