#!/usr/bin/env python
# coding: utf-8

# In[1]:




### list and default functions

lst = ["ankita", 28, 10, 1998]


# In[2]:


lst[3]


# In[3]:


lst1 = ["ankita's","dob", "is", [28, 10, 1998]]


# In[4]:


lst1[3][0]


# In[6]:


lst1


# In[8]:


lst1.append("khinvasara")


# In[9]:


lst1


# In[10]:


lst1.index("ankita's")


# In[13]:


lst1[-1] #to print from last


# In[14]:


lst1[2:5] #to print from 2nd to 5th postion


# In[15]:


lst1.insert(5,"student")


# In[16]:


lst1


# In[17]:


lst1.remove("student")


# In[20]:


lst1


# In[19]:


lst1.pop()


# In[21]:


lst1


# In[22]:


lst2 = lst1.copy()


# In[23]:


lst2


# In[26]:


dict = {"name" : "ankita",
       "age" : 21,
       "qual" : "mcs"}


# In[27]:


dict


# In[28]:


print(dict["name"])


# In[29]:


del dict["name"]


# In[30]:


dict


# In[33]:


dict["school"] = "chs"


# In[34]:


dict


# In[35]:


# set default functions 

set = {"ankita", "umesh", "khinvasara"}


# In[36]:


set


# In[37]:


set.add("student")


# In[38]:


set


# In[39]:


len(set)


# In[40]:



# tuple and default functions

tuple = ("student", "in", "pune")


# In[41]:


tuple


# In[42]:


tuple[2]


# In[43]:


tuple[-1]


# In[44]:


tuple[0:1]


# In[45]:


tuple[0:2]


# In[46]:


a = "ankita"


# In[47]:


a[2]


# In[48]:


a.upper()


# In[49]:


a.lower()


# In[50]:


a.replace("a", "t")


# In[52]:


b = "ankita khinvasara"


# In[53]:


b.split(",")


# In[ ]:




