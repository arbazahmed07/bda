A) Programs on Data Visualization Techniques (Python)
Data visualization is the process of representing data graphically using charts, graphs, and plots. It helps us understand patterns, trends, and relationships in data.
1. Line Chart
A line chart is used to represent changes in data over time.

Program:
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 180, 200]

plt.plot(months, sales, marker='o')

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()


Output: A line graph showing monthly sales variations.
2. Bar Chart
A bar chart compares different categories of data.

import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D']
marks = [85, 90, 75, 95]

plt.bar(students, marks, color='blue')

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()


Output: A bar graph comparing student marks.
3. Pie Chart
A pie chart represents data in the form of slices and shows percentage distribution.

import matplotlib.pyplot as plt

subjects = ['Python', 'Java', 'C++', 'JavaScript']
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects, autopct='%1.1f%%')

plt.title("Subject Distribution")

plt.show()



Output: A pie chart showing the percentage distribution of subjects.
4. Histogram
A histogram represents the frequency distribution of numerical data.
import matplotlib.pyplot as plt
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()



Output: A histogram showing the distribution of marks.
5. Scatter Plot
A scatter plot shows the relationship between two numerical variables.

import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 60, 70, 85]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()


Output: A scatter plot showing the relationship between study hours and marks.