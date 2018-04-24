SQL world
1
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id=languages.country_id
WHERE language="slovene"
ORDER BY percentage DESC

3
SELECT cities.name, cities.population
FROM cities 
JOIN countries ON cities.country_id = countries.id
WHERE countries.name ="Mexico" AND cities.population >500000
ORDER BY cities.population DESC

4
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
Where percentage  > 89

6

SELECT countries.name, countries.government_form,capital, life_expectancy
FROM countries 
WHERE government_form
like "Constitutional Monarchy" and capital > 200 and life_expectancy >75

5
SELECT countries.name, countries.surface_area, countries.population
FROM countries 
WHERE countries.surface_area< 501 and countries.population > 100000

7 
SELECT countries.name, cities.name 
FROM countries
JOIN cities ON countries.id=cities.country_id
WHERE countries.name LIKE 'Argentina' AND cities.district LIKE 'Buenos Aires' AND cities.population > 500000

8
SELECT countries.region, COUNT(countries.region)
FROM countries
GROUP BY region
ORDER BY COUNT(countries.region) DESC

2
SELECT countries.name, COUNT(cities.country_id)
FROM cities
JOIN countries ON countries.id = cities.country_id
GROUP BY country_id
ORDER BY COUNT(cities.country_id) DESC