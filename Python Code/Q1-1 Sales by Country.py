import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LBP-PC0H1X3H\MSSQLSERVER01;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('Q1,3 Sales by Country Name.sql').read()
print(query)
df = pd.read_sql_query(query, conn)
print(df)

# Stacked horizontal bar chart for Sales by Country
Y_axis = np.arange(len(df['CountryName']))
plt.barh(df['CountryName'],df['Sales_LastYear'], 
        label = 'Last Year', color='steelblue')
plt.barh(df['CountryName'],df['Sales_YTD'],left = df['Sales_LastYear'],
        label='Year To Date', color='mediumseagreen')
plt.xticks(ticks = [10000000,20000000,30000000,40000000,50000000],
          labels = ["$10M","$20M","$30M","$40M","$50M"])
plt.yticks(Y_axis, df['CountryName'])  
plt.xlabel("Sales")
plt.ylabel("Country")
plt.title("Sales by Country")
plt.legend()
plt.tight_layout()
plt.gca().invert_yaxis()
plt.show()