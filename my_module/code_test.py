#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pytest

from expense_tracker import add_expenses


# In[5]:


assert add_expenses([1, 2, 3]) == int
assert add_expenses([1, 2, 3]) == 6

