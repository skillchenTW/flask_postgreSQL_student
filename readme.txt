create table students(
	id serial primary key,
	fname varchar(40) not null,
	lname varchar(40) not null,
	email varchar(100) not null	
);

select * from students;

insert into students(id,fname,lname,email)
values
('7','Quinn','Flynn','flynn@hotmail.com'),
('8','Tiger','nizon','nizon@gmail.com'),
('9','Airi','sato','sato@gmail.com');

alter sequence students_id_seq restart with 10;


參考網站:
https://datatables.net/examples/styling/bootstrap4.html
