select customer.first_name, customer.last_name, customer.email, address.address
from customer
left join address
on address.address_id = customer.address_id
left join city
on city.city_id = address.city_id
where city.city_id = 312;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name
from film
left join film_category
on film.film_id = film_category.film_id
left join category
on film_category.category_id = category.category_id
where category.name = "Comedy";

select actor.actor_id, actor.first_name, film.title, film.description, film.release_year
from actor
left join film_actor
on actor.actor_id = film_actor.actor_id
left join film
on film_actor.film_id = film.film_id
where actor.actor_id = 5;

select customer.first_name, customer.last_name, customer.email, address.address
from customer
left join store
on customer.store_id = store.store_id
left join address
on customer.address_id = address.address_id
left join city
on city.city_id = address.city_id
where store.store_id = 1 and (city.city_id = 1 or city.city_id = 42 or city.city_id = 312 or city.city_id = 459);

select film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
from film
join film_actor
on film.film_id = film_actor.film_id
join actor
on film_actor.actor_id = actor.actor_id
where actor.actor_id = 15 and film.rating = "G" and film.special_features like "%behind the scenes%";

select film.film_id, film.title, actor.actor_id, actor.first_name
from actor
join film_actor
on film_actor.actor_id = actor.actor_id
join film
on film_actor.film_id = film.film_id
where film.film_id = 369;

select film.title, film.description, film.release_year, film.special_features, category.name
from film
join film_category
on film_category.film_id = film.film_id
join category
on category.category_id = film_category.category_id
where category.name = "drama" and film.rental_rate = 2.99;

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name, actor.actor_id
from film
join film_category
on film.film_id = film_category.film_id
join category
on film_category.category_id = category.category_id
join film_actor
on film.film_id = film_actor.film_id
join actor 
on film_actor.actor_id = actor.actor_id
where actor.first_name = "sandra" and actor.last_name = "kilmer" and category.name = "action"



