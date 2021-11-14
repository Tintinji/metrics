#!/usr/bin/env python
# coding: utf-8

# # Treatment Effects
# - Individual treatment effect (ITE)
# - Average treatment effect (ATE)
# - Average treatment effect of treated (ATT)
# - Local average treatment effect (LATE)
# - Marginal treatment effect (MTE)
# 
# ## Relationships of TEs

# First, I will make this statement:**ITE** is adorable but could never be measured. **ATE(ATT)** is the 

# In[1]:


import ipystata
from ipystata.config import config_stata  
# https://github.com/TiesdeKok/ipystata/tree/master/#setupunix
# This shows how to find the "Stata executable" in a Unix(MacOS) system
config_stata("/Applications/Stata/StataSE.app/Contents/MacOS/StataSE", force_batch=True)  


# In[2]:


get_ipython().run_cell_magic('stata', '', '\ndisplay "Hello, I am printed in Stata."  ')


# In[ ]:




