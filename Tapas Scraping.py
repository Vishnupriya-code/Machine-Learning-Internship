#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
import requests
import urllib.request
from PIL import Image
import io
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By


# In[3]:


url = 'https://forums.tapas.io/c/announcements'
driver = webdriver.Chrome()
driver.get(url)


# In[95]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text
    


# In[91]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Announcements")

pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.DataFrame(D)


# In[85]:


df.to_csv('tapas_announcements.csv')


# In[102]:


df.head(130)


# In[111]:


url = 'https://forums.tapas.io/c/events-challenges'
driver = webdriver.Chrome()
driver.get(url)


# In[120]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views heatmap-low')]")
for num in view_elements:
    views = num.text


# In[121]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Events|Challenges")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[119]:


df.head(130)


# In[122]:


df.to_csv('tapas_eventschallenges.csv')


# In[123]:


url = 'https://forums.tapas.io/c/Off-Topic'
driver = webdriver.Chrome()
driver.get(url)


# In[133]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views heatmap-high')]")
for num in view_elements:
    views = num.text


# In[136]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Off-Topic")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[137]:


df.head(50)


# In[138]:


df.to_csv('tapas_offtopic.csv')


# In[139]:


url = 'https://forums.tapas.io/c/art-comics'
driver = webdriver.Chrome()
driver.get(url)


# In[144]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[147]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Art|Comics")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[155]:


df.head(200)


# In[154]:


df.to_csv('tapas_artcomics.csv')


# In[156]:


url = 'https://forums.tapas.io/c/writing-novels'
driver = webdriver.Chrome()
driver.get(url)


# In[157]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[158]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Writing|Novels")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[161]:


df.head(100)


# In[162]:


df.to_csv('tapas_writingnovels.csv')


# In[163]:


url = 'https://forums.tapas.io/c/reviews-feedback'
driver = webdriver.Chrome()
driver.get(url)


# In[165]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[166]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Reviews|Feedbacks")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[168]:


df.head(50)


# In[169]:


df.to_csv('tapas_reviewfeedbacks.csv')


# In[170]:


url = 'https://forums.tapas.io/c/collaborations'
driver = webdriver.Chrome()
driver.get(url)


# In[171]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views heatmap-med')]")
for num in view_elements:
    views = num.text


# In[172]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Collaborations")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[174]:


df.head(100)


# In[175]:


df.to_csv('tapas_collaborations.csv')


# In[176]:


url = 'https://forums.tapas.io/c/questions'
driver = webdriver.Chrome()
driver.get(url)


# In[177]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[178]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Questions")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[180]:


df.head(100)


# In[181]:


df.to_csv('tapas_questions.csv')


# In[182]:


url = 'https://forums.tapas.io/c/answered'
driver = webdriver.Chrome()
driver.get(url)


# In[183]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[184]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Answered")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[185]:


df.head()


# In[186]:


df.to_csv('tapas_answered.csv')


# In[187]:


url = 'https://forums.tapas.io/c/tech-support-site-feedback'
driver = webdriver.Chrome()
driver.get(url)


# In[188]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views')]")
for num in view_elements:
    views = num.text


# In[189]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Tech Support")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[191]:


df.head(50)


# In[192]:


df.to_csv('tapas_techsupport.csv')


# In[193]:


url = 'https://forums.tapas.io/c/promotions'
driver = webdriver.Chrome()
driver.get(url)


# In[201]:


element = driver.find_elements(By.XPATH,"//td[contains(@class,'main-link clearfix')]")
for value in element:
    title = value.text
    
reply_elements = driver.find_elements(By.XPATH,"//span[contains(@class,'number')]")
for reply in reply_elements:
    replies = reply.text

view_elements = driver.find_elements(By.XPATH,"//td[contains(@class,'num views heatmap-high')]")
for num in view_elements:
        views = num.text


# In[204]:


import pandas as pd

D = {'titles': [], 'replies': [], 'views': [],'category': []}

for value,reply,num in zip(element,reply_elements, view_elements):
    D['titles'].append(value.text.strip())
    D['replies'].append(reply.text.strip())
    D['views'].append(num.text.strip())
    D['category'].append("Promotions")

df = pd.DataFrame(D)
pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[205]:


df.head(100)


# In[206]:


df.to_csv('tapas_promotions.csv')

