--create database PetsAndOwners
--go

use PetsAndOwners
go

create table Pet(
	petid int primary key identity,
	petname varchar(50) not null, 
	weight int not null
)

create table Owner(
	ownerid int primary key identity,
	ownername varchar(50) not null,
	phonenumber varchar(50) not null,
	birthdate date not null,
)

create table Ownership(
	petid int foreign key references Pet(petid),
	ownerid int foreign key references Owner(ownerid),
	
	constraint PK_Ownership primary key(petid, ownerid)
)


create or alter function validateOwnerName (@ownername varchar(50)) returns int as
begin
declare @return int = 0
if (len(@ownername)>=3)
set @return=1
return @return
end
go

create or alter function validateWeight (@weight varchar(50)) returns int as
begin
declare @return int = 0
if (@weight<50)
set @return=1
return @return
end
go

create or alter function validateOwnerAge (@birthdate date) returns int as
begin
declare @return int = 0
declare @current_date date = convert(date, getdate())
if (datediff(YEAR, @birthdate, @current_date) >= 14)
set @return=1
return @return
end
go

create or alter function validateOwnerPhoneNumber (@phonenumber varchar(50)) returns int as
begin
declare @return int = 0
if (@phonenumber like '07%')
set @return=1
return @return
end
go


create or alter procedure AddPetOwner @petname varchar(50), @weight int, @ownername varchar(50), @phonenumber varchar(50), @birthdate date as
begin
begin tran

begin try

if (dbo.validateOwnerName(@ownername)<>1)
begin
	raiserror('Owner name must have more than 3 characters.', 14, 1)
end
if (dbo.validateOwnerAge(@birthdate)<>1)
begin
	raiserror('The owner must be at least 14 years old.', 14, 1)
end
if (dbo.validateOwnerPhoneNumber(@phonenumber)<>1)
begin
	raiserror('The phone number must start with 07', 14, 1)
end
if (dbo.validateWeight(@weight)<>1)
begin
	raiserror('Animal weight should be smaller than 50.', 14, 1)
end

insert into Pet values (@petname, @weight)
declare @petid int = scope_identity()
insert into Owner values (@ownername, @phonenumber, @birthdate)
declare @ownerid int = scope_identity()
insert into Ownership(petid, ownerid) values (@petid, @ownerid)
commit tran
select 'Transaction committed' as 'Transaction message'
end try

begin catch
declare @errormessage varchar(100) = error_message()
rollback tran
select 'Transaction rollbacked' as 'Transaction message', @errormessage as 'Error message'
end catch
end


insert into Pet values ('Fluffy', 5)
insert into Pet values ('Lucky', 8)

insert into Owner values ('Alex', '0737867386', '2002/05/12')
insert into Owner values ('Maria', '0745286735', '2004/08/03')

select * from Pet
select * from Owner
select * from Ownership

exec AddPetOwner @petname = 'Max', @weight = 7, @ownername = 'Laura', @phonenumber = '0736957387', @birthdate = '2000/04/10' --all is ok
exec AddPetOwner @petname = 'Tom', @weight = 5, @ownername = 'Sergiu', @phonenumber = '0736952687', @birthdate = '2020/05/11' --the owner doesnt have 14 years


create or alter procedure AddPetOwner2 @petname varchar(50), @weight int, @ownername varchar(50), @phonenumber varchar(50), @birthdate date as
begin
set nocount on
declare @petid int = null
declare @ownerid int = null

begin try
begin tran
declare @ok int = 0
if (dbo.validateOwnerName(@ownername)<>1)
begin
	set @ok = 1
	raiserror('Owner name must have more than 3 characters.', 14, 1)
end
if (dbo.validateOwnerAge(@birthdate)<>1)
begin
	set @ok = 1
	raiserror('The owner must be at least 14 years old.', 14, 1)
end
if (dbo.validateOwnerPhoneNumber(@phonenumber)<>1)
begin
	set @ok = 1
	raiserror('The phone number must start with 07', 14, 1)
end

if (@ok<>1)
begin 
insert into Pet values (@petname, @weight)
set @petid = scope_identity()
end

if (dbo.validateWeight(@weight)<>1)
begin
	raiserror('Animal weight should be smaller than 50.', 14, 1)
end
else
begin
insert into Owner values (@ownername, @phonenumber, @birthdate)
set @ownerid = scope_identity()
end

if (@petid is not null and @ownerid is not null)
begin
insert into Ownership(petid, ownerid) values (@petid, @ownerid)
end
commit tran
end try
begin catch
declare @errormessage varchar(100) = error_message()
rollback tran
select 'Transaction rollbacked' as 'Transaction message', @errormessage as 'Error message'
end catch
end


exec AddPetOwner2 @petname = 'Figo', @weight = 55, @ownername = 'Elena', @phonenumber = '0736957387', @birthdate = '2000/04/10'

select * from Pet
select * from Owner
select * from Ownership


--dirty reeds
begin transaction
update Pet set petname = 'Suzi'
where petid = 1
waitfor delay '00:00:10'
rollback transaction

--non repeatable reads
insert into Pet(petname, weight) values ('Bibi', 40)
begin tran
waitfor delay '00:00:05'
update Pet set weight = 20 where petname = 'Bibi'

--phantom reads
begin tran
waitfor delay '00:00:04'
insert into Owner(ownername, phonenumber, birthdate) values ('Georgiana', '0735847562', '1999/08/05')
commit tran

--deadlock
begin tran
update Pet set petname = 'Bunny' where id = 1
waitfor delay '00:00:10'
update Owner set ownername = 'Irina' where id = 2
commit tran



--dirty reeds
set transaction isolation level read
uncommitted
begin tran
select * from Pet
waitfor delay '00:00:15'
select * from Pet 
commit tran

--dirty reeds solution
set transaction isolation level read committed
begin tran
select * from Pet
waitfor delay '00:00:15'
select * from Pet 
commit tran

--non-repeatable reads
set transaction isolation level read
committed
begin tran
select * from Pet
waitfor delay '00:00:05'
select * from Pet
commit tran

--non-repeatable reads solution
set transaction isolation level repeatable
read
begin tran
select * from Pet
waitfor delay '00:00:05'
select * from Pet
commit tran

--phantom reads
set transaction isolation level repeatable
read
begin tran
select * from Pet
waitfor delay '00:00:05'
select * from Pet 
commit tran

--phantom reads solution
set transaction isolation level serializable
begin tran
select * from Pet
waitfor delay '00:00:05'
select * from Pet 
commit tran


--deadlock
begin tran
update Pet set petname = 'Zuri' where petid = 1
waitfor delay '00:00:10'
update Owner set ownername = 'Sara' where ownerid = 1
commit tran

--deadlock solution
set deadlock_priority high
begin tran
update Pet set petname = 'Zuri' where petid = 1
waitfor delay '00:00:10'
update Owner set ownername = 'Sara' where ownerid = 1
commit tran

select * from Pet
select * from Owner
select * from Ownership



SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
Select * from Pet where petid=3
Waitfor delay '00:00:10'
select * from Pet where petid=4
Update Pet set petname = 'Beni' where petid=3
COMMIT TRAN


ALTER DATABASE Pet SET ALLOW_SNAPSHOT_ISOLATION ON
waitfor delay '00:00:10'
BEGIN TRAN
UPDATE Pet SET petname = 'Tomi' WHERE petid=3
waitfor delay '00:00:10'
COMMIT TRAN

ALTER DATABASE Pet SET ALLOW_SNAPSHOT_ISOLATION OFF
