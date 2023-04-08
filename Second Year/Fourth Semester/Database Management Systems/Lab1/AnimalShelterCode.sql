--create database AnimalShelter
--go

use AnimalShelter
go

create table Specie(
	specieid int primary key IDENTITY,
	speciename varchar(50) NOT NULL,
	speciespecifications varchar(50) NOT NULL,
)

create table Animal(
	animalid int primary key IDENTITY,
	animalname varchar(50) NOT NULL,
	animaldateofbirth datetime NOT NULL,
	animalweight float NOT NULL,
	gender varchar(10) NOT NULL,
	favouritetoy varchar(50),

	specieid int foreign key references Specie(specieid)


)

select * from Specie
select * from Animal

INSERT INTO Specie(speciename, speciespecifications) VALUES ('Suricata', 'Mamifer care traieste in colonii.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Panda rosu', 'Sta cam tot timpul in copaci. 66 cm lungime.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Urs panda', 'Mananca bambus.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Paun', 'Coada masc. e extravaganta pt a atrage femelele.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Leopard de zapada', 'Are corp slab, coada lunga.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Capra Alpina', 'Are coarne si produce mult lapte.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Ghepard', 'Este foarte rapid.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Gazela', 'Este un animal rumegator si ierbivor.')
INSERT INTO Specie(speciename, speciespecifications) VALUES ('Leu', 'Unul dintre cei mai mari rapitori terestri.')


INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Suricata Suzzy', '2010-09-10 11:14:42', 0.72, 'F', 1)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Suricata Tony', '2013-04-23 11:15:42', 0.9, 'M', 1)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Panda rosu Riki', '2017-08-14', 4, 'F', 'Sfoara', 2)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Panda rosu Thomas', '2020-02-02 13:24:42', 3.1, 'M', 2)



