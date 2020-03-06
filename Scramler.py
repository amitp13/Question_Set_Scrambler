#!/usr/bin/env python
# coding: utf-8

# In[78]:


from docx import Document
import random
import itertools


# In[79]:


doc = Document("SetA_answerkey.docx")
set = []
for para in doc.paragraphs: 
     set.append(para.text)


# In[80]:


starts = [n for n, l in enumerate(set) if l.startswith('1)')]
set_cl = set[starts[0]:]


# In[81]:


ans = []     # for all the answers
ques = []    # for all the question
ch = []      #for all options
for idx, val in enumerate(set_cl):
    if(val.startswith("Answer:") == True):
        ans.append(val)
    elif(val.startswith(("A)","B)","C)","D)","E)"))== True):
        ch.append(val)
    else:
        ques.append(val)


# In[82]:


#cleaning up the questions set by removing blanks 
ques_1 = [i for i in ques if i != ""]


# In[83]:


#Creating option into sets
from itertools import islice 
split_lst = []
for idx, val in enumerate(ch):
    if("True" in ch[idx]):
        split_lst.append(2)
    elif("True" not in ch[idx] and val.startswith("A)")):
         split_lst.append(5)
temp = iter(ch) 
ch_set = [list(islice(temp, 0, ele)) for ele in split_lst]


# In[84]:


print(ques_1[-1])
print(ch_set[-1])
print(ans[-1])

#combining our list back
qa = list(zip(ques_1,ch_set,ans))
qa = list(itertools.zip_longest(ques_1,ch_set,ans))


# In[85]:


new_qa = random.shuffle(qa)


# In[86]:


#formatting our output

for i in range(len(qa)):
    print(qa[i][0])
    if("True" in qa[i][1][0]):
        print(qa[i][1][0])
        print(qa[i][1][1])
    else:
        print(qa[i][1][0])
        print(qa[i][1][1])
        print(qa[i][1][2])
        print(qa[i][1][3])
        print(qa[i][1][4])
    print(qa[i][2])

