-- SQL-команды для создания таблиц
create table orders_data
(
	order_id int primary key not null,
	customer_id char(5) not null,
	employee_id int not null,
	order_date date not null,
	ship_city varchar(50) not null
);
create table employees_data
(
	employee_id int primary key not null,
	first_name varchar(20) not null,
	last_name varchar(20) not null,
	title varchar(50) not null,
	birth_date date not null,
	notes varchar(500)

);
create table customers_data
(
	customer_id char(5) primary key not null,
	company_name varchar(50) not null,
	contact_name varchar(40) not null
);
