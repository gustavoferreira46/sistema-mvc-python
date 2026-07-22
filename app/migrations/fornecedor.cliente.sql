create table fornecedor
(
	id integer not null auto_increment, 
    razao_social varchar (50) not null, 
    nome_fantasia varchar(50) not null, 
    cnpj char(14) not null, 
    sla_atendimento varchar (50),
	primary key(id)
);