#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  pandas  as  pd


# In[2]:


# now loading  data  from  url or local  hard disk 
data=pd.read_csv('http://13.234.66.67/summer19/datasets/customer.csv')


# In[7]:


#  checking  rows  and  columns 
data.info()


# In[5]:


#   printing  top  5  rows  only 
data.head(3)


# In[9]:


#data   #  printing  all data 


# In[13]:


#  any particular column 
#data['Age']


# In[16]:


#  finding  minimum number
data['Age'].min()
data['Age'].mean()


# In[17]:


data.head()


# In[25]:


#  range of  columns 
data.iloc[0:,[1,3]]


# In[27]:


#  all description
type(data)


# In[28]:


#  now  importing  data visualization  library

import seaborn  as  sb


# In[29]:


#  count and plot  age column 
sb.countplot(data['Age'])


# In[30]:


#  ploting  all the  columns 
data.hist()


# In[31]:


#  lets go back to our  bachpan 
import  matplotlib.pyplot   as  plt


# In[52]:


runs=[5,12,9]   #  this is in KM
balls=[2,5,7]  #   this is time take  by us in Hour 
run1=[5,12,9]   #  this is in KM
ball1=[1,8,5]  #   this is time take  by us in Hour 
#  above  data  is  for  dhoni only 


# In[54]:


# designing x  axis
plt.xlabel("distance")
plt.ylabel("Time")
'''
plt.scatter(distance,time,label="RAJESH performance")  #  for rajesh 
plt.scatter(distance1,time1,label="Ramesh Performance")  #  for ramesh
plt.plot(distance,time)
plt.plot(distance1,time1)
'''
plt.bar(runs,balls,label="virat Khohli")
plt.bar(run1,ball1,label="MS dhoni")
plt.grid(color='green')
plt.legend()   #  to show lable 
plt.show()  #  showing  graph


# In[59]:


#  age and gender 
#data['Age']
#data['Genre']
plt.xlabel('gender')
plt.ylabel('Age')
plt.bar(data['Genre'],data['Age'])
plt.grid(color='green')
plt.show()


# In[ ]:




