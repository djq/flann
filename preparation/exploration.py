import pandas as pd
import nltk
import pysentiment as ps
import re

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

	# count words
	list = re.findall("(\S+)", paragraph)
	hiv4_score['word_count'] = len(list)

	# store sentiment + word count
	paragraph_sentiment.append(hiv4_score)

# store in csv
outfile = open('../output/data.csv', 'w')
outfile.write('paragraph,word_count,polarity,subjectivity,positive,negative\n')

# loop through results and write to csv
for idx, sentiment in enumerate(paragraph_sentiment):
	# import ipdb; ipdb.set_trace()
	csv_string = '{idx},{word_count},{polarity},{subjectivity},{positive},{negative}\n'.format(
		idx=idx,
		word_count=sentiment['word_count'],
		polarity=sentiment['Polarity'],
		subjectivity=sentiment['Subjectivity'],
		positive=sentiment['Positive'],
		negative=sentiment['Negative'])
	outfile.write(csv_string)


outfile.close()

print 'finished!'