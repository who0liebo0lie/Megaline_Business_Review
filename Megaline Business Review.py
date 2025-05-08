#!/usr/bin/env python
# coding: utf-8

# ## Megaline Business Review

# Project Overview:
# Telecom giant Megaline has hired an analyst. The company offers its clients two prepaid plans, Surf and Ultimate. The commercial department wants to know which of the plans brings in more revenue in order to adjust the advertising budget.
# 
# Preliminary analysis of the plans based on a relatively small client selection. Data on 500 Megaline clients: who the clients are, where they're from, which plan they use, and the number of calls they made and text messages they sent in 2018. Following is analyzation of the clients' behavior and determine which prepaid plan brings in more revenue.

# Sprint 3 covers Stastical Data Analysis (SDA)
# 
# Completion of this project will demonstrate ability to load, cleanse, and analyze data.  Project will revolve around evaluating 500 clinets of telecom operator Megaline.  They have two charge options of Surf or Ultimate.  
# 
# Surf
# Monthly charge: $20
# 500 monthly minutes, 50 texts, and 15 GB of data
# After exceeding the package limits:
# 1 minute: 3 cents
# 1 text message: 3 cents
# 1 GB of data: $10
# 
# Ultimate
# Monthly charge: $70
# 3000 monthly minutes, 1000 text messages, and 30 GB of data
# After exceeding the package limits:
# 1 minute: 1 cent
# 1 text message: 1 cent
# 1 GB of data: $7
# 
# 
# The information to evaluate are contained from five different files which are uploaded to their own dataframes.
# 
# The data on users is stored in the "users" dataframe contains columns user_id  (unique user identifier), first_name  (user's name), last_name (user's last name), age (user's age in years), reg_date (subscription date following dd, mm, yy pattern), churn_date (the date the user stopped using the service (if the value is missing, the calling plan was being used when this database was extracted)), city (user's city of residence), and plan  (calling plan name). 
# 
# The "calls" data frame contains the data on calls.  The following columns exist:
# id — unique call identifier
# call_date — call date
# duration — call duration (in minutes)
# user_id — the identifier of the user making the call
# 
# The messages dataframe contains the data on texts.  The following columns exist:
# id — unique text message identifier
# message_date — text message date
# user_id — the identifier of the user sending the text
# 
# The internet dataframe contains data on web sessions.  The following columns exist:
# id — unique session identifier
# mb_used — the volume of data spent during the session (in megabytes)
# session_date — web session date
# user_id — user identifier
# 
# The plans dataframe contains data on the plans.  The following columns exist:
# plan_name — calling plan name
# usd_monthly_fee — monthly charge in US dollars
# minutes_included — monthly minute allowance
# messages_included — monthly text allowance
# mb_per_month_included — data volume allowance (in megabytes)
# usd_per_minute — price per minute after exceeding the package limits (e.g., if the package includes 100 minutes, the 101st minute will be charged)
# usd_per_message — price per text after exceeding the package limits
# usd_per_gb — price per extra gigabyte of data after exceeding the package limits (1 GB = 1024 megabytes)
# 
# 

# ## Initialization

# In[1]:


# Loading all the libraries 
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns 

from scipy import stats as st



# ## Load data

# In[2]:


# Load the data files into different DataFrames
calls = pd.read_csv('/datasets/megaline_calls.csv')
internet= pd.read_csv('/datasets/megaline_internet.csv')
messages = pd.read_csv('/datasets/megaline_messages.csv')
plans = pd.read_csv('/datasets/megaline_plans.csv')
users = pd.read_csv('/datasets/megaline_users.csv')


# ## Prepare the data

# Each file type will be checked for duplicated rows and duplicates in columns (where necessary). Duplicates will be removed if found.  Each file will then be reviewed for missing values 

# In[3]:


#Prepare data from "calls" file
print(calls.duplicated().sum())
#only 2 of the 4 columns matter if they are duplicated.  A call date and duraction can occur for multiple
#users.  However each call should be unique and each user_id should be unique 
print(calls.duplicated('id').sum())
print(calls.duplicated('user_id').sum())

calls.info()


# In[4]:


#check for empty cells in whole row
calls.isna().sum()
#check for empty cells in each column 
#calls['user_id'].isna().sum()
#calls['id'].isna().sum()
#calls['call_date'].isna().sum()
#calls['duration'].isna().sum()

#there are no empties so data clean for use 


# In[5]:


#Prepare data from "users" file
print(users.duplicated().sum())
#only 1 of the 8 columns matter if they are duplicated. Each user should be unique and each user_id should be unique 
print(calls.duplicated('id').sum())

#gather general info
users.info()


# In[6]:


#check for empty cells in whole row
users.isna().sum()


# In[7]:


#churn_date has 466 empty which indicates that they are still current users so replace with NA 
users['churn_date']=users['churn_date'].fillna(pd.to_datetime('today'))
users.isna().sum()


# In[8]:


#Prepare data from "internet" file
print(internet.duplicated().sum())
#none of the columns require unique values so no individual search 

#find general information rearding dataframe
calls.info()
#check for empty cells in whole row
internet.isna().sum()


# In[9]:


#Prepare data from "messages" file
print(messages.duplicated().sum())
#none of the columns require unique values so no individual search 

#find general information rearding dataframe
messages.info()
#check for empty cells in whole row
messages.isna().sum()


# In[10]:


#Prepare data from "plans" file
print(plans.duplicated().sum())
#none of the columns require unique values so no individual search 

#find general information rearding dataframe
plans.info()
#check for empty cells in whole row
plans.isna().sum()


# ## Plans

# In[11]:


# Print the general/summary information about the plans' DataFrame
plans.describe()
plans.isnull().sum()
plans.info()


# In[12]:


# Print a sample of data for plans
plans.head()


# In the plans dataframe printout it is intersting that there are only two rows(one of each plan). There are three different data types (float, int64, and object).  There is no missing data. Noticing that the project instructions give the quanitty of information in GB.  However in the table they are listed as MB (with a correct conversion of 1 GB= 1024 MB).    

#  

# ## Fix data

# ## Enrich data

# In[13]:


plans['gb_per_month']=['15','30']
plans.head()


# ## Users

# In[14]:


# Print the general/summary information about the users' DataFrame
users.describe()
users.isnull().sum()
users.info()


# In[15]:


# Print a sample of data for users
users.head()


# [Describe what you see and notice in the general information and the printed data sample for the above price of data. Are there any issues (inappropriate data types, missing data etc) that may need further investigation and changes? How that can be fixed?]

# There are two different data types (object and int64). Previously discovered that there were missing null values in the churn_date column but replaced them with NA. 

#  

# ### Fix Data

# none are needed 

# ### Enrich Data

# none are needed 

# ## Calls

# In[16]:


# Print the general/summary information about the calls' DataFrame
calls.describe()
calls.isnull().sum()
calls.info()



# In[17]:


# Print a sample of data for calls
calls.head()


# The calls dataframe has object, float, and int64 datatypes.  There are no empty cells.  There is nothing needing further investigation. 

#  

# ### Fix data

# In[18]:


#convert data type of date column
calls['call_date']=pd.to_datetime(calls['call_date'])
calls.info()
print(calls.head())


# ### Enrich data

# In[19]:


calls['duration']=calls['duration'].apply(np.ceil).astype(int)


# ## Messages

# In[20]:


# Print the general/summary information about the messages' DataFrame
messages.describe()
messages.isnull().sum()
messages.info()


# In[21]:


# Print a sample of data for messages
messages.tail()


# Messages dataframe has object and integer data types.  There are no empty cells or rows.  No further investigation needed. 

#  

# ### Fix data

# In[22]:


#convert date datatype
messages['message_date']=pd.to_datetime(messages['message_date'])
messages.info()


# ### Enrich data

# none

# ## Internet

# In[23]:


# Print the general/summary information about the internet DataFrame
internet.describe()
internet.isnull().sum()
internet.info()


# In[24]:


# Print a sample of data for the internet traffic
internet.head()


# The internet dataframe contains floats, integers, and objects.  There are no missing data rows or columns.  

#  

# ### Fix data

# In[25]:


internet['session_date'] = pd.to_datetime(internet['session_date'])
internet.info()


# ### Enrich data

# none needed 

# ## Study plan conditions

# # Print out the plan conditions and make sure they are clear for you
# Surf
# Monthly charge: $20
# 500 monthly minutes, 50 texts, and 15 GB of data
# After exceeding the package limits:
# 1 minute: 3 cents
# 1 text message: 3 cents
# 1 GB of data: $10
# 
# Ultimate
# Monthly charge: $70
# 3000 monthly minutes, 1000 text messages, and 30 GB of data
# After exceeding the package limits:
# 1 minute: 1 cent
# 1 text message: 1 cent
# 1 GB of data: $7
# 

# In[26]:


plans.columns
plans.head()


# ## Aggregate data per user
# 
# [Aggregate data per user per period in order to have just one record per user per period to ease the further analysis a lot.]

# In[27]:


# Calculate the number of calls made by each user per month. Save the result.
# Calculate the amount of minutes spent by each user per month. Save the result.
calls['month']=calls['call_date'].dt.month
calls_per_user=calls.groupby(['user_id','month']).agg({'call_date':'count', 'duration': 'sum'})
calls_per_user


# In[28]:


# Calculate the number of messages sent by each user per month. Save the result.
#convert time listing into a month listing
messages['month']=messages['message_date'].dt.month
message_per_user=messages.groupby(['user_id','month']).agg({'message_date':'count'})
message_per_user


# In[29]:


# Calculate the volume of internet traffic used by each user per month. Save the result.
#convert time listing into a month listing
internet['month']=internet['session_date'].dt.month
traffic_volume=internet.groupby(['user_id','month']).agg({'mb_used':'sum'})
traffic_volume


# [Put the aggregate data together into one DataFrame so that one record in it would represent what an unique user consumed in a given month.]

# In[30]:


# Merge the data for calls, minutes, messages, internet based on user_id and month
#double check with another method 
user_monthly_info=pd.concat([calls_per_user, message_per_user, traffic_volume], axis=1,)
user_monthly_info=user_monthly_info.fillna(0)
user_monthly_info.reset_index(inplace=True)
user_monthly_info.head()


# In[31]:


#add which type of plan users had 
user_monthly_info = user_monthly_info.merge(users, on=['user_id'], how='inner')
user_monthly_info


# In[32]:


# Add the plan information
#ensure columns match.  The common column is "plans" and "plan_name"
plans.columns
user_monthly_info.columns
user_monthly_info_cleaned = user_monthly_info.loc[:, ~user_monthly_info.columns.duplicated()]
monthly_info = user_monthly_info_cleaned.merge(plans, left_on='plan', right_on='plan_name', how='left')
monthly_info


# [Calculate the monthly revenue from each user (subtract the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan).

# In[33]:


monthly_info.info()


# In[34]:


# Calculate the monthly revenue for each user
#first calculate the overage cost for each user in messages, minute, and gb overages
monthly_info['message_cost']=((monthly_info['message_date']-monthly_info['messages_included']).clip(lower=0))*monthly_info['usd_per_message']
monthly_info['minute_cost']=((monthly_info['duration']-monthly_info['minutes_included']).clip(lower=0))*monthly_info['usd_per_minute']

#convert to be same datatype.  needs to be float to perform calculations
monthly_info['mb_per_month_included']= monthly_info['mb_per_month_included'].astype(float)
monthly_info['gb_per_month']= monthly_info['gb_per_month'].astype(float)

monthly_info['extra_gb']=(monthly_info['mb_used']-monthly_info['mb_per_month_included']).clip(lower=0)
monthly_info['monthly_gb_cost']=np.ceil(monthly_info['extra_gb']/1024)*monthly_info['usd_per_gb']
#monthly_info['gb_cost']=(np.ceil(monthly_info['mb_used']-monthly_info['mb_per_month_included']).clip(lower=0)/1024)*monthly_info['usd_per_gb']

#total monthly cost will be the plan cost+monthly minute overage+gb overage+message overage
monthly_info['monthly_revenue']=monthly_info['usd_monthly_pay']+monthly_info['minute_cost']+monthly_info['monthly_gb_cost']+monthly_info['message_cost']
monthly_info


# ## Study user behaviour

# Calculate some useful descriptive statistics for the aggregated and merged data, which typically reveal an overall picture captured by the data. 

# ### Calls

# In[35]:


# Compare average duration of calls per each plan per each distinct month. Plot a bar plat to visualize it.
#create table of information just with plan, month, and duration sum
average_duration=monthly_info.groupby(['plan','month']).agg({'duration':'mean'}).reset_index()
print(average_duration)


for plan in average_duration['plan'].unique():
    subset = average_duration[average_duration['plan'] == plan]
    plt.bar(subset['month'], subset['duration'], label=plan, alpha=0.7)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Duration (minutes)')
plt.title('Average Call Duration')
plt.legend(title='Type of Plan')
plt.tight_layout()



# In[36]:


# Compare the number of minutes users of each plan require each month. Plot a histogram.
plan_minutes = monthly_info.groupby(['plan', 'month'])['duration'].sum().reset_index()

# Plotting
plt.figure()

# Plot each plan
for plan in plan_minutes['plan'].unique():
    subset = plan_minutes[plan_minutes['plan'] == plan]
    plt.bar(subset['month'], subset['duration'], label=plan, alpha=0.7)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Call Duration (minutes)')
plt.title('Minutes Used per Plan per Month')
plt.legend(title='Plan')
plt.tight_layout()


# In[37]:


# Calculate the mean and the variance of the monthly call duration
monthly_call_stats= monthly_info.groupby(['plan', 'month'])['duration'].agg(['mean', 'var']).reset_index()
print(monthly_call_stats)


# In[38]:


surf = monthly_call_stats[monthly_call_stats['plan'] == 'surf']
ultimate = monthly_call_stats[monthly_call_stats['plan'] == 'ultimate']
print(surf.head())
print(ultimate.head())


# In[39]:


#create df of each type of plan
surf = monthly_info[monthly_info['plan'] == 'surf']
ultimate = monthly_info[monthly_info['plan'] == 'ultimate']

# Plot a boxplot to visualize the distribution of the monthly call duration
sns.boxplot(data=surf, x='month', y='duration')

plt.title('Distribution of Monthly Call of Surf Plan')
plt.xlabel('Montht')
plt.ylabel('Average Call Duration')
plt.show()




# In[40]:


#create new boxplot 
sns.boxplot(data=ultimate, x='month', y='duration')

#fig, ax = plt.subplots()
plt.title('Distribution of Monthly Call of Ultimate Plan')
plt.xlabel('Month')
plt.ylabel('Average Call Duration')
plt.show()


# Overallthe surf plan users make more calls during the year.  The calls tend to increase as the year goes on regardless of plan type chosen. 

# ### Messages

# In[41]:


# Compare the number of messages users of each plan tend to send each month
average_messages = monthly_info.groupby(['plan', 'month'])['message_date'].sum().reset_index()
print(average_messages)


# In[42]:


# Compare the amount of internet traffic consumed by users per plan
monthly_info['gb_used']=monthly_info['mb_used']/1024
average_gb_usage = monthly_info.groupby(['plan', 'month'])['gb_used'].sum().reset_index()
print(average_gb_usage)
# Plotting
plt.figure()

# Plot each plan
for plan in average_gb_usage['plan'].unique():
    subset = average_gb_usage[average_gb_usage['plan'] == plan]
    plt.bar(subset['month'], subset['gb_used'], label=plan, alpha=0.7)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('GB Used')
plt.title('Average GB Used per Plan per Month')
plt.legend(title='Plan')


# The surf plan uses more GB overall.  In January neither plan is using more than 1000 GB.  However by December surf plan customers are above 5000 GB and ultimate plan as close to 3000 GB.  In the month of December almost 2x usage of GB compared to Ultimate plan.  The usage seems closer in the beginning of the year. 

#  

# ### Internet

# Internet traffic increases as the months progress.  Stating in March the number of gB used in surf plan is double than ultimate plan. 

#  

# ## Revenue

# In[43]:


# Compare the revenue of each type of plan generate. Plot a histogram.
plan_revenue = monthly_info.groupby(['plan', 'month'])['monthly_revenue'].sum().reset_index()
print(plan_revenue)
# Plotting
plt.figure()

# Plot each plan
for plan in plan_revenue['plan'].unique():
    subset = plan_revenue[plan_revenue['plan'] == plan]
    plt.bar(subset['month'], subset['monthly_revenue'], label=plan, alpha=0.7)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Revenue generated per Plan per Month')
plt.legend(title='Plan')
plt.tight_layout()


# In[44]:


#evaluate which plan goes over their plan more 
#create a column for messages, minutes, and gb determining overages 
#calculate message overages 
monthly_info['monthly_message_usage']=(monthly_info['message_date']-monthly_info['messages_included']).clip(lower=0)
#group by plan and print to confirm that done correctly 
over_messages = monthly_info.groupby(['plan', 'month'])['monthly_message_usage'].sum().reset_index()
print(over_messages)



# In[45]:


#calculate minute overages and print some to confirm
monthly_info['monthly_minute_usage']=(monthly_info['duration']-monthly_info['minutes_included']).clip(lower=0)
over_minutes = monthly_info.groupby(['plan', 'month'])['monthly_message_usage'].sum().reset_index()
print(over_minutes.head())


# In[46]:


#calculate internet overages and print some to confirm
monthly_info['over_internet']=(monthly_info['mb_used']-monthly_info['gb_per_month']).clip(lower=0)
over_internet = monthly_info.groupby(['plan', 'month'])['extra_gb'].sum().reset_index()
print(over_internet.head())


# In[47]:


#merge together the individual overage dataframes for messages, minutes, and internet
monthly_overage=pd.concat([over_minutes, over_messages, over_internet], axis=1,)
#fill in any blank spaces with zero
monthly_overage=monthly_overage.fillna(0)
monthly_overage.reset_index(inplace=True)
monthly_overage.head()


# Ultimate users tend do not surpass their minute or message usage.  However they do sometimes surpass their gB allowances.  Surf users routinely surpass in minutes, messages, and gB (except not in January).  

# ## Test statistical hypotheses

# In[48]:


# Test the hypotheses
#H0 hypothesis is that there is no difference between the average revenue from users of the Ultimate and Surf calling plans differ 
#H1 hypothesis is that there is a difference between the average revenue from users of the Ultimate and Surf calling plans differ 

# set the critical statistical significance level at statistical acceptance
alpha = 0.05

#updated problem for using columns rather than hardcoded values. 
surf_revenue_test = plan_revenue[plan_revenue['plan'] == 'surf']
print(surf_revenue_test)
ultimate_revenue_test = plan_revenue[plan_revenue['plan'] == 'ultimate']
print(ultimate_revenue_test)
results = st.ttest_ind(surf_revenue_test['monthly_revenue'], ultimate_revenue_test['monthly_revenue'])
# test the hypothesis that the means of the two independent populations are equal

print('p-value:', results.pvalue) # your code: print the p-value you get

if results.pvalue<alpha:# your code: compare the p-value you get with the significance level):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")


# In[49]:


# Test the hypotheses
#H0= The average revenue from users in NY/NJ is the same as users from other area in the country. 
#H1=The average revenue from users in NY/NJ is different from other areas of the country. 
#create revenue data for NJ/NY
ny_nj_revenue = monthly_info[monthly_info['city'].str.contains('NY-NJ')]
ny_nj_revenue



# In[50]:


# Extract revenue data for other regions
other_regions_revenue = monthly_info[~monthly_info['city'].str.contains('NY-NJ')]
print(other_regions_revenue.head(20))


# In[51]:


alpha = 0.05
# set the critical statistical significance level at statistical acceptance

results = st.ttest_ind(ny_nj_revenue['monthly_revenue'],other_regions_revenue['monthly_revenue'],equal_var=False)
# test the hypothesis that the means of the two independent populations are equal

print('p-value:', results.pvalue) # your code: print the p-value you get

if results.pvalue<alpha:# your code: compare the p-value you get with the significance level):
    print("We reject the null hypothesis")
else:
    print("We can't reject the null hypothesis")


# ## General conclusion

# Megaline has laid out interesting options for their clients.  Their is a tiered structure to choose for payment based on how many minutes talking, messages sent, and GB of internet used.  Each provided file was checked for duplicated rows and null values.  Wherever a date was missing for ‘churn_date” because users are still current customers todays date was inserted.  Through evaluations some of the datatypes of columns were required to be changed integer or formatting style.  The minutes columns for how long users talked needed to be rounded up if it was any decimal point.  Internet usage was provided in MB but we were concerned with GB so it was divided by 1024 to be reported in GB.  
# 
# Since users made multiple entries per month an aggregated dataframe was created with each user_id listing the phone usage per month.  Each time point was adjusted to reflect only the month the task was performed in.  The monthly revenue per user was calculated by subtracting the usage values from users plan allowance.  Any overages were multiplied by plan dictated surcharges. 
# 
# Ultimately the surf plan generates more revenue for Megaline.  The plan is less expensive but users tend to use over their allotted minutes, messages, and GB of data.  This issue increases towards the end of the year.  In order to generate more money perhaps Megaline should considering lowering the usage terms (less minutes, messages, and GB).  Statistically the average revenue does not differ and NY/NJ residents do not spend more.  All of this was learned through statistical data analysis.  
# 
