--create database modelPrEx
--go

create table Stations(
	sid int primary key identity,
	sname varchar(50) unique
)


create table TrainTypes(
	ttid int primary key identity,
	description varchar(50)
)

create table Trains(
	tid int primary key identity,
	tname varchar(50),

	ttid int foreign key references TrainTypes(ttid)
)

create table Routes(
	rid int primary key identity,
	rname varchar(50) unique,
	tid int foreign key references Trains(tid)
)

create table Stops(
	rid int foreign key references Routes(rid),
	sid int foreign key references Stations(sid),
	arrival time,
	departure time

	constraint pk_Stops primary key(rid, sid)
)

go
create or alter procedure addStops @rid int, @sid int, @arr time, @depart time
as
	declare @nr int;
	set @nr = 0;
	select @nr = count(*) from Stops where rid = @rid and sid = @sid
	if (@nr <> 0 ) begin
		update Stops
		set arrival = @arr, departure = @depart
		where rid = @rid and sid = @sid
	end
	else begin
		insert into Stops values (@rid, @sid, @arr, @depart)
	end
go


create table R(
	FK1 int not null,
	FK2 int not null,
	C1 varchar(100) not null,
	C2 varchar(100) not null,
	C3 int not null,
	C4 int not null,
	C5 varchar(100) not null,
	constraint pk_R primary key (FK1, FK2)
)


insert into R(FK1, FK2, C1,C2,C3,C4,C5) values
(1,1,'Pisica pe acoperisul fierbinte', 'Tennessee Williams', 100, 20, 'AB'),
(1,2,'Conul Leonida fata cu reactiunea', 'Ion Luca Caragiale', 50, 50, 'CQ'),
(1,3,'Concert din muzica de Bach', 'Hortensia Papadat-Bengescu', 50, 10, 'QC'),
(2,1, 'Fata babei si fata mosneagului', 'Ion Creanga', 100,100,'QM'),
(2,2,'Frumosii nebuni ai marilor orase', 'Fanus Neagu', 10,10,'BA'),
(2,3,'Frumoasa calatorie a ursilor panda povestita de un saxofonist care avea o iubita la Frankfurt', 'Matei Visniec', 100, 20, 'MQ'),
(3,1,'Mansarda la Paris cu vedere spre moarte', 'Matei Visniec', 100,50,'PQ'),
(3,2,'Richard al III-lea se interzice sau Scene din viata lui Meyerhold', 'Matei Visniec', 100, 50,'PQ'),
(3,3, 'Masinaria Cehov. Nina sau despre fragilitatea pescarusilor impaiati','Matei Visniec', 100,100,'AZ'),
(4,1,'Omul de zapada care voia sa intalneasca soarele', 'Matei Visniec', 100,100,'CP'),
(4,2,'Extraterestrul care isi dorea ca amintire o pijama', 'Matei Visniec', 50,10,'CQ'),
(4,3,'O  femeie draguta cu o floare si ferestre spre nord', 'Edvard Radzinski', 10,100,'CP'),
(4,4,'Trenul din zori nu mai opreste aici', 'Tennessee Williams', 200, 100, 'MA')

update r
set c3 = 200, c4 = 10
where fk1 = 3 and fk2 = 1

select C2,sum(C3) totalc3, avg(C3) avgc3
FROM R
WHERE C3>=100 OR C1 LIKE '%Pisica%'
group by c2
having sum(c3) > 100

select *
from 
(select FK1, fk2, c3 + c4 Totalc3c4 from r
where fk1 = fk2) r1
inner join (select fk1, fk2, c5
from r
where c5 like '%Q%') r2 on r1.fk1 = r2.fk1 and r1.fk2 = r2.fk2

create or alter trigger TrOnUpdate
on r
for update as
declare @total int = 0
select @total = SUM(i.c3 - d.c3)
from deleted d inner join inserted i on d.fk1 = i.fk1 and d.fk2 = i.fk2 
where d.c3 < i.c3
print @total

update r
set c3 = 300
where fk1 < fk2