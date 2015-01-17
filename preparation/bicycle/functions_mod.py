# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:06:20 2015

@author: David
"""

import re
import pysentiment as ps

hiv4 = ps.HIV4() # create pysentiment HIV4 object (slow)

def word_occurence(chapters,text_dir,target_word):
    word_occurences=[]

    for chapter in chapters:
        f=open(text_dir + str(chapter) + '.txt')
    
        text = f.readlines()
    
        for paragraph in text:
            if paragraph != '\n':
                # parse words            
                words=re.findall(r"[\w']+", paragraph)
                # convert to lowercase
                words_lower=[word.lower() for word in words]
                word_occurences.append(words_lower.count(target_word))
                

                
    return word_occurences

def word_occurence_and_sentiment(chapters,text_dir,target_word):
    word_occurences=[]
    sent_score=[]
    for chapter in chapters:
        f=open(text_dir + str(chapter) + '.txt')
    
        text = f.readlines()
    
        for paragraph in text:
            if paragraph != '\n':
                # parse words            
                words=re.findall(r"[\w']+", paragraph)
                # convert to lowercase
                words_lower=[word.lower() for word in words]
                word_occurences.append(words_lower.count(target_word))
                
                hiv4_tokens = hiv4.tokenize(paragraph)
                hiv4_score = hiv4.get_score(hiv4_tokens)
                
                sent_score.append(hiv4_score)
                
    return word_occurences,sent_score

# for each paragraph number, the function returns the paragraph number 
#def find_chapters():
    
