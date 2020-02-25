select * from manufacturers;
select * from products;

-- 1. Select the names of all the products in the store.
select name from products;
-- 2. Select the names and the prices of all the products in the store.
select name, price from products;
--3. Select the name of the products with a price less than or equal to $200.
select name from products where price <= 200;
--4. Select all the products with a price between $60 and $120.
select * from products where price between 60 and 120;
--5. Select the name and price in cents (i.e., the price must be multiplied by 100).
select name, price * 100 as priceCents from products;
--6. Compute the average price of all the products.
select avg(price) from products;
--7. Compute the average price of all products with manufacturer code equal to 2.
select avg(price) from products where manufacturer = 2;
--8. Compute the number of products with a price larger than or equal to $180.
select count(price) from products where price >= 180;
--9. Select the name and price of all products with a price larger than or equal to $180,
-- and sort first by price (in descending order), and then by name (in ascending order).
select name, price from products where price >= 180 order by price desc, name asc;
--10. Select all the data from the products, including all the data for each product's manufacturer.
SELECT p.*, m.name
FROM products p
    INNER JOIN manufacturers m ON p.manufacturer = m.code;