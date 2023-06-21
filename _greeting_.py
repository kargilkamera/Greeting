#!/usr/bin/env python
# coding: utf-8

# # This is just a basic project on greeting someone by taking there name as input

# In[21]:


import time

name = input('enter your name')
name = name.upper()
current_time = time.localtime()
current_time =int(time.strftime('%H',current_time))
quote = ('The way to develop self-confidence is to do the thing you fear and get a record of successful experiences behind you.')

if current_time <= 12:
    print('Good Morning',name)
elif current_time>12 and current_time <16:
    print('Good Afternoon',name)
elif current_time>16 and current_time < 19:
    print('Good Evening',name)
else:
    print('Good Night',name)
print(name,',','this is for you:-',  quote)    


# In[ ]:





# In[ ]:




