create database CompanyDB;
show databases;

use CompanyDB;

create table Employees(EmpID Int Primary Key, EmpName varchar(255), Salary int(5), JoinDate date);

desc Employees;

create table Departments(DeptID Int Primary Key, DeptName varchar(255));


alter table Employees 
add email varchar(100);

alter table Departments 
add dept_location varchar(100);

alter table Employees 
add Phone varchar(10),
add Age int;

alter table Employees 
modify Phone varchar(10) NOT NULL;

alter table Employees 
modify EmpName varchar(100);

alter table departments
drop primary key;

alter table departments
add primary key(DeptID);
