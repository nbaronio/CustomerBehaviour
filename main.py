import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

# import the dataset
df = pd.read_csv("customer_data.csv")
df.head()

# 1. Dataset Exploration

# this dataset is containing different informations about the demographic of a customer (age, gender, income...)
# and the good that he/she is buying.

# seeing how many rows and columns there are in the dataset
df.shape

# seeing the types of the variables
df.dtypes

# seeing how many null rows there are in the dataset
df.isnull().sum()
# there are no NULL rows! yuppi!

# let's drop the ID column and the promotion usage, we dont need them
df.drop(columns="id", inplace = True)
df.drop(columns="promotion_usage", inplace = True)

# let's delve into the demographics of the customers

# we don't want the warnings 
warnings.filterwarnings("ignore")

# we create a barplot to confront number of male and females (watch out for the colors!)
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))
colors = ['pink', 'lightblue']
ax = sns.countplot(x='gender', data=df, palette=colors)
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# let's create a pie chart to see different education levels

# at first, let's see how many have each degree
education_counts = df['education'].value_counts()
education_counts
labels = education_counts.index
sizes = education_counts.values
# we want to show (explode) the 'master' index
master_index = labels.tolist().index('Masters')
explode = [0] * len(labels)
explode[master_index] = 0.1 # Explode the 'Masters' slice
plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Education Levels')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# this way we can see that the majority of people have a College degree (almost 40%), while the least 
# common degree is the Master degree (9.8%)


# let's do the same thing for the type of product bought
category_counts = df['product_category'].value_counts()
category_counts
category_labels = category_counts.index
category_sizes = category_counts.values
plt.figure(figsize=(8,8))
plt.pie(category_sizes, labels = category_labels, 
        autopct='%1.1f%%', startangle=140)
plt.title('Distribution of bought products')
plt.axis('equal')
plt.show()

# i would like to know depending on the gender the income and how much of that income the person spends
# ON AVERAGE, for each type of good

# i tried to do it but I was using means of incomes and purchase_amounts for each good, and in some cases
# the income was smaller than the purchase_amount
# so i prefer to wait until a new better idea concerning how to develop this model come out to me 

# GOOD IDEA FROM LUDO


## i can show what each category of degree buy (product category for each degree class)

group_ed_cat = df.groupby(['product_category', 'education']).size().unstack(fill_value=0)

# Plotting subplots as pie charts
fig, axes = plt.subplots(nrows=1, ncols=len(group_ed_cat.columns), figsize=(64, 64))

# Iterate over each column (education level) and plot a pie chart
for i, col in enumerate(group_ed_cat.columns):
    group_ed_cat[col].plot.pie(ax=axes[i], autopct='%1.1f%%', labels=group_ed_cat.index, legend=None)

plt.show()

# as we can see there are no specific differences between different education levels in buying different 
# types of goods


## let's see where the customers come from
region = df['region']

region_count = region.value_counts()
region_color = ['red','yellow','green','skyblue']
region_count.plot(kind='bar', color = ['#4285F4','#34A853','#FBBC05','#EA4335'])
plt.show()


## let's see which are the differences in the various product categories based on the region
group_reg_cat = df.groupby(['product_category','region']).size().unstack(fill_value=0)
group_reg_cat

# plotting subplots as pie charts
fig1, axes1 = plt.subplots(nrows=1, ncols=len(group_reg_cat.columns), figsize=(64,64))

# and as we did before let's iterate the same function for every region
for i,col in enumerate(group_reg_cat):
    group_reg_cat[col].plot.pie(ax=axes1[i],autopct='%1.1f%%', labels=group_reg_cat.index, legend=None)
plt.show()

