--# write your SQL statement here: 
-- you are given a table 'sumtriangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.

SELECT n,
       CASE
          WHEN n > 0 THEN
             n * ( n + 1 ) * ( n + 2 ) / 6
          ELSE
             0
       END AS res
  FROM sumtriangular;