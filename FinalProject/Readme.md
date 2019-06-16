# How to do
1. install mysql
2. start mysql
    $ sudo systemctl start mysql
3. $ mysql -u [user] -p
    enter password
4. mysql> create database [dbname];
5. mysql> use [dbname];
6. mysql> CREATE TABLE data(name VARSHAR(255), sentence VARCHAR(255));
7. mysql> SET GLOBAL local_infile=1;
8. mysql> LOAD DATA LOCAL INFILE '/Users/rexsung/Downloads/Final_text.txt' INTO TABLE data COLUMNS TERMINATED BY '\t';
9. mysql> exit
10. in server.js line 12~14 -> type your [username], [password] and [dbname]
11. node sever.js
12. localhost:7680
