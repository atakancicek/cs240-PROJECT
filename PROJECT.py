
# coding: utf-8

# In[1]:

import pandas as pd
import csv


# In[2]:

output = open("AllstarFull.csv", "rb")
data = pd.read_csv("AllstarFull.csv")


# In[3]:

data


# In[ ]:

#playerID : Player ID code 
#yearID : Year
#gameNum : Game number (zero if only one All-Star game played that season)
#gameID : Retrosheet ID for the game idea
#TeamID : Team name
#lgID : League Name
#GP : Games played (1.0 if played in the game)
#startingPos : If the player was started, its position


# In[4]:

years = data['yearID']


# In[5]:

years


# In[6]:

leagues = data['lgID']


# In[7]:

leagues


# In[8]:

data.sort_values(by='GP')


# In[9]:

pd.value_counts(data['GP'].values, sort=False)


# In[10]:

#There are 3990 players that played in the all-star game, and there are 1139 players that didn't played in the all-star game


# In[11]:

#Since we have different type of leagues(AL, NL), now i have to specify how many players played in AL league, and how many
#played in NL league.


# In[12]:

#getting every data about AL league


# In[13]:

al = data[data.lgID == 'AL']


# In[14]:

al


# In[15]:

#now, getting the data about NL league


# In[16]:

nl = data[data.lgID == 'NL']


# In[17]:

nl


# In[18]:

#now i will create 2 lists, in order to calculate the players whether they played in AL league.


# In[19]:

al_played = []
al_notplayed = []


# In[21]:

for i in al.GP:
    if i == 1.0:
        al_played.append(i)
    if i == 0.0:
        al_notplayed.append(i)


# In[22]:

#now, this procedure helped me to calculate the amount of players whether they played or not in the all star game


# In[23]:

#so basically if i just say print len(list), it will give me the amount of players


# In[24]:

#but before this, i also will make the same procedure for NL league players.


# In[25]:

nl_played = []
nl_notplayed = []


# In[26]:

for i in nl.GP:
    if i == 1.0:
        nl_played.append(i)
    if i == 0.0:
        nl_notplayed.append(i)


# In[27]:

#Number of players that played in AL league all-star game:


# In[28]:

print len(al_played)


# In[29]:

#Number of player that not played in AL league all-star game:


# In[30]:

print len(al_notplayed)


# In[31]:

#Number of players that played in NL league all-star game:


# In[32]:

print len(nl_played)


# In[33]:

#Number of players that not played in NL league all-star game:


# In[34]:

print len(nl_notplayed)


# In[35]:

import thinkstats2
import thinkplot


# In[36]:

#in order to make the histogram, i must assign total number of players into a variable


# In[39]:

alPlayed = len(al_played)
alNotPlayed = len(al_notplayed)
nlPlayed = len(nl_played)
nlNotPlayed = len(nl_notplayed)


# In[40]:

from __future__ import print_function, division

get_ipython().magic(u'matplotlib inline')

import thinkstats2
import thinkplot


# In[41]:

#now its time to draw the histogram


# In[43]:

#total players played in all star game:
totalPlayed = alPlayed + nlPlayed

#total dnp players in all star game:
totalDNP = nlNotPlayed + alNotPlayed


# In[45]:

#total played:
print (totalPlayed)

#total notplayed:
print (totalDNP)


# In[46]:

hist = thinkstats2.Hist({1.0:totalPlayed, 0.0:totalDNP}, label='All-star game')


# In[48]:

thinkplot.Hist(hist)
thinkplot.Config(xlabel='All-star game played', ylabel='Total amount of players')


# In[49]:

#This i my histogram, as you can see total played players are way much more than those who didn't played in both leagues
#all star game.


# In[50]:

#now back into my question, which league has more players played in its own allstar game.


# In[55]:

hist = thinkstats2.Hist({'AL League':alPlayed, 'NL League': nlPlayed}, label='All-star game')


# In[56]:

thinkplot.Hist(hist)
thinkplot.Config(ylabel='Total amount of players')


# In[57]:

#As we can see from the graph, NL league has slightly more players that played in the all-star game.


# In[58]:

pmf1 = thinkstats2.Pmf({'AL League': alPlayed, 'NL League':nlPlayed} , label='All-star game')


# In[59]:

thinkplot.Hist(pmf1)
thinkplot.Config(ylabel='Pmf')


# In[60]:

#This is PMF, and now, here is CDF


# In[73]:

first_cdf = thinkstats2.Cdf('AL'= alPlayed, label='AL League')
other_cdf = thinkstats2.Cdf('NL'= nlPlayed, label='NL League')


# In[74]:

thinkplot.PrePlot(2)
thinkplot.Cdfs([first_cdf, other_cdf])
thinkplot.Config(ylabel='CDF')


# In[75]:

cdf = thinkstats2.Cdf({'AL League': alPlayed, 'NL League': nlPlayed}, label='All-star games')
thinkplot.Cdf(cdf)
thinkplot.Config(ylabel='CDF', loc='upper left')


# In[76]:




# In[ ]:



