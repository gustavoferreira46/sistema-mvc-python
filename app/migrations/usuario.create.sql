create table usuario
(
	id integer not null auto_increment, 
    nome varchar(50) not null, 
    email varchar (80) not null, 
    data_nascimento char (12) not null,
    primary key(id)
);
