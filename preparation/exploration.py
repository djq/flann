import pandas as pd
import nltk
import pysentiment as ps
import re

chapter_lists = [1,12] # currently cleaned chapters
hiv4 = ps.HIV4() # create pysentiment HIV4 object (slow)

# prepare CSV file for results
results = open('../output/data.csv', 'w')
results.write('chapter,paragraph,word_count,polarity,subjectivity,positive,negative\n')


def summarize_sentiment(results, paragraph_sentiment, chapter):
	"""
	Loop through paragraph sentiment values, and write to existing CSV
	"""
	# loop through results and write to csv
	for idx, sentiment in enumerate(paragraph_sentiment):
		csv_string = '{chapter},{idx},{word_count},{polarity},{subjectivity},{positive},{negative}\n'.format(
			chapter=chapter,
			idx=idx,
			word_count=sentiment['word_count'],
			polarity=sentiment['Polarity'],
			subjectivity=sentiment['Subjectivity'],
			positive=sentiment['Positive'],
			negative=sentiment['Negative'])
		results.write(csv_string)


# loop through chapters and calculate sentiment values
for chapter in chapter_lists:
	_file = '../text/{}.txt'.format(chapter)
	paragraph_sentiment = []

	with open(_file) as f:
		chapter_text = f.read()

		# split into paragraphs based on newlines
		# this assumes that the text is correctly formatted with a linebreak
		# before the start of every paragraph
		chapter_paragraphs = chapter_text.split('\n')

		# remove '' from paragraphs
		chapter_paragraphs = [para for para in chapter_paragraphs if para != '']

		for paragraph in chapter_paragraphs:

			# calculate sentiment for each paragraph
			hiv4_tokens = hiv4.tokenize(paragraph)
			hiv4_score = hiv4.get_score(hiv4_tokens)

			# count words
			list = re.findall("(\S+)", paragraph)
			hiv4_score['word_count'] = len(list)

			# store sentiment + word count
			paragraph_sentiment.append(hiv4_score)

		# write results to file for this chapter
		summarize_sentiment(results, paragraph_sentiment, str(chapter))

# import ipdb; ipdb.set_trace()

# close CSV file
results.close()

print 'finished!'