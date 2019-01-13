Log Analysis Project

## Introduction
An internal reporting tool is build up using python which will use a database to display the information about the questions like 
1. Which are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Installation

1. Download Vagrant[https://www.vagrantup.com/]
2. Download Virtual Box[https://www.virtualbox.org/wiki/Download_Old_Builds_5_1] depending upon the configuration of the system
3. Use Github to fork and clone the repository by clicking here[https://github.com/udacity/fullstack-nanodegree-vm]
4. Inside the vagrant directory, open Git Bash and run the following command 
`vagrant up`
5. Then again run the following command into the terminal to log into the Linux VM
`vagrant ssh`
6. Load the data by using the following command
`psql -d news -f newsdata.sql`
7. One can connect to the database by `psql news` where news is a database and can explore the data using `\dt` and `\d <tablename>`

## Creating views 
Login into the database by using the following command
`psql news`
Create 5 views by using the following commands


### Popular_Articles View

`create view popular_articles as select substring(l.path,10) as article_name,count(ip) as views from log l,articles ar where ar.slug=substring(l.path,10) group by substring(l.path,10) order by views desc;`

---
### Popular_Article_Authors View
`create view popular_article_authors as select au.name,count(ip) as views from log l,articles ar,authors au where ar.slug=substring(l.path,10) and ar.author=au.id group by au.name order by views desc;`

---
### Error View
`create view error as select count(time) as error_c,cast(time as date) from log where cast(status as text) not like '%200%' group by cast(time as date) order by cast(time as date);`

---
### Total View
`create view total as select count(time) as tot,cast(time as date) order by cast(time as date);`

---
### Error_Percentage

`create view error_percentage as select e.time,cast(round(((e.error_c*100)/t.tot),2) as decimal(5,2)) as error_per from total t,error e where t.time=e.time;`

---
## Running the Project
1. Change the path to get into the project directory.
2.  Type `python news.py` in terminal to run the project. 