import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('Queries/Q5 - Store Survey Duration and Revenue.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head())

#print(f"N = {len(df['Trading_Duration'])}")
#print(np.corrcoef([df['Trading_Duration'],df['AnnualRevenue']]))
a,b = np.polyfit(df['Trading_Duration'], df['AnnualRevenue'], 1)
#print(a,b)

plt.scatter(df['Trading_Duration'],df['AnnualRevenue'])
# plt.plot(df['Trading_Duration'], a * df['Trading_Duration'] + b, c = 'red') # line of best fit
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K'])
plt.xlabel('Trading Duration (Years)')
plt.ylabel('Annual Revenue')
plt.title("Annual Revenue by Trading Duration (Store Survey)")
plt.tight_layout()
plt.show()
plt.clf()

query = open('Queries/Q5 - Average Revenue 5 Year Groups.sql').read()
# print(query)
df = pd.read_sql_query(query, conn)
# print(df.head(10))

plt.bar(df['year_group'],df['avg_rev'],width =5,align = 'edge',linewidth= 0.2,edgecolor='black')
plt.xlabel('Year Established')
plt.ylabel('Annual Revenue')
plt.title("Average Annual Revenue by Year Established")
plt.text(x = 2000.5,y = 50000,s = ' Few\n stores\nopened')
plt.yticks(ticks = [0,25000,50000,75000,100000,125000,150000,175000],labels = ['$0K','$25K','$50K','$75K','$100K','$125K','$150K','$175K'])
plt.tight_layout()
plt.show()