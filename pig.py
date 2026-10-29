Q1. Enter the Grunt Shell
pig


Q2. Create Two Datasets Using the gedit Command in Local System
Create the first file:
gedit pigfile.txt


Contents:
1,2,3
4,5,6
5,7,0


Create the second file:
gedit pigfile1.txt


Contents:
2,4,5
2,4,5
4,7,9


Q3. Copy the Files from Local System to HDFS
hadoop fs -put pigfile.txt /user/cloudera/
hadoop fs -put pigfile1.txt /user/cloudera/


Q4. Load and Read the Datasets in Pig
a = LOAD '/user/cloudera/pigfile.txt' USING PigStorage(',');
DUMP a;

b = LOAD '/user/cloudera/pigfile1.txt' USING PigStorage(',');
DUMP b;


Q5. Specify the Schema for Both Datasets
a = LOAD '/user/cloudera/pigfile.txt' USING PigStorage(',')
    AS (a1:int, a2:int, a3:int);
DUMP a;

b = LOAD '/user/cloudera/pigfile1.txt' USING PigStorage(',')
    AS (b1:int, b2:int, b3:int);
DUMP b;


Q6. Check the Schema of Both Datasets
DESCRIBE a;
DESCRIBE b;


Q7. Combine Two Datasets Using UNION
c = UNION a, b;
DUMP c;


Q8. Split a Dataset into Two Relations Using SPLIT
SPLIT c INTO d IF $0 == 1, e IF $0 == 4;

DUMP d;
DUMP e;


- d contains records where the first column equals 1.
- e contains records where the first column equals 4.
Q9. Filter a Dataset Where Column 1 Is Greater Than 6
f = FILTER c BY $1 > 6;
DUMP f;


Q10. Group a Dataset by Column 2
g = GROUP c BY $2;
DUMP g;


Q11. Select Columns 1 and 2 from Dataset a
s1 = FOREACH a GENERATE $1, $2;
DUMP s1;


Q12. Store the Result in HDFS
STORE s1 INTO '/user/cloudera/pigresult';


Q13. Check the Files Written to HDFS
hadoop fs -ls /user/cloudera/pigresult/


Q14. Display the Contents of the Output File
hadoop fs -cat /user/cloudera/pigresult/part-m-00000