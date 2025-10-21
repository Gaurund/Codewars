-- # write your SQL statement here: you are given a table 'getcount' with column 'str', return a table with column 'str' and your result in a column named 'res'.

SELECT str,
       (
          SELECT COUNT(*)
            FROM regexp_matches(
             str,
             '[aeiou]',
             'g'
          )
       ) AS res
  FROM getcount;