# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 21:06:44 2015

@author: David
"""

# plots the number of 'bicycle' occurrences per paragraph, and examines any links with 
# sentiment polarity.


from matplotlib import pyplot as plt 
import numpy as np

import functions_mod as fmod
fmod=reload(fmod)


text_dir = './../../text/';

chapters = range(1,12);

# for each paragraph, obtain occurences of word bicycle and perform sentiment analysis
bicycle_occurences,sent_score=fmod.word_occurence_and_sentiment(chapters,text_dir,'bicycle')

# obtain polarity values from sentiment score
polarity = [sent_score[n]['Polarity'] for n in range(len(sent_score))]

# paragraphs where 'bicycle' occurs
bicycle_index = [ix for ix in range(len(bicycle_occurences)) if bicycle_occurences[ix]>0]

# polarity values in paragraphs where 'bicycle' occurs
bicycle_polarity = [polarity[ix] for ix in bicycle_index]


# plot of 'number of bicycle occurences'
fig1 = plt.figure(1)
plt.clf()
plt.plot(bicycle_occurences)
plt.xlabel('Paragraph')
plt.ylabel('Number of bicycle occurences')
plt.show()

# errorbar plot
# is there a shift in polarity for paragraphs containing 'bicycle'?
fig2 = plt.figure(2)
plt.clf()
plt.errorbar(1,np.mean(polarity),np.std(polarity))
plt.errorbar(2,np.mean(bicycle_polarity),np.std(bicycle_polarity))
plt.xlim(0.5,2.5)
plt.show()
# not really...

fig3 = plt.figure(3)
plt.clf()
plt.plot(polarity)
plt.plot(bicycle_index,bicycle_polarity,'o')
plt.xlabel('Paragraph')
plt.ylabel('Polarity')
plt.show()






            

    
