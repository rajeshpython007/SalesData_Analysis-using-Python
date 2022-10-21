#!/usr/bin/env python
# coding: utf-8

# # SALES ANALYSIS USING PYTHON - Jupyter

# # 𝐎𝐁𝐉𝐄𝐂𝐓𝐈𝐕𝐄

# 𝑻𝒐 𝒇𝒊𝒏𝒅 𝒕𝒉𝒆 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈:
# 
# 1.𝒐𝒗𝒆𝒓𝒂𝒍𝒍 𝒔𝒂𝒍𝒆𝒔 𝒕𝒓𝒆𝒏𝒅  
# 
# 2.𝑻𝒐𝒑 10 𝒑𝒓𝒐𝒅𝒖𝒄𝒕𝒔 𝒃𝒚 𝒔𝒂𝒍𝒆𝒔.  
# 
# 3.𝑴𝒐𝒔𝒕 𝑺𝒆𝒍𝒍𝒊𝒏𝒈 𝑷𝒓𝒐𝒅𝒖𝒄𝒕𝒔  
# 
# 4.𝑴𝒐𝒔𝒕 𝒑𝒓𝒆𝒇𝒆𝒓𝒓𝒆𝒅 𝑺𝒉𝒊𝒑𝒑𝒊𝒏𝒈 𝑴𝒐𝒅𝒆  
# 
# 5.𝑴𝒐𝒔𝒕 𝑷𝒓𝒐𝒇𝒊𝒕𝒂𝒃𝒍𝒆 𝑪𝒂𝒕𝒆𝒈𝒐𝒓𝒚 𝒂𝒏𝒅 𝑺𝒖𝒃-𝑪𝒂𝒕𝒆𝒈𝒐𝒓𝒚

# # THE LIBRARIES USED

# 1. 𝙋𝙖𝙣𝙙𝙖𝙨                  - 𝙁𝙤𝙧 𝙙𝙖𝙩𝙖 𝙢𝙖𝙣𝙞𝙥𝙪𝙡𝙖𝙩𝙞𝙤𝙣, 𝙚𝙭𝙥𝙡𝙤𝙧𝙞𝙩𝙖𝙩𝙞𝙫𝙚 𝙙𝙖𝙩𝙖 𝙖𝙣𝙖𝙡𝙮𝙨𝙞𝙨.
# 
# 2. 𝙈𝙖𝙩𝙥𝙡𝙤𝙩𝙡𝙞𝙗 𝙖𝙣𝙙 𝙎𝙚𝙖𝙗𝙤𝙧𝙣  - 𝙁𝙤𝙧 𝘿𝙖𝙩𝙖 𝙑𝙞𝙨𝙪𝙖𝙡𝙞𝙯𝙖𝙩𝙞𝙤𝙣  
# 
# 3. %𝙢𝙖𝙩𝙥𝙡𝙤𝙩𝙡𝙞𝙗 𝙞𝙣𝙡𝙞𝙣𝙚       - 𝙁𝙤𝙧 𝙞𝙣𝙡𝙞𝙣𝙞𝙣𝙜 𝙩𝙤 𝙙𝙞𝙨𝙥𝙡𝙖𝙮 𝙩𝙝𝙚 𝙤𝙪𝙩𝙥𝙪𝙩 𝙤𝙛 𝙥𝙡𝙤𝙩𝙩𝙞𝙣𝙜 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙞𝙣𝙡𝙞𝙣𝙚 𝙬𝙞𝙩𝙝𝙞𝙣 𝙛𝙧𝙤𝙣𝙩𝙚𝙣𝙙𝙨.

# # DATASET USED : US SUPERSTORE SALES 

# In[8]:


#importing the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#Creation of dataframe by using the data-set which is in excel.
#importing the excel file.
df = pd.read_excel("E:\\DATA SCIENCE\\Project\\python\\Data Analysis\\Sales\\superstore_sales.xlsx")


# # Exploratory_DataAnalysis

# In[7]:


#Let's Display the Top 5 rows of the data-frame.

df.head()


# # The Number of Rows and Columns that are available in this data-set.

# In[10]:


df.shape


# FINDINGS - 
# Rows    : 21
# Columns : 51,290

# # Summary Of Sales-Dataset.
# 1. Number of Non-Null Values in each column.
# 2. Data-Type of each column.
# 3. Memory used.

# In[12]:


df.info()


# # Number of  Null_Values in each column?

# In[13]:


df.isnull().sum()


# Findings : There are no null_values in the dataset. 

# # Date Of Entry of first data into data_set?

# In[14]:


df['order_date'].min()


# FINDINGS : On 1st January of 2011 the 1st data was entered.

# # Date Of Entry of last data into data_set?

# In[15]:


df['order_date'].max()


# FINDINGS : On 31st December 2014 the last data was entered.

# # Month of Order Date from the data_set.

# In[21]:


df['month'] = df['order_date'].apply(lambda x: x.strftime('%m'))
#apply is for applyig the condition to each row.
#strftime is to convert date object to string representation.


# In[22]:


df['month']


# # TOP 10 Products Based On sales.

# In[59]:


#Grouping 'Products' based on 'Sales'.
prod_bySales = pd.DataFrame(df.groupby('product_name').sum(numeric_only=True)['sales'])

#Sorting the sales in descending order. 
#Fuction 'sort_values' - To sort the data in asc/desc order) Of Passed Columns.
prod_bySales.sort_values(by=['sales'],ascending=False, inplace = True )

#TOP10 Products
prod_bySales[:10]


# # Most Sold Products 

# In[61]:


#grouping the products based on Sold Quantity.
most_sold_products = pd.DataFrame(df.groupby('product_name').sum(numeric_only=True)['quantity'])

#sorting the values in descending order by using the 'sort_values' function and making the 'inplace' true.
most_sold_products.sort_values(by=['quantity'],ascending=False, inplace = True)

#Top10
most_sold_products[:10]


# # Most Profitable Products .

# In[66]:


#grouping the products based on Profit.
most_profitable_product = pd.DataFrame(df.groupby('product_name').sum(numeric_only=True)['profit'])

#sorting the values in descending order by using the 'sort_values' function and making the 'inplace' True.
most_profitable_product.sort_values(by=['profit'],ascending=False, inplace = True)

#Top
most_sold_products[:1]


# # Most Preferred mode of shipment.

# In[73]:


#grouping the products based on number of quantity.
mst_prfrd_shipmnt = pd.DataFrame(df.groupby('ship_mode').sum(numeric_only=True)['quantity'])

#sorting the values is descending order.
mst_prfrd_shipmnt.sort_values(by=['quantity'],ascending=False, inplace = True)

mst_prfrd_shipmnt[:5]


# # Most Preferred mode-of-shipment by Visualization.
# #we will use seaborn library here to count as well as visualize.

# In[84]:


sns.countplot(x='ship_mode', data=df) #countplot :counts the no of observation in each category. 
plt.figure(figsize=(10,10)) #figsize: depicts the size of plot.
plt.show() #displaying the plot.


# # Statistical Summary of Whole Dataset

# In[96]:


# describe method gives descriptive statistics of the data frame.Tt only shows the statistics on the numerical columns.

df.describe().round()


# In[ ]:




