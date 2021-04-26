#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1

year_birth=[1999, 1995, 2005, 2010, 2007, 2006, 1994, 1996, 1979, 2008]
for x in range(len(year_birth)):
    year_birth[x]=2021-year_birth[x]
    year_birth.sort()
print("The ages of the customers is: " + str(year_birth))


# In[5]:


#Q2

age = [20, 24, 14, 9, 12, 13, 25, 23, 40, 11]
age_clean = age.copy()
age_clean.sort()
print(age_clean)
age_clean.pop(0)
age_clean.pop(-1)
print(age_clean)


# In[7]:


#Q3

berlin = [15, 13, 16, 18, 19, 10, 12 ]
munich = [7, 13, 15, 20, 19, 18, 10, 16]

def common_items(list1, list2):
   return list(set(list1) & set(list2)) 
combined = common_items(berlin, munich)


# In[8]:


combined


# In[12]:


#Q4

listA = [15, 13, 16, 18, 19, 10, 12]
listB = [7, 13, 15, 20, 19, 18, 10, 16]

def findCommons(listA, listB):
    result = []
    for counter in range(len(listA)):
        if (listA[counter] in listB) & (listA[counter] not in result):
            result.append(listA[counter])
    return sorted(result)
    print(result)


# In[13]:


1 + 1 


# In[14]:


#Q4

age = [15, 13, 16, 18, 19, 15, 10]

age.sort()
print(age)

dup_items = set()
uniq_items = []
for x in age:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)


# In[15]:


duplicated_ages = [15,13,16,18,19,15,10]
ages = []
for i in duplicated_ages:         
    if i not in ages:
         ages.append(i)
    elif i in ages:
        continue # --- why ? # functions, continue/break
print(ages)


# In[ ]:


#Q5

import numpy as np 
def a_is_in(a, b):
    list1 = np.array(a)
    list2 = np.array(b)
    if list1 in list2:
        return True
    else:
        return False
    return

a = [15]
b = [15, 13, 16, 18, 19, 15, 10]

_is_in = a_is_in(a,b)
print(_is_in)


# In[19]:


#Q5

import numpy as np 
def a_is_in(a, b):
    list1 = np.array(a)
    list2 = np.array(b)
    if list1 in list2:
        return True
    else:
        return False
    return

a = [28]
b = [15, 13, 16, 18, 19, 15, 10]

_is_in = a_is_in(a,b)
print(_is_in)


# In[3]:


x = [23,24,43,67]


# In[4]:


10 in x


# In[5]:


24 in x


# In[6]:


age_list = [23,24,43,67]


# In[18]:


def anyname(ages, age):
    if age in ages:
        return "anystringoranynumber"
    else:
        return "elsething"
        


# In[21]:


result = anyname(age_list, 23)


# In[22]:


result


# In[22]:


#Intermediate Level - Set 1
# Q1

inputs = [[2, 4, 0, 100, 4, 11, 2602, 36], # --- Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21], # --- Should return: 160 (the only even number)

[2, 4, 6, 8, 10, 3],] # --- Should return: 3

def outlier(array):
    in_list = list(array)
    is_even = True
    l_1 = in_list[0]%2 ==0
    l_2 = in_list[1]%2 ==0
    l_3 = in_list[2]%2 ==0
    
    if l_1:
        if l_1 and l_2:
            pass
        elif l_1 and l_3:    
            pass
        else:
            is_even = False

    elif not l_1:
        if not l_1 and not l_2:
            is_even = False
        elif not l_1 and not l_3:
            is_even = False
        else:
            pass
       
    if is_even:
        for x in in_list:
            if x % 2 != 0: return x
    else:
        for x in in_list:
            if x % 2 == 0: return x
for l in inputs:
    print(outlier(l))


# In[ ]:


1 + 1 * 2


# In[ ]:





# In[ ]:




