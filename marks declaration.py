#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pywhatkit as what
import smtplib 


# In[4]:


df = pd.read_csv("sml.csv")


# In[5]:


df


# In[6]:


name=df["Name"]
subject=df["subject"]
marks=df["marks"]
phone=df["phone"].values.tolist()
mail=df["mail"]


# In[7]:


for i in range(len(name)):
    message=""" Hi {} , your examination sheets of {} have been checked. 
    You have scored {} marks.""". format(name[i],subject[i],marks[i])
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("17jacker@gmail.com", "plveoholvpwnutwg")
    s.sendmail("17jacker@gmail.com", mail[i], message)
    s.quit()


# In[ ]:


for i in range(len(name)):
    message=""" Hi {} , your examination sheets of {} have been checked. 
    You have scored {} marks.""". format(name[i],subject[i],marks[i])
    num="+91" + str(phone[i])
    #print(num)
    what.sendwhatmsg_instantly(num, message,15, True, 2)


# In[ ]:





# In[ ]:








