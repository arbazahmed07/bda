Q1. Enter the Hive Shell
hive


Q2. Create and Select a Database
CREATE DATABASE emp_details;
USE emp_details;


Q3. Create a Managed (Internal) Table
CREATE TABLE emp (
    empno INT,
    ename STRING,
    job STRING,
    sal INT,
    deptno INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


Q4. Load Data from Local File System into a Hive Table
LOAD DATA LOCAL INPATH
'/home/cloudera/Desktop/empdetails.txt'
OVERWRITE INTO TABLE emp;


Q5. Check the Location of a Managed Table in HDFS
hadoop fs -ls /user/hive/warehouse/emp_details.db


List the files inside the emp table directory:
hadoop fs -ls /user/hive/warehouse/emp_details.db/emp


Display the data file contents:
hadoop fs -cat /user/hive/warehouse/emp_details.db/emp/empdetails.txt


Q6. Check the Schema of a Table
DESCRIBE emp;


For detailed table information:
DESCRIBE EXTENDED emp;


Q7. Display All Tables in the Current Database
SHOW TABLES;


Q8. Select All Employee Names
SELECT ename FROM emp;


Q9. Retrieve Records Where Employee Name Is 'A'
SELECT * FROM emp WHERE ename = 'A';


Q10. Count the Total Number of Records
SELECT COUNT(1) FROM emp;


Alternatively:
SELECT COUNT(*) FROM emp;


Q11. Calculate the Sum of Salaries for Each Department
SELECT deptno, SUM(sal)
FROM emp
GROUP BY deptno;


Q12. Retrieve Employees Whose Salary Is Between 1000 and 2000
SELECT * FROM emp
WHERE sal BETWEEN 1000 AND 2000;


Q13. Select Employees Whose Job Has Exactly Five Characters
SELECT ename FROM emp
WHERE job LIKE '_____';


Q14. Select Employees Whose Job Has 'l' as the Second Character
SELECT ename FROM emp
WHERE job LIKE '_l%';


Q15. Retrieve the Total Salary for Each Department
SELECT deptno, SUM(sal)
FROM emp
GROUP BY deptno;


Q16. Add a New Column to a Table
ALTER TABLE emp ADD COLUMNS (lastname STRING);


Q17. Rename a Table
ALTER TABLE emp RENAME TO emp1;


Q18. Drop a Table
DROP TABLE emp;



Database Management Commands
Q19. Display All Databases
SHOW DATABASES;


Q20. Create a Database
CREATE DATABASE hiveDemoDb;


Q21. Create Another Database
CREATE DATABASE hiveDemoDb1;


Q22. Drop a Database
DROP DATABASE hiveDemoDb1;



Managed Table Commands
Q23. Create a Managed Table
CREATE TABLE hiveDemoDb.employee (
    Id INT,
    Name STRING,
    Salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';


Q24. Describe a Table
DESCRIBE hiveDemoDb.employee;


Q25. Create a Table Using the Schema of an Existing Table
CREATE TABLE IF NOT EXISTS hiveDemoDb.copy_employee
LIKE hiveDemoDb.employee;


Q26. Create a Table with Column Comments and Table Properties
CREATE TABLE hiveDemoDb.new_employee (
    Id INT COMMENT 'Employee Id',
    Name STRING COMMENT 'Employee Name',
    Salary FLOAT COMMENT 'Employee Salary'
)
COMMENT 'Table Description'
TBLPROPERTIES (
    'creator' = 'Gaurav Chawla',
    'created_at' = '2021-11-30 11:00:00'
);


Q27. View the Table Schema
DESCRIBE hiveDemoDb.new_employee;



External Table Commands
Q28. Create a Directory in HDFS
hdfs dfs -mkdir /HiveDirectory


Q29. Create an External Table
CREATE EXTERNAL TABLE emplist (
    Id INT,
    Name STRING,
    Salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/HiveDirectory';


Q30. Display Records from the External Table
SELECT * FROM emplist;


Q31. Insert a Record into the External Table
INSERT INTO TABLE emplist
VALUES (11, 'John', 70000);


Q32. Insert Another Record
INSERT INTO TABLE emplist
VALUES (12, 'Robert', 80000);


Q33. Insert a Third Record
INSERT INTO TABLE emplist
VALUES (13, 'Catherine', 90000);


Q34. Display All Records from the External Table
SELECT * FROM emplist;