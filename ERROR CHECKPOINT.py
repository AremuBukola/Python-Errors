#!/usr/bin/env python
# coding: utf-8

# In[64]:


try: 
    mylist=[14, "hello", 967] 
    mylist[6] 
except: 
        print ("List index out of range")#The indexed number does not exist in the list





# In[62]:


try:
    import Pandas
    import NumPy
except:
    print("No module named Pandas")#The madule Pandas was not defined


# In[51]:


print ('python errors')# The error is the one that can be corrected and that has beeen done


# In[54]:


try: 
    mydictionnary={True:"hello",False:"bye", '3':"python"}
    mydictionnary['True']
except: 
    print('KeyError')# The error here is that the class True is not a key


# In[57]:


i = 14
while i < 78:
    print(i)# There should be an indentation after a function declaration
    i += 1


# ### STOP ITERATION

# In[61]:


try:
    it=iter([1,2,3])
    next(it)
    next(it)
    next(it)
next(it)
except: 
    print ("The set only has 3 elements")


# ### TYPE ERROR

# In[66]:


15 + 15 # This has been corrected as you can only concatenate elements in the same type


# ### VALUE ERROR

# In[68]:


try:
    int('python')
except:
    print ("you cannot convert string to integer")# This error occurs because it is impossible to convert string to integer


# ### NAME ERROR

# In[70]:


try:
    python
except:
    print ("python is not defined")# There is no variable name assisgned to python


# ### ZERO DIVISION ERROR

# In[72]:


try:
    x=19/0
except:
    print ("It is impossible to divide a number by zero")# The solution to this is inexpressible.


# In[ ]:




