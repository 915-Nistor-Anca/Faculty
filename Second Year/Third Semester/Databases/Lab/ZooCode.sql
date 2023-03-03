--create database Zoo
--go

use Zoo
go


create table Family(
	fid int primary key IDENTITY,
	familydescr varchar(50)
)

create table Area(
	areaid int primary key IDENTITY,
	areaname varchar(50) NOT NULL,
	arealocation varchar(10) NOT NULL,
	areadescr varchar(50)
)

create table Specie(
	specieid int primary key IDENTITY,
	speciename varchar(50) NOT NULL,
	speciespecifications varchar(50) NOT NULL,

	areaid int foreign key references Area(areaid)
)

create table Animal(
	animalid int primary key IDENTITY,
	animalname varchar(50) NOT NULL,
	animaldateofbirth datetime NOT NULL,
	animalweight float NOT NULL,
	gender varchar(10) NOT NULL,
	favouritetoy varchar(50),

	fid int foreign key references Family(fid),
	specieid int foreign key references Specie(specieid)


)

create table ShopType(
	shoptypeid int primary key IDENTITY,
	shoptypename varchar(50) NOT NULL
)

create table Shop(
	shopid int primary key IDENTITY,
	shopname varchar(50) NOT NULL,
	shopdescr varchar(50),

	areaid int foreign key references Area(areaid),
	shoptypeid int foreign key references ShopType(shoptypeid)
)

create table Attraction(
	attractionid int primary key IDENTITY,
	attractiondescr varchar(50) NOT NULL,
	ticketprice int NOT NULL,
	minimumage int,

	areaid int foreign key references Area(areaid)
)

create table Job(
	jobid int primary key IDENTITY,
	jobname varchar(50) NOT NULL,
	jobdescription varchar(50) NOT NULL
)

create table Employee(
	cnp varchar(20) primary key,
	firstname varchar(30) NOT NULL,
	lastname varchar(30) NOT NULL,
	adress varchar(50) NOT NULL,
	employeedateofbirth datetime NOT NULL,
	dateofemployment datetime NOT NULL,
	phonenumber varchar(15) NOT NULL,
	salary int NOT NULL,
	email varchar(50),
	highestformofeducation varchar(50),

	jobid int foreign key references Job(jobid)
)

create table Assignment(
	startingdate datetime NOT NULL,
	endingdate datetime NOT NULL,

	areaid int foreign key references Area(areaid),
	cnp varchar(20) foreign key references Employee(cnp)
	constraint PK_Assignment primary key (areaid, cnp)
)

--insert into tablename(col1,col2) values(1,1...)

--update tablename set salary = ... salary*1.05
	--where name = 'Popescu' and ...

--delete from table ...
	--where

--select d.name, sum(e.salary) as Costs, count(e.id) as ECount
--from Dep as d
--left outo join Em e on e.id = d.id
--group by d.id

                  --iner       left             right                 full
--E D               1,1        1,1              1,1                   1,1
--1 1               2,2		   2,2              2,2                   2,2
--2 2               3,3        3,3			    3,3                   3,3
--3 3                          4, null          null,5                4,null
--4 5                                                                 null,5 


INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')
INSERT INTO Family (familydescr) VALUES ('')

SELECT f.fid, f.familydescr 
FROM Family f

DELETE
FROM Family 
WHERE fid = 2

INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Tundra Alpina', 'S-V', 'Nu exista arbori, este prea rece.')

SELECT *
FROM Area

INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Padurea Boreala', 'N', '16% din supr. Terrei. Cald si umed, soluri sarace.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Desert', 'S-E', 'Foarte putine precipitatii.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Savana', 'S-V', 'Calda cu secete, soluri putin fertile.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Padurea Tropicala', 'N-E', 'Clima tropicala umeda, vegetatie deasa.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Tundra', 'N-V', 'Trai foarte dificil, -40/-50 grade Celsius.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Scrubul', 'S', 'Predominanta cu tufisuri.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Padurea Temperata', 'N-E', 'Exista copaci cu frunze late.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Zona Umeda', 'S-E', 'Suprafata acoperita de ape putin adanci.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Zona Yummy', 'C', 'Zona cu mancare si bauturi.')
INSERT INTO Area (areaname, arealocation, areadescr) VALUES('Zona Shopping', 'C', 'Zona in care se pot cumpara cadouri/suveniruri.')

INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Pinguin Imperial', 'Cea mai mare+rezistenta pasare marina.', 6)

SELECT *
FROM Specie

INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Suricata', 'Mamifer care traieste in colonii.', 7)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Panda rosu', 'Sta cam tot timpul in copaci. 66 cm lungime.', 8)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Urs panda', 'Mananca bambus.', 8)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Paun', 'Coada masc. e extravaganta pt a atrage femelele.', 8)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Leopard de zapada', 'Are corp slab, coada lunga.', 1)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Capra Alpina', 'Are coarne si produce mult lapte.', 1)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Ghepard', 'Este foarte rapid.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Gazela', 'Este un animal rumegator si ierbivor.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Leu', 'Unul dintre cei mai mari rapitori terestri.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Castor', 'Este un rozator semi-acvatic.', 9)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Flamingo', 'Are picioare lungi si poate zbura.', 9)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Gorila de munte', 'Imparte 99% din ADN cu oamenii.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Jaguar', 'Poate ajunge la v=80km/h. E felina.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Leopard negru', 'Este extrem de rar.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Cimpanzeu', 'Consuma frunze, fructe, miere, insecte.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Tigru Bengalez', 'Abdomen alb, coada portocalie cu dungi negre.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Lemur', 'Mic, ochi mari, coada lunga.', 5)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Urs polar', 'Cel mai mare animal de prada intalnit pe uscat.', 6)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Bou moscat', 'Are blana groasa si miros puternic.', 6)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Cangur rosu', 'Mamele isi tin puii in marsupiu.', 7)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Elefant asiatic', 'Animal erbivor de talie mare. Trompa lunga.', 7)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Urs Grizzly', 'Consuma iarba, fructe de padure, radacini etc.', 12)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Dromader', 'Are o cocoasa si picioare lungi.', 3)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Broasca testoasa africana', 'Poate trai sute de ani.', 3)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Girafa', 'E cel mai inalt animal.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Elefant african', 'E erbivor si prefera sa ramana langa apa.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Rinocer negru', 'A fost salvat de la disparitie acum cativa ani.', 4)
INSERT INTO Specie(speciename, speciespecifications, areaid) VALUES ('Crocodil', 'Acoperit de placi osoase.', 9)

INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Tiroliana', 25, 12, 5)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Patinaj printre pinguini', 15,5,6)

SELECT *
FROM Attraction

INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Carusel', 23, 14, 7)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Plimbare cu masina', 35, 5, 8)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Escaladat', 10, 16, 1)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Tobogane cu apa', 19, 5, 9)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Concurs culinar', 15, 18, 10)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Vanatoare de comori prin sapaturi', 20, 5, 2)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Plimbare cu camila', 15, 5, 3)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Roller coaster', 35, 18, 4)
INSERT INTO Attraction(attractiondescr, ticketprice, minimumage, areaid) VALUES ('Amfiteatru pt copii', 15, 0, 11)


SELECT s.areaid, a.areaname, speciename
FROM Specie s, Area a
WHERE s.areaid = a.areaid
ORDER BY s.areaid


INSERT INTO ShopType(shoptypename) VALUES ('Mancare')
INSERT INTO ShopType(shoptypename) VALUES ('Suvenir')
INSERT INTO ShopType(shoptypename) VALUES ('Bautura')

SELECT *
FROM ShopType

INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Apa', 'Plata sau minerala.', 10, 3)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Rucsacuri', '-', 11, 2)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand cu Burgeri', 'Burger cu pui/vita.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Hot Dogi', 'Crenvurst in chifla cu maioneza/ketchup.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Sushi', 'Diferite tipuri + sos la alegere.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Salate', 'Combinatie de 5 ingrediente la alegere.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Cheesecake', 'Cu fructe, Oreo, Nutella etc.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Cafea', 'Cappuccino, espresso, latte macchiato etc.', 10, 3)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Sucuri', 'Suc de mere/portocale/pere.', 10, 3)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Popcorn', 'Cu unt/sare/cascaval.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Covrigi', 'Cu sare/susan/mac.', 10, 1)
INSERT INTO Shop(shopname, shopdescr, areaid, shoptypeid) VALUES ('Stand de Brelocuri', 'Cu diferite capete de animal.', 11, 2)

SELECT *
FROM Shop

SELECT *
FROM Animal

INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, fid, specieid) VALUES ('Pinguinul Tarra', '2019-02-04 13:14:30', 10, 'F', 'Minge', 1, 1)

DELETE
FROM Animal
WHERE fid = 1

INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, fid, specieid) VALUES ('Pinguinul Terry', '2018-03-04 12:15:20', 13, 'M', 'Cuburi de gheata', 1, 1)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Suricata Suzzy', '2010-09-10 11:14:42', 0.72, 'F', 2)

INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Suricata Tony', '2013-04-23 11:15:42', 0.9, 'M', 2)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Panda rosu Riki', '2017-08-14', 4, 'F', 'Sfoara', 3)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Panda rosu Thomas', '2020-02-02 13:24:42', 3.1, 'M', 3)

SELECT *
FROM Specie

INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Ursul panda Mimi', '2014-08-16 23:43:31', 86, 'F', 4)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Paunul Napoli', '2019-08-28 12:13:25', 5.2, 'M', 2, 5)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Paunul Jerry', '2016-05-07 12:14:14', 7, 'M', 2, 5)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Capra Alpina Mira', '2017-06-04 13:15:53', 60, 'F', 7)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Tap Alpin Jon', '2012-03-16 13:15:53', 58.3, 'M', 'Suport pentru lovituri', 7)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Gorila de munte Troy', '2012-10-15 13:24:24', 102, 'M', 7, 13)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Gorila de munte Cleo', '2014-05-04 12:24:35', 96, 'F', 7, 13)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Tigrul Bengalez George', '2016-06-04 12:21:24', 220, 'M', 'Suport de ascutit unghiile', 17)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Tigrul Bengalez Rita', '2017-07-23 10:22:21', 140, 'F', 'Os', 17)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, fid, specieid) VALUES ('Leul Simba', '2005-07-12 13:22:21', 190, 'M', 'Bucata mare de lemn', 3, 10)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Leoaica Nala', '2006-08-15 15:12:30', 130, 'F', 3, 10)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Ursul polar Fram', '1996-11-14 17:28:41', 463, 'M', 19)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Dromaderul Lisa', '2006-12-04 17:52:11', 310, 'F', 24)


INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Gazela Fifi', '2015-01-16 14:55:24', 23, 'M', 4, 9)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Gazela Kiki', '2011-01-16 14:55:24', 23, 'M', 4, 9)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Leopardul negru Zoe', '2003-02-12 16:25:15', 45, 'F', 15)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Leopardul negru Star', '2002-05-06 11:41:42', 70, 'M', 15)


INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, fid, specieid) VALUES ('Cimpanzeul Roco', '1995-06-17 14:24:44', 43, 'M', 'Acuarele pentru pictura', 8, 16) 
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Cimpanzeul Figa', '1998-05-16 12:26:10', 42, 'F', 8, 16) 
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Lemurul Muriel', '2015-05-12 23:25:15', 2.3, 'M', 9, 18)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Lemurul Tina', '2016-02-20 21:21:48', 2.1, 'F', 9, 18)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Boul moscat Fred','2014-11-07 13:15:16', 218, 'M', 20)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Boul moscat Alred','2014-05-15 11:23:14', 312, 'M', 20)


INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) VALUES ('Broasca testoasa africana Xenia', '1980-05-18 23:15:21', 44, 'F', 'Lumina pentru incalzire', 25)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Broasca testoasa africana Max', '1976-11-04 13:15:16', 45, 'M', 25)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Girafa Gilbert', '2005-05-05 14:16:25', 865, 'M', 11, 26)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, fid, specieid) VALUES ('Girafa Vera', '2004-07-12 17:12:21', 870, 'F', 11, 26)
INSERT INTO Animal(animalname, animaldateofbirth, animalweight, gender, specieid) VALUES ('Crocodilul Rex', '2008-02-05 18:15:49', 964, 'M', 29)


SELECT *
FROM Animal
-- query: ce animale se pot inmulti (sa fie din aceeasi specie, sa fie din familii diferite si sa fie mascul/femela)

INSERT INTO Job(jobname,jobdescription) VALUES ('Ingrijitor zoo', 'Are grija de animale, le da sa manance etc.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Intretinere zoo', 'Se ocupa cu ingrijirea potecilor si curatarea lor.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Educator', 'Prezent la diferite specii pentru a da informatii.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Entertainer', 'Distreaza copiii.')
INSERT INTO Job(jobname,jobdescription) VALUES ('Vanzator', 'Lucreaza la un magazin.')

SELECT *
FROM Job

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, email, jobid)
VALUES ('1900217628745', 'Vasile', 'Oltu', 'str. Galaxiei, nr. 15, bloc D4, ap. 34', '1990-02-17 12:14:25', '2007-01-19 23:12:14', '0736587562', 2000, 'oltu.vs@gmail.com', 2)

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, email, jobid)
VALUES ('1800204683496', 'Flaviu', 'Miclaus', 'str. Bradului, nr. 17B', '1980-03-07 12:14:25', '2019-03-07 23:12:14', '0722625735', 3100, 'miclaus.flaviu@yahoo.com', 6)

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, email, jobid)
VALUES ('1950918591587', 'Cornel', 'Vascan', 'str. Slatina, nr. 3, bloc E2, ap. 25', '1995-09-07 12:14:25', '2016-07-18 23:12:14', '0741648369', 2900, 'cornel.vascan@gmail.com', 6)

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, email, jobid, highestformofeducation)
VALUES ('1981128863974', 'Alex', 'Munteanu', 'str. Vidraru, nr. 7, bloc A2, ap. 69', '1998-11-28 12:14:25', '2020-09-19 23:12:14', '0736056278', 3100, 'alex.munteanu@gmail.com', 1, 'USAMV, CLUJ')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid)
VALUES ('1920117748934', 'Daniel', 'Lascu', 'str. Vultureni, nr. 30', '1992-01-17 12:14:25', '2018-05-19 23:12:14', '0728573924', 2650, 6)


INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('1830719583957', 'Cristian', 'Duma', 'str. Zanelor, nr. 50C', '1983-03-19 12:14:25', '2009-07-21 23:12:14', '0725773829', 2300, 5, 'cristian.duma@gmail.com')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid)
VALUES ('2750904275628', 'Dana', 'Topa', 'str. Parang, nr. 9', '1975-09-04 12:14:25', '2009-12-22 23:12:14', '07225628564', 2000, 5)

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('1010815384756', 'Radu', 'Voicu', 'str. Paris, nr. 9', '2001-08-15 12:14:25', '2020-01-25 23:12:14', '0737582476', 2400, 4, 'radu.voicu@yahoo.com')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('2830713483657', 'Cristina', 'Rab', 'str. Peana, nr. 23, bloc B4, ap. 106', '1983-07-13 12:14:25', '2014-11-05 23:12:14', '0746285628', 3210, 6, 'cristina.rab@yahoo.com')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('2850415165376', 'Sabrina', 'Morar', 'str. 1 Mai, nr. 10', '1985-05-15 12:14:25', '2013-09-04 23:12:14', '0738693758', 2100, 5, 'morar.sabrina@yahoo.com')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, highestformofeducation)
VALUES ('2730917568758', 'Claudia', 'Baraboi', 'str. Nordului, nr. 3', '1973-09-17 12:14:25', '2002-11-05 23:12:14', '0748564895', 3500, 1, 'USAMV, Timisoara')


INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('1700612784535', 'Cristian', 'Dumitru', 'str. Orzului, nr. 5', '1970-06-12 12:14:25', '2005-05-03 23:12:14', '0745384657', 3980, 2, 'cristian.dumitru@yahoo.com')

SELECT *
FROM Employee

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('2810816587368', 'Elena', 'Maxim', 'str. Artarului, nr. 18', '1981-08-16 12:14:25', '2018-07-15 23:12:14', '0735493652', 3200, 2, 'elena.m@gmail.com')

INSERT INTO
Employee(cnp, firstname, lastname, adress, employeedateofbirth, dateofemployment, phonenumber, salary, jobid, email)
VALUES ('1770602679458', 'Petre', 'Radoi', 'str. Porumbeilor, nr. 60', '1977-06-02 12:14:25', '2020-11-19 23:12:14', '0738564728', 4000, 5, 'petre.rad@yahoo.com')


Select *
From Assignment

DELETE
FROM Assignment

INSERT INTO Assignment (startingdate, endingdate, areaid, cnp) VALUES ('2021-06-02 22:23:15', '2021-09-07 12:14:15', 10, '1770602679458')
INSERT INTO Assignment (startingdate, endingdate, areaid, cnp) VALUES ('2022-04-19 22:23:15', '2022-12-17 12:14:15', 3, '2730917568758')
INSERT INTO Assignment (startingdate, endingdate, areaid, cnp) VALUES ('2022-04-19 22:23:15', '2022-10-17 12:14:15', 7, '1010815384756')
INSERT INTO Assignment (startingdate, endingdate, areaid, cnp) VALUES ('2022-12-19 22:23:15', '2022-12-23 12:14:15', 5, '1010815384756')



--TEMA

-- referential integrity constraints violation
INSERT INTO Assignment (startingdate, endingdate, areaid, cnp) VALUES ('2021-06-02 22:23:15', '2021-09-07 12:14:15', 100, '1770602679458')

--UPDATE/DELETE STATEMENTS

UPDATE Employee
SET salary = salary + 100
WHERE salary < 2500

UPDATE Area
SET areadescr = 'Trai dificil, temperaturi scazute'
WHERE areaname = 'Tundra'

UPDATE Animal
SET favouritetoy = 'Ball'
Where specieid = 14 and favouritetoy IS NULL

UPDATE Attraction
SET minimumage = 7
WHERE minimumage BETWEEN 0 and 5

DELETE
FROM Assignment
WHERE endingdate <= GETDATE()


DELETE
FROM Animal
WHERE fid = 1 or fid = 2

DELETE
FROM Animal 
WHERE animalid IN
(SELECT animalid
FROM Animal
WHERE DATEDIFF(year, animaldateofbirth, GETDATE()) > 100)


--a) UNION OPERATION
--masculii mai mari de 8 ani sau femelele mai mari de 10 ani
SELECT a.animalid, a.animalname, a.gender, a.animaldateofbirth
FROM Animal a
WHERE a.gender = 'M' and DATEDIFF(year, a.animaldateofbirth, GETDATE()) > 8
UNION
SELECT a.animalid, a.animalname, a.gender, a.animaldateofbirth
FROM Animal a
WHERE a.gender = 'F' and DATEDIFF(year, a.animaldateofbirth, GETDATE()) > 10


--atrbuirile neincepute sau nefinalizate
SELECT e.cnp, e.firstname, e.lastname, a.areaid, a.startingdate, a.endingdate
FROM Employee e, Assignment a
WHERE e.cnp = a.cnp and (GETDATE() < a.startingdate OR a.endingdate > GETDATE())

--b) INTERSECTION OPERATION
--animalele cu cea mai mare greutate din fiecare specie
SELECT s.specieid, a.animalid, a.animalname, a.animalweight
FROM Animal a, Specie s
WHERE s.specieid = a.specieid
and a.animalweight 
IN
(SELECT max(animalweight)
FROM Animal
GROUP BY specieid)
ORDER BY a.animalweight

--animalele care nu au jucarie si sunt pui
SELECT *, DATEDIFF(year, animaldateofbirth, GETDATE()) as 'Years'
FROM Animal
WHERE favouritetoy is NULL
INTERSECT
SELECT *, DATEDIFF(year, animaldateofbirth, GETDATE()) as 'Years'
FROM Animal
WHERE DATEDIFF(year, animaldateofbirth, GETDATE()) <= 5

--c) DIFFERENCE OPERATION
--animalele care au familie
SELECT *
FROM Animal
EXCEPT
SELECT *
FROM Animal a
WHERE a.fid is NULL

--magazinele fara cele de suveniruri(id 2)
SELECT s.shopname, s.shopdescr, s.areaid, st.shoptypeid as 'TYPE ID', st.shoptypename as 'TYPE NAME'
FROM Shop s, ShopType st
WHERE s.shoptypeid = st.shoptypeid 
and shopid NOT IN 
(SELECT shopid
FROM SHOP 
WHERE shoptypeid = 2)
GROUP BY st.shoptypeid, s.shopname, s.shopdescr, s.areaid, st.shoptypename


--d) 
--toate atribuirile cu angajatii care le indeplinesc
SELECT *
FROM Employee e INNER JOIN Assignment a ON e.cnp = a.cnp

--cat sunt salariile angajatilor adunate pt fiecare meserie
SELECT TOP 50 PERCENT j.jobname, sum(e.salary) as 'Total cost', count(e.cnp) as 'Number of employees'
FROM Job j
LEFT JOIN Employee e on e.jobid = j.jobid
GROUP BY j.jobid, j.jobname
ORDER BY sum(e.salary) DESC


--afiseaza toate speciile cu animalele pe care le contin
SELECT f.fid, a.animalname, s.speciename, s.speciespecifications
FROM Family f
RIGHT JOIN Animal a
ON f.fid = a.fid 
RIGHT JOIN Specie s
ON s.specieid = a.specieid 
RIGHT JOIN Area ar
ON ar.areaid = s.areaid
GROUP BY f.fid, a.animalname, s.speciename, s.speciespecifications


--toate atribuirile + toti angajatii fara atribuiri
SELECT a.cnp, a.startingdate, a.endingdate,e.firstname, e.lastname
FROM Employee e
FULL JOIN Assignment a
ON a.cnp = e.cnp


--e)
--angajatii care nu au nicio atribuire in partea de nord a gradinii zoologice
SELECT e.firstname
FROM Employee e
WHERE e.cnp NOT IN
(SELECT a.cnp
FROM Assignment a
WHERE a.areaid IN
(SELECT ar.areaid
FROM Area ar
WHERE ar.arealocation = 'N'))


--angajatul cu cel mai mare salar
SELECT e.cnp, e.firstname, e.lastname, e.salary, e.jobid, j.jobname
FROM Employee e, Job j
WHERE e.jobid = j.jobid and salary =
(SELECT max(salary)
FROM Employee)


select * from Area

--f)
--angajatii care au lucrat in zona cu magazine a gradinii (id = 10)
SELECT e.firstname, e.lastname, e.jobid, j.jobname
FROM Employee e, Job j
WHERE EXISTS
(SELECT *
FROM Assignment a
WHERE a.cnp = e.cnp AND a.areaid = 10)
AND e.jobid = j.jobid


--femelele care fac parte dintr-o familie
SELECT a.animalid, a.animalname, a.specieid, a.fid
FROM Animal a
WHERE EXISTS
(SELECT *
FROM Family f
WHERE a.fid = f.fid)
AND a.gender = 'F'

--g) SUBQUERY IN FROM CLAUSE
--angajatii care au salariul mai mare sau egal decat media salariilor 
SELECT e.cnp, e.firstname, e.lastname, e.salary, avgsalary
FROM (SELECT AVG(salary) as avgsalary FROM Employee) as salary, Employee as e
WHERE e.salary >= salary.avgsalary

--atractiile care au pretul mai mic decat media preturilor
SELECT a.attractionid, a.attractiondescr, a.areaid, a.ticketprice,  tp as 'Average ticketprice'
FROM Attraction a, (SELECT AVG(ticketprice) as tp FROM Attraction) as p
WHERE a.ticketprice < p.tp

--h)
--numarul de animale pt fiecare specie
SELECT DISTINCT s.speciename, COUNT(a.animalid) as 'Number of animals'
FROM Specie s, Animal a
WHERE s.specieid = a.specieid
GROUP BY s.speciename
HAVING COUNT(a.animalid) > 1

-- toate animalele grupate pe specie
SELECT DISTINCT a.animalname, a.specieid
FROM Animal a
GROUP BY a.specieid, a.animalname


--varsta medie pt angajatii care au salariul minim de 2500 pentru fiecare meserie care are macar 2 angajati
SELECT e.jobid, AVG(DATEDIFF(year, e.employeedateofbirth, GETDATE())) AS "Average age"
FROM Employee e
WHERE e.salary >= 2500
GROUP BY e.jobid
HAVING 2 <=
(SELECT COUNT(*)
FROM Employee e2
WHERE e2.jobid = e.jobid)

--nr maxim de kg pentru animalele care au varsta minima de 5 ani pentru fiecare specie care are macar 1 animal
SELECT a.specieid, MAX(a.animalweight)
FROM Animal a
WHERE DATEDIFF(year, a.animaldateofbirth, GETDATE()) >= 5
GROUP BY a.specieid
HAVING 1 <= 
(SELECT COUNT(*)
FROM Animal a2
WHERE a.specieid = a2.specieid)
ORDER BY MAX(a.animalweight)

--i)
--angajatii care sunt educatori

SELECT *
FROM Employee e
WHERE e.jobid = ANY
(SELECT j.jobid
FROM Job j
WHERE j.jobname LIKE 'Educator')

SELECT *
FROM Employee e
WHERE e.jobid IN
(SELECT j.jobid
FROM Job j
WHERE j.jobname LIKE 'Educator')

--angajatul cu salariul maxim pt fiecare meserie

SELECT e.jobid, e.firstname, e.lastname, e.salary
FROM Employee e
WHERE e.salary = ALL
(SELECT MAX(e2.salary)
FROM Employee e2
WHERE e.jobid = e2.jobid)


SELECT e.jobid, e.firstname, e.lastname, e.salary
FROM Employee e
WHERE e.salary IN
(SELECT MAX(e2.salary)
FROM Employee e2
WHERE e.jobid = e2.jobid)


--numele si data nasterii celui mai mic animal

SELECT a.animalname, a.animaldateofbirth
FROM Animal a
WHERE DATEDIFF(year, a.animaldateofbirth, GETDATE()) < ANY
(SELECT DATEDIFF(year, a2.animaldateofbirth, GETDATE())
FROM Animal a2)

SELECT a.animalname, a.animaldateofbirth
FROM Animal a
WHERE DATEDIFF(year, a.animaldateofbirth, GETDATE()) <
(SELECT MIN(DATEDIFF(year, a2.animaldateofbirth, GETDATE()))
FROM Animal a2)

--angajatii care au vechime mai mare decat toti angajatii numiti Radu
SELECT *
FROM Employee e
WHERE DATEDIFF(year, e.dateofemployment, GETDATE()) > ALL (SELECT DATEDIFF(year, e2.dateofemployment, GETDATE())
FROM Employee e2
WHERE e2.firstname = 'Radu')


SELECT *
FROM Employee e
WHERE DATEDIFF(year, e.dateofemployment, GETDATE()) = (SELECT MAX(DATEDIFF(year, e2.dateofemployment, GETDATE()))
FROM Employee e2
WHERE e2.firstname = 'Radu')
----

--primele 10 animale cu cea mai mare greutate
SELECT TOP 10 * 
FROM Animal a
ORDER BY a.animalweight DESC




--lab 3

--modify a column

GO
CREATE OR ALTER PROCEDURE setTicketPriceAttractionDecimal
AS ALTER TABLE Attraction ALTER COLUMN ticketprice DECIMAL(4, 2)

GO
CREATE OR ALTER PROCEDURE setTicketPriceAttractionInt
AS ALTER TABLE Attraction ALTER COLUMN ticketprice INT

--add/remove a column

GO
CREATE OR ALTER PROCEDURE addContainsVeganProductsShopType
AS ALTER TABLE ShopType ADD containsVeganProducts VARCHAR(10)

GO
CREATE OR ALTER PROCEDURE removeContainsVeganProductsShopType
AS ALTER TABLE ShopType DROP COLUMN containsVeganProducts


--add/remove default constraint

GO
CREATE OR ALTER PROCEDURE addDefaultToAttractionTicketPrice
AS ALTER TABLE Attraction ADD CONSTRAINT default_price DEFAULT(0) FOR ticketprice

GO
CREATE OR ALTER PROCEDURE removeDefaultToAttractionTicketPrice
AS ALTER TABLE Attraction DROP CONSTRAINT default_price

--create/drop a table

GO
CREATE OR ALTER PROCEDURE addShow
AS CREATE TABLE Show(
			show_id int,
			show_name varchar(100) NOT NULL,
			show_ticketprice int,
			area_id int NOT NULL,
			CONSTRAINT SHOW_PRIMARY_KEY PRIMARY KEY(show_id)
			)

GO
CREATE OR ALTER PROCEDURE dropShow
AS DROP TABLE Show

--add/remove a primary key

GO
CREATE OR ALTER PROCEDURE addPrimaryKeyShow
AS
	ALTER TABLE Show
		DROP CONSTRAINT SHOW_PRIMARY_KEY
	ALTER TABLE Show
		ADD CONSTRAINT SHOW_PRIMARY_KEY PRIMARY KEY(show_id, show_name)

GO 
CREATE OR ALTER PROCEDURE removeAndAddOldPrimaryKeyShow
AS
	ALTER TABLE Show
		DROP CONSTRAINT SHOW_PRIMARY_KEY
	ALTER TABLE Show
		ADD CONSTRAINT SOW_PRIMARY_KEY PRIMARY KEY(show_id)


--add/remove candidate key

GO
CREATE OR ALTER PROCEDURE newCandidateArea
AS
	ALTER TABLE Area
	ADD CONSTRAINT AREA_CANDIDATE_KEY UNIQUE(areaname, arealocation)

GO
CREATE OR ALTER PROCEDURE removeCandidateArea
AS
	ALTER TABLE Area
	DROP CONSTRAINT AREA_CANDIDATE_KEY

--add/remove a foreign key
GO
CREATE OR ALTER PROCEDURE newForeignKeyShow
AS
	ALTER TABLE Show
	ADD CONSTRAINT SHOW_FOREIGN_KEY FOREIGN KEY(area_id) REFERENCES Area(areaid)

GO
CREATE OR ALTER PROCEDURE removeForeignKeyShow
AS
	ALTER TABLE Show
	DROP CONSTRAINT SHOW_FOREIGN_KEY
GO
--a new table that holds the current version of the database schema

CREATE TABLE versionTable (
	vrs INT
)

INSERT INTO versionTable 
VALUES (1) --initial version

CREATE TABLE procedureTable (
	initial_version INT,
	final_version INT,
	procedure_name VARCHAR(100),
	PRIMARY KEY (initial_version, final_version)
)

INSERT INTO procedureTable
VALUES
	(1, 2, 'setTicketPriceAttractionDecimal'),
	(2, 1, 'setTicketPriceAttractionInt'),
	(2, 3, 'addContainsVeganProductsShopType'), 
	(3, 2, 'removeContainsVeganProductsShopType'),
	(3, 4, 'addDefaultToAttractionTicketPrice'),
	(4, 3, 'removeDefaultToAttractionTicketPrice'),
	(4, 5, 'addShow'),
	(5, 4, 'dropShow'),
	(5, 6, 'addPrimaryKeyShow'),
	(6, 5, 'removeAndAddOldPrimaryKeyShow'),
	(6, 7, 'newCandidateArea'),
	(7, 6, 'removeCandidateArea'),
	(7, 8, 'newForeignKeyShow'),
	(8, 7, 'removeForeignKeyShow')

SELECT *
FROM procedureTable

GO
CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT)
AS
	DECLARE @current_version INT
	DECLARE @procedureName VARCHAR(100)
	SELECT @current_version = vrs FROM versionTable

	IF (@newVersion > (SELECT MAX(final_version) FROM procedureTable) OR @newVersion < 1)
		RAISERROR ('This version is invalid.', 10, 1)
	ELSE
	BEGIN
		IF @newVersion = @current_version
			PRINT('The current version is the one you want.');
		ELSE
		BEGIN
			IF @current_version > @newVersion
			BEGIN
				WHILE @current_version > @newVersion 
					BEGIN
						SELECT @procedureName = procedure_name FROM procedureTable WHERE initial_version = @current_version AND final_version = @current_version-1
						EXEC (@procedureName)
						SET @current_version = @current_version - 1
					END
			END

			IF @current_version < @newVersion
			BEGIN
				WHILE @current_version < @newVersion 
					BEGIN
						SELECT @procedureName = procedure_name FROM procedureTable WHERE initial_version = @current_version AND final_version = @current_version+1
						EXEC (@procedureName)
						SET @current_version = @current_version + 1
					END
			END

			UPDATE versionTable SET vrs = @newVersion
		END
	END

EXEC goToVersion 1
UPDATE versionTable 
SET vrs = 7



-- lab 4
-- SCRIPT

if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRuns]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRuns]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tests]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tests]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Views]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Views]

GO



CREATE TABLE [Tables] (

	[TableID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunTables] (

	[TestRunID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunViews] (

	[TestRunID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRuns] (

	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,

	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,

	[StartAt] [datetime] NULL ,

	[EndAt] [datetime] NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestTables] (

	[TestID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[NoOfRows] [int] NOT NULL ,

	[Position] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestViews] (

	[TestID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Tests] (

	[TestID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Views] (

	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



ALTER TABLE [Tables] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tables] PRIMARY KEY  CLUSTERED 

	(

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunTables] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunViews] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRuns] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRuns] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestTables] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestViews] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Tests] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tests] PRIMARY KEY  CLUSTERED 

	(

		[TestID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Views] WITH NOCHECK ADD 

	CONSTRAINT [PK_Views] PRIMARY KEY  CLUSTERED 

	(

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] ADD 

	CONSTRAINT [FK_TestRunTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunTables_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestRunViews] ADD 

	CONSTRAINT [FK_TestRunViews_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestTables] ADD 

	CONSTRAINT [FK_TestTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestTables_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestViews] ADD 

	CONSTRAINT [FK_TestViews_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	),

	CONSTRAINT [FK_TestViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	)

GO


GO
CREATE OR ALTER PROCEDURE addToTables (@tableName VARCHAR(50)) AS
BEGIN
	IF @tableName IN (SELECT [Name] from [Tables]) 
	BEGIN
		PRINT 'Table already present in Tables'
		RETURN
	END

	IF @tableName NOT IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES)
	BEGIN
		PRINT 'Table not present in the database'
		RETURN
	END

	INSERT INTO [Tables] ([Name]) 
	VALUES
		(@tableName)
END

GO
CREATE OR ALTER PROCEDURE addToViews (@viewName VARCHAR(50)) AS
BEGIN
	IF @viewName IN (SELECT [Name] from [Views]) 
	BEGIN
		PRINT 'View already present in Views'
		RETURN
	END

	IF @viewName NOT IN (SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS)
	BEGIN
		PRINT 'View not present in the database'
		RETURN
	END

	INSERT INTO [Views] ([Name]) 
	VALUES
		(@viewName)
END

GO
CREATE OR ALTER PROCEDURE addToTests (@testName VARCHAR(50)) AS
BEGIN
	IF @testName IN (SELECT [Name] from [Tests]) 
	BEGIN
		PRINT 'Test already present in Tests'
		RETURN
	END

	INSERT INTO [Tests] ([Name]) 
	VALUES
		(@testName)
END


GO
CREATE OR ALTER PROCEDURE connectTableToTest (@tableName VARCHAR(50), @testName VARCHAR(50), @rows INT, @pos INT) AS
BEGIN
	IF @tableName NOT IN (SELECT [Name] FROM [Tables]) 
		BEGIN
			PRINT 'Table not present in Tables'
			RETURN
		END

	IF @testName NOT IN (SELECT [Name] FROM [Tests])
		BEGIN
			PRINT 'Test not present in Test'
			RETURN
		END

	IF EXISTS( 
		SELECT * 
		FROM TestTables T1 JOIN Tests T2 ON T1.TestID = T2.TestID
		WHERE T2.[Name] = @testName AND Position = @pos
	)
		BEGIN
			PRINT 'Position provided conflicts with previous positions'
			RETURN
		END

	INSERT INTO [TestTables] (TestID, TableID, NoOfRows, Position) 
	VALUES (
		(SELECT [Tests].TestID FROM [Tests] WHERE [Name] = @testName),
		(SELECT [Tables].TableID FROM [Tables] WHERE [Name] = @tableName),
		@rows,
		@pos
	)
END

GO
CREATE OR ALTER PROCEDURE connectViewToTest (@viewName VARCHAR(50), @testName VARCHAR(50)) AS
BEGIN
	IF @viewName NOT IN (SELECT [Name] FROM [Views]) 
		BEGIN
			PRINT 'View not present in Views'
			RETURN
		END

	IF @testName NOT IN (SELECT [Name] FROM [Tests]) 
		BEGIN
			PRINT 'Test not present in Tests'
			RETURN
		END

	INSERT INTO [TestViews] (TestID, ViewID)
	VALUES(
		(SELECT [Tests].TestID FROM [Tests] WHERE [Name] = @testName),
		(SELECT [Views].ViewID FROM [Views] WHERE [Name] = @viewName)
	)
END



GO
CREATE OR ALTER PROCEDURE runTest (@testName varchar(50)) AS
BEGIN
    IF @testName NOT IN (SELECT Name FROM Tests)
	BEGIN
        PRINT 'Test not in Tests'
        RETURN
    END
    DECLARE @command varchar(100)
    DECLARE @testStartTime datetime2
    DECLARE @startTime datetime2
    DECLARE @endTime datetime2
    DECLARE @table varchar(50)
    DECLARE @rows int
    DECLARE @pos int
    DECLARE @view varchar(50)
    DECLARE @testId int


    SELECT @testId=TestID FROM Tests WHERE Name=@testName
    DECLARE @testRunId int
    SET @testRunId = (SELECT max(TestRunID)+1 FROM TestRuns)
    IF @testRunId IS NULL
        SET @testRunId = 0


    DECLARE tableCursor cursor scroll for --creez cursor pt fiecare tabel care trebuie rulat
        SELECT T1.Name, T2.NoOfRows, T2.Position
        FROM Tables T1 join TestTables T2 on T1.TableID = T2.TableID
        WHERE T2.TestID = @testId --aleg tabelele care sunt in testul rulat
        ORDER BY T2.Position
    DECLARE viewCursor cursor for --cursor pt view
        SELECT V.Name
        FROM Views V join TestViews TV on V.ViewID = TV.ViewID
        WHERE TV.TestID = @testId

    SET @testStartTime = sysdatetime()


    OPEN tableCursor
    fetch last from tableCursor into @table, @rows, @pos --ia ultimul rand in cursor si il face randul curent
    WHILE @@FETCH_STATUS = 0 begin --daca fetch ul a reusit
        exec ('delete from '+ @table)
        fetch prior from tableCursor into @table, @rows, @pos --returneaza randul care urmeaza
    END
    CLOSE tableCursor

    open tableCursor
    SET IDENTITY_INSERT TestRuns ON --pot face modificari cand e on
    insert into TestRuns (TestRunID, Description, StartAt)values (@testRunId, 'Tests results for: ' + @testName, @testStartTime)
    SET IDENTITY_INSERT TestRuns OFF
    fetch tableCursor into @table, @rows, @pos
    WHILE @@FETCH_STATUS = 0 BEGIN --pt fiecare tabel care e in test
        SET @command = 'populateTable' + @table --se executa procedura care populeaza tabelul
        if @command not in (select ROUTINE_NAME from INFORMATION_SCHEMA.ROUTINES) begin
            print @command + 'does not exist'
            return
        end


        set @startTime = sysdatetime()
        exec @command @rows -- execut comanda
        set @endTime = sysdatetime()
        insert into TestRunTables (TestRunID, TableId, StartAt, EndAt) values (@testRunId, (select TableID from Tables where Name=@table), @startTime, @endTime)
        fetch tableCursor into @table, @rows, @pos
    END
    close tableCursor
    deallocate tableCursor

    open viewCursor
    fetch viewCursor into @view
    while @@FETCH_STATUS = 0 begin --pt fiecare view care apartine testului
        set @command = 'select * from ' + @view
        set @startTime = sysdatetime()
        exec (@command)
        set @endTime = sysdatetime()
        insert into TestRunViews (TestRunID, ViewID, StartAt, EndAt) values (@testRunId, (select ViewID from Views where Name=@view), @startTime, @endTime)
        fetch viewCursor into @view
    end
    close viewCursor
    deallocate viewCursor

    update TestRuns
    set EndAt=sysdatetime()
    where TestRunID = @testRunId
END

GO
CREATE OR ALTER VIEW getAreaLocalization AS
	SELECT arealocation, count(*) as number_of_areas
	FROM Area
	GROUP BY arealocation

exec addToViews 'getAreaLocalization'
exec addToTests 'test1'
exec addToTables 'Area'
exec connectTableToTest 'Area', 'test1', 1000, 1
exec connectViewToTest 'getAreaLocalization', 'test1'



GO
CREATE OR ALTER PROCEDURE populateTableArea(@rows int) as
	WHILE @rows > 0 begin
		insert into Area(areaname, areadescr, arealocation) values (floor(rand()*100), 'Testing', 'Name')
		set @rows = @rows - 1
	END

execute runTest 'test1'

select * from TestRuns

select *
from TestRunViews

select *
from TestRunTables

select *
from TestTables

GO
CREATE OR ALTER VIEW getAssignmentsAndEmployees AS
	SELECT e.cnp, e.firstname, e.lastname
	FROM Employee e INNER JOIN Assignment a ON e.cnp = a.cnp


SELECT * FROM Area










CREATE TABLE Manager (
	cnp INT PRIMARY KEY,
	salary INT UNIQUE,
	phone_number INT
)

CREATE TABLE ZooEvent (
	event_id INT PRIMARY KEY,
	event_cost INT
)

CREATE TABLE ManagerEventAssignment (
	assignment_id INT PRIMARY KEY,
	m_cnp INT FOREIGN KEY REFERENCES Manager(cnp),
	e_id INT FOREIGN KEY REFERENCES ZooEvent(event_id)
)

insert into Manager(cnp, salary, phone_number) values (1, 3000, 75292018)

insert into Manager(cnp, salary, phone_number) values (2, 3060, 57689549)
insert into Manager(cnp, salary, phone_number) values (3, 4785, 25648697)
insert into Manager(cnp, salary, phone_number) values (4, 3658, 76983345)
insert into Manager(cnp, salary, phone_number) values (5, 1356, 64524153)
insert into Manager(cnp, salary, phone_number) values (6, 3565, 24346780)

insert into ZooEvent(event_id, event_cost) values (1, 4224)
insert into ZooEvent(event_id, event_cost) values (2, 3791)
insert into ZooEvent(event_id, event_cost) values (3, 2720)
insert into ZooEvent(event_id, event_cost) values (4, 2371)
insert into ZooEvent(event_id, event_cost) values (5, 4681)

select * from Manager

insert into ManagerEventAssignment(assignment_id, m_cnp, e_id) values (1,1,1)
insert into ManagerEventAssignment(assignment_id, m_cnp, e_id) values (2,1,1)
insert into ManagerEventAssignment(assignment_id, m_cnp, e_id) values (3,1,2)


--a)

select * from Manager --clustered index scan

select * from Manager where cnp < 10000000 --clustered index seek

select salary from Manager order by salary --nonclustered index scan

select salary from Manager where salary between 3000 and 4000 --nonclustered index seek

select phone_number from Manager where salary = 3000 --key lookup

--b)
select * from ZooEvent where event_cost = 2720

--c)

select m.cnp, e.event_id, a.assignment_id
from ManagerEventAssignment a
inner join Manager m on m.cnp = a.m_cnp
inner join ZooEvent e on e.event_id = a.e_id
