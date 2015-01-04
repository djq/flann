import pandas as pd
import nltk
import pysentiment as ps
import re

chapter_lists = [1, 2, 3, 4, 5, 9, 10, 11, 12] # currently cleaned chapters
# 6, 7, 8
# footnotes for 9 need to be checked
# chapter_lists = range(1,13) # testing

hiv4 = ps.HIV4() # create pysentiment HIV4 object (slow)

# prepare CSV file for results
results = open('../output/data.csv', 'w')
results.write('chapter,paragraph,word_count,no_count,yes_count,polarity,subjectivity,positive,negative\n')


def summarize_sentiment(results, paragraph_sentiment, chapter):
	"""
	Loop through paragraph sentiment values, and write to existing CSV
	"""
	# loop through results and write to csv
	for idx, sentiment in enumerate(paragraph_sentiment):
		csv_string = '{chapter},{idx},{word_count},{no_count},{yes_count},{polarity},{subjectivity},{positive},{negative}\n'.format(
			chapter=chapter,
			idx=idx,
			word_count=sentiment['word_count'],
			no_count=sentiment['no_count'],
			yes_count=sentiment['yes_count'],
			polarity=sentiment['Polarity'],
			subjectivity=sentiment['Subjectivity'],
			positive=sentiment['Positive'],
			negative=sentiment['Negative'])
		results.write(csv_string)


# loop through chapters and calculate sentiment values
for chapter in chapter_lists:

	# construct file path
	chapter_file = '../text/{}.txt'.format(chapter)
	paragraph_sentiment = []

	# read chapter
	with open(chapter_file) as f:
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

			# count total words
			word_list = re.findall("(\S+)", paragraph)
			hiv4_score['word_count'] = len(word_list)

			# count certain words
			no_list = re.findall("no", paragraph.lower())
			hiv4_score['no_count'] = len(no_list)

			yes_list = re.findall("yes", paragraph.lower())
			hiv4_score['yes_count'] = len(yes_list)

			# store sentiment and word counts in an array
			paragraph_sentiment.append(hiv4_score)

		# write results to file for this chapter
		summarize_sentiment(results, paragraph_sentiment, str(chapter))

# import ipdb; ipdb.set_trace()

# close CSV file
results.close()

print 'finished!'