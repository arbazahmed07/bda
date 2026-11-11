# Pig Latin Program to Count Number of Logs Per Day


1. Create a log file (logs.txt)

Command:
gedit logs.txt


Enter the following data:
2026-10-28 INFO Login
2026-10-28 ERROR Failed
2026-10-29 INFO Logout
2026-10-29 INFO Login
2026-10-29 ERROR Failed


2. Load file into HDFS
hdfs dfs -mkdir -p /user/hadoop
hdfs dfs -put logs.txt /user/hadoop/


3. Create Pig Latin program (logs.pig)
logs = LOAD '/user/hadoop/logs.txt'
USING PigStorage(' ')
AS (date:chararray, level:chararray, msg:chararray);

grouped = GROUP logs BY date;

result = FOREACH grouped
GENERATE group, COUNT(logs);

DUMP result;


4. Run Pig program
pig logs.pig


Output:
(2026-10-28,2)
(2026-10-29,3)


Result: Successfully counted the number of logs generated per day using Pig Latin.