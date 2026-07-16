use mini_erp;

create table cliente
(
	id integer not null auto_increment,
    nome varchar(50) not null, 
    email varchar(100) not null,
    data_nascimento varchar (12) not null,
    limite_credito decimal (10,2) not null,
    primary key(id)
);