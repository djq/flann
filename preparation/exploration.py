import pandas as pd
import nltk
import pysentiment as ps

# read in text


text = open('../text/1.txt').read()

# split into paragraphs based on newlines
# this assumes that the text is correctly formatted with a linebreak
# before the start of every paragraph
paragraphs = text.split('\n')

paragraph_sentiment = []
hiv4 = ps.HIV4()
for paragraph in paragraphs:
#    print paragraph
#	# calculate sentiment for each paragraph
#	# index position is used to identify paragraph	
   
   hiv4_tokens = hiv4.tokenize(paragraph)
   hiv4_score = hiv4.get_score(hiv4_tokens)
   paragraph_sentiment.append(hiv4_score)

# store in csv
outfile = open('../output/data.csv', 'w')
outfile.write('paragraph, polarity\n')

# loop through results and write to csv
for idx, sentiment in enumerate(paragraph_sentiment):
	# import ipdb; ipdb.set_trace()
	csv_string = '{idx}, {polarity}\n'.format(idx=idx, polarity=sentiment['Polarity'])
	outfile.write(csv_string)


outfile.close()




print 'finished!'