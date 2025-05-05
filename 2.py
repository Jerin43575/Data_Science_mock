import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')
df.dropna(inplace=True)
df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'])
df.drop_duplicates(inplace=True)
top_product=df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)
print(top_product)
monthly_sales=df.groupby(df['ORDERDATE'].dt.to_period("M"))['SALES'].sum()
print(monthly_sales)
print(df.select_dtypes(include="number").columns)

top_product.plot(kind='bar',title='Sales by Products')
monthly_sales.plot(kind='line',title="Monthly Sales")
import plotly.express as px
fig=px. bar(df,x='PRODUCTLINE',y='SALES',color='PRODUCTLINE',title='Sales by Product')
fig.show()