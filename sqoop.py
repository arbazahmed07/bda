Q1. Enter the MySQL CLI in Cloudera
mysql -u root -pcloudera


Q2. Create a Database
CREATE DATABASE sqoop_db;


Q3. Select the Database
USE sqoop_db;


Q4. Create a Table in the Database
CREATE TABLE emp (
    empno INT PRIMARY KEY,
    ename VARCHAR(10),
    job VARCHAR(9),
    mgr INT,
    hiredate DATE,
    sal INT,
    deptno INT
);


Q5. Insert Records into the Table
INSERT INTO emp VALUES
(1, 'ABC', 'teacher', 100, '2013-01-12', 50000, 10);

INSERT INTO emp VALUES
(2, 'XYZ', 'teacher', 200, '2014-10-02', 650000, 20);

INSERT INTO emp VALUES
(3, 'PQRS', 'teacher', 200, '2010-10-02', 640000, 30);


Q6. Display the Contents of the Table
SELECT * FROM emp;



Sqoop – Import
Q7. Import a MySQL Table into HDFS
Run this command in the Linux terminal:
sqoop import --connect jdbc:mysql://localhost/sqoop_db --username root --password cloudera --table emp --target-dir /user/cloudera/scoop_data


Q8. Check Whether Data Is Imported into HDFS
hadoop fs -ls /user/cloudera/scoop_data


Q9. Display Records from the Imported Partitions
First partition:
hadoop fs -cat /user/cloudera/scoop_data/part-m-00000


Second partition:
hadoop fs -cat /user/cloudera/scoop_data/part-m-00001


Third partition:
hadoop fs -cat /user/cloudera/scoop_data/part-m-00002



Sqoop – Export
Q10. Export Data from HDFS into a MySQL Table
Step 1: Create a local file.
gedit abc.txt


Example contents:
1,2,3


Step 2: Copy the file to HDFS.
hadoop fs -put abc.txt /user/cloudera/


Step 3: Select the database in MySQL.
USE sqoop_db;


Step 4: Create the destination table.
CREATE TABLE abc_table (
    a INT,
    b INT,
    c INT
);


Step 5: Export the HDFS data to MySQL.

Run this command in the Linux terminal:
sqoop export --connect jdbc:mysql://localhost/sqoop_db --username root --password cloudera --table abc_table --export-dir /user/cloudera/abc.txt --input-fields-terminated-by ','


Q11. Verify the Exported Data in MySQL
SELECT * FROM abc_table;


Important: For Sqoop export, --export-dir should ideally point to an HDFS directory containing the data files. To follow the standard approach, you can create a directory for the file:
hadoop fs -mkdir /user/cloudera/abc_data
hadoop fs -mv /user/cloudera/abc.txt /user/cloudera/abc_data/


Then use:
sqoop export --connect jdbc:mysql://localhost/sqoop_db --username root --password cloudera --table abc_table --export-dir /us