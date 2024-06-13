create table Recipe (
	Recipe_id integer,
	Name varchar(30) not null,
	Instructions text,
	constraint Recipe_PK primary key (Recipe_id)
);

create table Ingredient (
	Ingredient_id integer,
	Name varchar(30) not null,
	constraint Ingredient_PK primary key (Ingredient_id)

);

create table RecipeIngredient (
	Recipe_id integer,
	Ingredient_id integer,
	Quantity integer not null,
	Unit varchar(30) not null,
	constraint RecipeIngredient_PK primary key (Recipe_id, Ingredient_id),
	constraint RecipeIngredient_FK1 foreign key (Recipe_id) references Recipe(Recipe_id)
		on update cascade
		on delete cascade,
	constraint RecipeIngredient_FK2 foreign key (Ingredient_id) references Ingredient(Ingredient_id)
		on update cascade
		on delete cascade
);

create table Stock (
	Stock_id integer,
	Quantity integer,
	Ingredient_id integer not null,
	constraint Stock_PK primary key (Stock_id),
	constraint Stock_FK foreign key (Ingredient_id) references Ingredient(Ingredient_id)
		on update cascade
		on delete cascade
);