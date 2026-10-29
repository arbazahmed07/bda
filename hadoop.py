Q1. Check the Hadoop Version
hadoop version


Q2. List Files and Subdirectories in HDFS
hadoop fs -ls


Q3. List All Directories Under the HDFS Root Directory
hadoop fs -ls /


Q4. Copy a File from Local File System to HDFS
hadoop fs -copyFromLocal students.txt /user/cloudera


Q5. Check Whether a File Is Copied to HDFS
hadoop fs -ls


Q6. Display the Contents of a File in HDFS
hadoop fs -cat students.txt


Q7. Copy a Local File to HDFS Using the put Command
hadoop fs -put students.txt /user/cloudera/studentscopied.txt


Q8. Copy a File from HDFS to the Local File System
hadoop fs -copyToLocal students.txt studentscopiedtolocal.txt


Q9. Check the Health of the Hadoop File System
hdfs fsck /


Q10. Create a Directory in HDFS
hadoop fs -mkdir /kriti2018


Q11. Copy a File from One HDFS Location to Another
hadoop fs -cp /user/cloudera/kriti.txt /user/cloudera/kriti2018


Q12. Create an Empty File in HDFS
hadoop fs -touchz /user/cloudera/empty.txt


Q13. Check the Size of a File in HDFS
hadoop fs -du /user/cloudera/students.txt


To display the total size:
hadoop fs -du -s /user/cloudera/students.txt


Q14. Print the Contents of a File Stored in HDFS
hadoop fs -cat /user/cloudera/students.txt


Q15. Count Directories, Files, and Bytes in HDFS
hadoop fs -count /user/cloudera/kriti2018


Q16. Remove a File from HDFS
hadoop fs -rm /user/cloudera/empty.txt


Q17. Delete a Directory and Its Contents from HDFS
hadoop fs -rm -r /user/cloudera/kriti2018


Q18. Copy a File into a Directory in HDFS
hadoop fs -cp /user/cloudera/dummy3.txt /user/cloudera/kriti2018


Q19. Move a File into a Directory in HDFS
hadoop fs -mv /user/cloudera/emptyfile.txt /user/cloudera/kriti2018


Q20. Display Help for an Individual HDFS Command
hdfs dfs -usage mkdir


Q21. Display Help for a Given or All HDFS Commands
hadoop fs -help


For help with a specific command:
hadoop fs -help mkdir


Q22. Check HDFS Disk Space and Memory Availability
hadoop fs -df


To check the HDFS root:
hadoop fs -df /


Q23. Check and Balance Data Distribution Across HDFS Nodes
hadoop balancer


Q24. Change File Permissions to 777
hadoop fs -chmod 777 /user/cloudera/students.txt


Q25. Empty the HDFS Trash
hadoop fs -expunge


Q26. Display the Last Kilobyte of a File in HDFS
hadoop fs -tail /user/cloudera/n.txt


Q27. Append Local File Contents to a File in HDFS
hadoop fs -appendToFile /home/cloudera/Desktop/first.txt /user/cloudera/second.txt


To verify the contents:
hadoop fs -cat /user/cloudera/second.txt