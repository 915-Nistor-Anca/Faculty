--create database PracticalExam
--go

use PracticalExam
go

create table TeamType(
typeid int primary key IDENTITY,
maxnumber int not null
)

create table Sport(
sportid int primary key IDENTITY,
sportname varchar(50) not null,
sportdescription varchar(50) not null
)

create table Team(
teamid int primary key IDENTITY,
teamname varchar(50) not null,
numberofmembers int not null,
startupyear int not null,
city varchar(50) not null,

typeid int foreign key references TeamType(typeid),
sportid int foreign key references Sport(sportid)
)


create table Player(
playerid int primary key IDENTITY,
playername varchar(50) not null,
playersurname varchar(50) not null,
birthday datetime not null,
gender varchar(50) not null
)

create table ContractPlayerTeam(
startdate datetime not null,
enddate datetime not null,

playerid int foreign key references Player(playerid),
teamid int foreign key references Team(teamid),

constraint PK_Contract primary key
)


--non-repeatable reads
set transaction isolation level read
committed
begin tran
select * from Player
waitfor delay '00:00:05'
update Player set playersurname = 'x' where playerid = 1
commit tran

--non-repeatable reads solution
set transaction isolation level repeatable
read
begin tran
select * from Player
waitfor delay '00:00:05'
select * from Player
commit tran