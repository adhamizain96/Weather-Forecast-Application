#!/usr/bin/env python
# coding: utf-8

# In[7]:


#requests - allows you to send HTTP/1.1 requests 
import requests as r
city = input('What city do you want to check the weather forecast for?: ')
url = 'https://wttr.in/{}'.format(city)
#.get() - returns the value of the item with the specified key
city_report = r.get(url)
print(city_report.text)


# In[ ]:




