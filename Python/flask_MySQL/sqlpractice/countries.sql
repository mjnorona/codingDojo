SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY percentage DESC;

select countries.name, count(cities.id) as total
from countries
left join cities
on countries.id = cities.country_id
group by countries.id
order by total desc;

select countries.name, cities.name, cities.population
from cities, countries
where countries.name = "Mexico" and countries.id = cities.country_id and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage
from countries
left join languages
on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;

select countries.name, countries.surface_area, countries.population
from countries
where surface_area < 501 and population > 100000;

select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where government_form = "Constitutional Monarchy" and capital > 200 and life_expectancy > 75;

select countries.name, cities.name, cities.district, cities.population
from cities, countries
where countries.id = cities.country_id and cities.district = "Buenos Aires" and cities.population > 500000;

select countries.region, count(countries.id) as total
from countries
group by countries.region
order by total desc;


