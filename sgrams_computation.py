skips = [0, 1]
in_file1 = open("wordlist.txt", "r+")

# Breaking words into s-grams
def sgrams(entry, skips):
	result = set()
	for skip in skips:
		for i in range(0, len(entry) - skip - 1):
			result.add(entry[i] + entry[i + skip + 1])
	if len(entry) < 2:
		result.add(entry)
	return result

#Sgram_dict is a dictionary which has format word:{s-gram}
sgram_dict = dict()
for i in in_file1:
	sgram_dict[i.rstrip()] = sgrams(i.rstrip(), skips)

def ranked_list(entry, skips):
	b_query = sgrams(query, skips) #Break query into sgrams
	sgram_sort = dict() #Sgram_dict is a dictionary which has format word:jaccard
	k = 10 #Returns top k
	#Loop in dictionary to calculate jaccards
	for word in sgram_dict:
		values = sgram_dict[word]
		jaccard =  float(len(values.intersection(b_query))) / float(len(values.union(b_query)))
		if len(sgram_sort) < k:
			sgram_sort[word] = jaccard
		if len(sgram_sort) == k:
			if sgram_sort[min(sgram_sort, key=sgram_sort.get)] < jaccard:
				del sgram_sort[min(sgram_sort, key=sgram_sort.get)]
				sgram_sort[word] = jaccard #Replace the minimum value in dictionary with higher jaccard
	return sgram_sort

misspells = open("aspell_testdata.txt", "r+")

for line in misspells:
	values = line.rstrip().split()
	answer = values[1]
	query = values[0]
	sgram_sort = ranked_list(query, skips)
	rank = 1
	final_rank = 1
	print "\nThe given query is: " + query + "\n"
	for w in sorted(sgram_sort, key=sgram_sort.get, reverse=True):
		print w, sgram_sort[w]
		if w == answer:
			final_rank = rank
		else:
			rank += 1
	print "\nThe correct answer was found at rank: " + str(final_rank) + "\n"
