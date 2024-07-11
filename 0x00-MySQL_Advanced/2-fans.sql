-- Count Non unique fans per country
-- Order Results by number of fans
SELECT origin AS origin , COUNT(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
