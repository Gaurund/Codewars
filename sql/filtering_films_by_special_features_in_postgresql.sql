-- Write a PostgreSQL query that selects film_id, the title and special_features 
-- columns from the film table in the DVD rental database, and returns films that 
-- have either "Deleted Scenes" or "Behind the Scenes" as a special feature, 
-- but not both - meaning that if there are "Deleted Scenes", there should not be 
-- "Behind the Scenes" and vice versa. The query should also exclude films that have "Commentaries" as a special feature.

-- Notes:
-- for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
-- The result should be order by title alphabetically, if title is the same - then by film_id in asc order.
-- special_features is the text[] type. It represents a one-dimensional array of values, where each value is of the text data type.

SELECT f.film_id, f.title, f.special_features 
FROM film AS f
WHERE (('Behind the Scenes' = ANY (f.special_features) AND NOT 'Deleted Scenes' = ANY (f.special_features)) OR
(NOT 'Behind the Scenes' = ANY (f.special_features) AND 'Deleted Scenes' = ANY (f.special_features)))
AND NOT 'Commentaries' = ANY (f.special_features)
ORDER BY f.title, f.film_id ASC;