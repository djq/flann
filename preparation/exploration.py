import pandas as pd
import nltk
import pysentiment as ps

# read in text
text = open('../text/1.txt').read()

# split into paragraphs based on newlines
# this assumes that the text is correctly formatted with a linebreak
# before the start of every paragraph
paragraphs = text.split('\n')

# remove '' from paragraphs
paragraphs = [para for para in paragraphs if para != '']

paragraph_sentiment = []
hiv4 = ps.HIV4()
for paragraph in paragraphs:
	# calculate sentiment for each paragraph
	# index position is used to identify paragraph
	hiv4_tokens = hiv4.tokenize(paragraph)
	hiv4_score = hiv4.get_score(hiv4_tokens)
	hiv4_score['count'] = len(paragraph)
	paragraph_sentiment.append(hiv4_score)

# store in csv
outfile = open('../output/data.csv', 'w')
outfile.write('paragraph, count, polarity, positive, negative\n')

# loop through results and write to csv
for idx, sentiment in enumerate(paragraph_sentiment):
	# import ipdb; ipdb.set_trace()
	csv_string = '{idx},{count},{polarity},{positive},{negative}\n'.format(
		idx=idx,
		count=sentiment['count'],
		polarity=sentiment['Polarity'],
		positive=sentiment['Positive'],
		negative=sentiment['Negative'])
	outfile.write(csv_string)


outfile.close()

print 'finished!'