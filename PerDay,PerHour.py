# Experiment: Pig Latin – Count Logs Per Day and Per Hour
# Aim
# To load log data from HDFS using Pig Latin and calculate the number of logs per day, per hour, and per day-hour combination.

1. Create a log file
Command:
gedit logs.txt


Enter data:
2026-10-25,09,User Login
2026-10-25,09,Page Visited
2026-10-25,10,User Logout
2026-10-25,10,User Login
2026-10-26,09,Error Occurred
2026-10-26,09,User Login
2026-10-26,11,Page Visited
2026-10-27,10,User Login
2026-10-27,10,Page Visited


2. Load file into HDFS
hadoop fs -put logs.txt /user/cloudera/


3. Start Pig Grunt shell
pig


4. Load log data
A = LOAD '/user/cloudera/logs.txt'
USING PigStorage(',')
AS (log_date:chararray, log_hour:chararray, message:chararray);


5. Display data
DUMP A;


6. Count logs per day
B = GROUP A BY log_date;

C = FOREACH B GENERATE
    group AS log_date,
    COUNT(A) AS total_logs;

DUMP C;


Output:
(2026-10-25,4)
(2026-10-26,3)
(2026-10-27,2)


7. Count logs per hour
D = GROUP A BY log_hour;

E = FOREACH D GENERATE
    group AS log_hour,
    COUNT(A) AS total_logs;

DUMP E;


Output:
(09,4)
(10,4)
(11,1)


8. Count logs per day and hour
F = GROUP A BY (log_date, log_hour);

G = FOREACH F GENERATE
    group.log_date,
    group.log_hour,
    COUNT(A);

DUMP G;


Output:
(2026-10-25,09,2)
(2026-10-25,10,2)
(2026-10-26,09,2)
(2026-10-26,11,1)
(2026-10-27,10,2)


9. Store results in HDFS (Optional)
STORE C INTO '/user/cloudera/daily_logs';
STORE E INTO '/user/cloudera/hourly_logs';
STORE G INTO '/user/cloudera/daily_hourly_logs';