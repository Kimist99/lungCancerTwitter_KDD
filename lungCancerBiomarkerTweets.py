# In[1]:


import nltk
nltk.download()

import re #regexp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#input data converted from CSV to text file and create tokens
f=open('tweetsLCBiomarkers10_8.txt','r')# r = raw string,reg exp
data1=f.read()
tokens = nltk.word_tokenize(data1)
text = nltk.Text(tokens)
print(tokens)


# In[3]:


#remove punctuation from text, make lowercase
type(tokens)
text = nltk.Text(tokens)
type(text)  
words = [w.lower() for w in text if w.isalpha()]
words #file of chunk`


# In[7]:


#Count word frequency
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = words[:]
for token in words:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(30, cumulative=False)

data3 = freq
data3


#Output words and frequency
dataLC = pd.DataFrame(list(data3.items()), columns = ["Word", "Frequency"])
dataLC

#Output as text file
np.savetxt(r'C:\Users\dataLC.txt', dataLC.values, fmt='%s')
