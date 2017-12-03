#master function
def count_of_words(filename):
	with open(filename, mode='r') as f:
		lines = [line.strip() for line in f]
	wordcount = 0
	for item in lines:
		wordcount = wordcount + len(item.split())
	print ('the numbers of words is',wordcount)