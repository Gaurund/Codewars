-- You need to write an SQL query to analyze employee hiring and attrition trends from 
-- the year of inception in 2014 up to the year of 2023. The objective is to provide 
-- a clear picture of how many employees joined and left the company each year, reflecting the dynamic changes in the workforce.

-- You are working with an employees table from ABC Kata Solutions' database. Below is the schema for the employees table:

-- id (int): A unique identifier for each employee.
-- joined_date (date): The date on which the employee joined ABC Kata Solutions.
-- left_date (date, nullable): The date on which the employee left ABC Kata Solutions, if applicable
-- Write an SQL query that identifies how many employees joined and left ABC Kata Solutions each year, 
-- from 2014 through 2023. The query should produce a list of years from 2014 to 2023 along with two counts for each year. The result set should have 3 colums:

-- year: The year being reported.
-- joined_quantity: The number of employees who joined ABC Kata Solutions. Refers to the total number 
-- of employees whose joined_date falls within the specific calendar year.
-- left_quantity: The number of employees who left ABC Kata Solutions. Refers to the total number 
-- of employees whose left_date falls within the specific calendar year, indicating they have left the company.
-- Ensure each year from 2014 to 2023 is included in the final report, regardless of whether there were 
-- any hires or departures in those years. The results should be sorted in ascending order by the year.

-- For this sample data:

-- | id | joined_date | left_date  |
-- +----+-------------+------------+
-- | 1  | 2014-03-15  | 2018-05-20 |
-- | 2  | 2014-06-10  | <null>     |
-- | 3  | 2015-07-21  | 2019-12-30 |
-- | 4  | 2017-01-05  | <null>     |
-- | 5  | 2018-11-11  | 2020-03-15 |
-- | 6  | 2019-12-25  | <null>     |
-- | 7  | 2020-07-20  | <null>     |
-- | 8  | 2021-05-27  | 2023-01-10 |
-- the desired output is the following:

-- | year        | joined_quantity | left_quantity |
-- +-------------+-----------------+---------------+
-- | 2014        | 2               | 0             |
-- | 2015        | 1               | 0             |
-- | 2016        | 0               | 0             |
-- | 2017        | 1               | 0             |
-- | 2018        | 1               | 1             |
-- | 2019        | 1               | 1             |
-- | 2020        | 1               | 1             |
-- | 2021        | 1               | 0             |
-- | 2022        | 0               | 0             |
-- | 2023        | 0               | 1             |
-- GLHF!

SELECT year,
COUNT(*) FILTER(WHERE EXTRACT(year FROM joined_date) = year) AS joined_quantity,
COUNT(*) FILTER(WHERE EXTRACT(year FROM left_date) = year) AS left_quantity
FROM generate_series(2014, 2023) AS year, employees
GROUP BY year
ORDER BY year;