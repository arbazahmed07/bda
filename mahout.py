# B) Mahout Machine Learning Library
# Aim
# To perform K-Means clustering using Apache Mahout.
# Program

# Create input directory
hdfs dfs -mkdir -p /mahout/input

# Create dataset
gedit data.txt


Enter the data:
1,1
2,2
3,3
8,8
9,9
10,10


Upload the dataset:
hdfs dfs -put data.txt /mahout/input/


Run Mahout K-Means:
mahout kmeans \
-i /mahout/input \
-c /mahout/clusters \
-o /mahout/output \
-k 2 \
-x 10


Output
Cluster 1:
(1,1)
(2,2)
(3,3)

Cluster 2:
(8,8)
(9,9)
(10,10)