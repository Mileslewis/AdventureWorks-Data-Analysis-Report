import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('Queries/Q5 - Totalled Orders per stores Last Year.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head())

plt.scatter(df['YearOpened'],df['total_revenue'])
# plt.plot(df['Trading_Duration'], a * df['Trading_Duration'] + b, c = 'red') # line of best fit
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K','$350K','$400K','$450K','$500K'])
plt.xlabel('Store Established')
plt.ylabel('Annual Revenue')
plt.title("Revenue Figures Per Store From Last Years Recorded Orders")
plt.tight_layout()
plt.show()