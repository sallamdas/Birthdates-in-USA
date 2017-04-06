
# coding: utf-8

# In[4]:

f=open('births.csv','r').read()
f.split('\n')
# for item in f:
#     item.split('\n')
#     print(item)


# In[3]:

print(f)


# In[5]:


header_rows=f[1:len(f)]
print(header_rows)


# In[18]:

day_of_week={}
birth_count=[]
births=[]
for item in header_rows:
    item.split(',')
    dayofweek=item[3]
    birth_count=item[4]
    if(dayofweek in day_of_week):
        births.append(birth_count)
    


# In[6]:

f = open("births.csv", 'r')
text = f.read()
print(text)


# In[7]:


lines_list = text.split("\n")
lines_list


# In[10]:

data_no_header = lines_list[1:len(lines_list)]
days_counts = dict()

for line in data_no_header:
    split_line = line.split(",")
    day_of_week = split_line[3]
    num_births = int(split_line[4])

    if day_of_week in days_counts:
        days_counts[day_of_week] = days_counts[day_of_week] + num_births
    else:
        days_counts[day_of_week] = num_births

days_counts


# In[ ]:



