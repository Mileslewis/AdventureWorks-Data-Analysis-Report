import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('Queries/Q4 - Sick leave by job title.sql').read()
#print(query)

df = pd.read_sql_query(query, conn)
#print(df.head())

plt.bar(df['JobTitle'],df['Average_SickLeave'])
plt.xlabel('Job Title')
plt.ylabel('Average Sick Leave (hours)')
plt.title("Average Sick Leave by Job Title")
plt.xticks(rotation = 45)
plt.show()