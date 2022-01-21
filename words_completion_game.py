#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from random_word import RandomWords
from IPython.display import clear_output
import time

words = RandomWords()
lst = words.get_random_words()
    
for i in range(1,len(lst)):
    try:
        g = random.randint(3,6)
        if len(lst[i])<=g:
            continue
        else:
            print(lst[i])
            time.sleep(2)
            clear_output(wait=True)
        
        a = lst[i][:g]

        tot = len(lst[i]) - len(a)

        print(a,end="")

        for x in range(tot):


            print("_",end=" ")
            time.sleep(1)
        try:
            xyz = input("\nComplete the word or type quit to quit the program: ")
        except BaseException as owo1:
            print(owo1)
            time.sleep(2)
        if xyz.lower() == "quit":
            break
        if xyz.lower() == lst[i].lower():
            print("SUCCESFUL!!")
            time.sleep(2)
        
        else:
            print("UNSUCCESFUL!! The word was: ",lst[i])
            time.sleep(2)
        
    except BaseException as owo:
        print(owo)
        time.sleep(2)
    clear_output(wait=True)


# In[5]:





# In[ ]:




