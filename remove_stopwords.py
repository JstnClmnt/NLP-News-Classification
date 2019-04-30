#############################################################
# This python code removes tagalog stop words from the      #
# input text.												#		
#############################################################

import csv

f = open('tagalog_stop_words.csv','r')
d = f.read()
stop_words = d.split('\r\n')

result = []
sample_input = "Ako ay masaya at hindi makulit naming"

input_words = sample_input.split()

# filter_stopwords = [word for word in input_words if word.lower() not in stop_words]
filter_stopwords = filter(lambda word: word.lower() not in stop_words, input_words);
result.append(filter_stopwords)

print(result)