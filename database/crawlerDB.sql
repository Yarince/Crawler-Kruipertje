/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     8-5-2017 09:42:03                            */
/*==============================================================*/
-- drop database if exists crawlerDB;

-- create database crawlerDB;

use crawlerDB;

drop table if exists url;

/*==============================================================*/
/* Table: URL                                                   */
/*==============================================================*/
create table url
(
   id					varbinary(255) primary key,
   url                  varchar(255) unique,
   ip_address           varchar(15) not null,
   last_visited         datetime not null,
   date_found			datetime null
);

-- CREATE user IF NOT EXISTS 'Python'@'localhost' IDENTIFIED BY 'Password_2017';
-- Grant outside access
-- GRANT ALL PRIVILEGES ON crawlerDB . * TO 'Python'@'%' IDENTIFIED BY 'Password_2017';

-- Example
insert into url values(unhex('1220135900da0a130c60d5e24b0e1eff'), 'http://technovium.nl','0.0.0.0', now(), null);