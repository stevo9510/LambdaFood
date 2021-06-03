Use ProjectTwoDb;

-- Create Tables
create table FoodCategory
(
	id int not null,
	category_name varchar(50) not null,
	icon_path varchar(512) null, 
	PRIMARY KEY (id)
);

create table Food
(
	id int not null auto_increment,
	food_name varchar(50) not null,
	food_description varchar(250) null,
	image_url varchar(2048) null,
	food_category_id int,
	PRIMARY KEY (id),
	FOREIGN KEY (food_category_id) REFERENCES FoodCategory(id)
);

create table FoodIngredient
(
	food_id int not null,
	ingredient_name varchar(50) not null,
	sequence int null,

	PRIMARY KEY (food_id, ingredient_name),
	FOREIGN KEY (food_id) REFERENCES Food(id)
);

-- Insert static / enum data
insert into FoodCategory
(
	id,
	category_name,
	icon_path
)
values (1, 'American', 'images/american_food.png'), 
        (2, 'Italian', 'images/italian_food.png'), 
        (3, 'Mexican', 'images/indian_food.png');
