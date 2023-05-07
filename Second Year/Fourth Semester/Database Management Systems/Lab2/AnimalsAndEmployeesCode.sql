--create database AnimalsAndEmployees
--go

use AnimalsAndEmployees
go


create table Specie(
	specieid int primary key IDENTITY,

	speciename varchar(50) NOT NULL,
	speciespecifications varchar(50) NOT NULL,
	endangered int NOT NULL
)

create table Animal(
	animalid int primary key IDENTITY,

	animalname varchar(50) NOT NULL,
	animalweight float NOT NULL,
	gender varchar(10) NOT NULL,

	specieid int foreign key references Specie(specieid)


)


create table Job(
	jobid int primary key IDENTITY,

	jobname varchar(50) NOT NULL,
	jobdescription varchar(50) NOT NULL
)

create table Employee(
	employeeid int primary key IDENTITY,

	employeename varchar(30) NOT NULL,
	phonenumber varchar(50) NOT NULL,
	salary int NOT NULL,
	yearofemployment int NOT NULL,

	jobid int foreign key references Job(jobid)
)

INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Suricata', 'Mamifer care traieste in colonii.',0)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Panda rosu', 'Sta cam tot timpul in copaci. 66 cm lungime.',1)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Urs panda', 'Mananca bambus.',1)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Paun', 'Coada masc. e extravaganta pt a atrage femelele.',0)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Leopard de zapada', 'Are corp slab, coada lunga.',1)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Capra Alpina', 'Are coarne si produce mult lapte.',0)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Ghepard', 'Este foarte rapid.',0)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Gazela', 'Este un animal rumegator si ierbivor.',0)
INSERT INTO Specie(speciename, speciespecifications, endangered) VALUES ('Leu', 'Unul dintre cei mai mari rapitori terestri.',0)

INSERT INTO Animal(animalname, animalweight, gender, specieid) VALUES ('Suricata Suzzy', 0.72, 'F', 1)
INSERT INTO Animal(animalname, animalweight, gender, specieid) VALUES ('Suricata Tony', 0.9, 'M', 1)
INSERT INTO Animal(animalname, animalweight, gender, specieid) VALUES ('Panda rosu Riki',  4, 'F', 2)
INSERT INTO Animal(animalname, animalweight, gender, specieid) VALUES ('Panda rosu Thomas', 3.1, 'M', 2)

select a.animalname, a.specieid, s.speciename from animal a, specie s
where a.specieid = s.specieid


INSERT INTO Job(jobname,jobdescription) VALUES ('Ingrijitor zoo', 'Are grija de animale, le da sa manance etc.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Intretinere zoo', 'Se ocupa cu ingrijirea potecilor si curatarea lor.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Educator', 'Prezent la diferite specii pentru a da informatii.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Entertainer', 'Distreaza copiii.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Vanzator', 'Lucreaza la un magazin.')

select * from job
drop table employee

INSERT INTO
Employee(employeename, phonenumber, salary, jobid, yearofemployment)
VALUES ('Cornel Vascan', '0741648369', 2900, 1, 2005)

INSERT INTO
Employee(employeename, phonenumber, salary, jobid, yearofemployment)
VALUES ('Alexandra Munteanu', '0736056278', 3100, 2, 2009)

INSERT INTO
Employee(employeename, phonenumber, salary, jobid, yearofemployment)
VALUES ('Daniel Lascu','0728573924', 2650, 2, 2016)

INSERT INTO
Employee(employeename, phonenumber, salary, jobid, yearofemployment)
VALUES ('Dana Topa', '07225628564', 2000, 5, 2021)
