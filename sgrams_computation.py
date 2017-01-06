import heapq
query = raw_input("Enter here unfortunate misspelled word: ")
skips = [0, 1]

in_file1 = open("wordlist.txt", "r+")
in_file = open("wordlist_sgrams.txt", "r+")

# Breaking words into s-grams
def sgrams(entry, skips):
		result = set()
		for skip in skips:
				for i in range(0, len(entry) - skip - 1):
						result.add(entry[i] + entry[i + skip + 1])
		if len(entry) < 2:
				result.add(entry)
		return result

b_query = sgrams(query, skips)

#Sgram_dict is a dictionary which has format word:{s-gram}
sgram_dict = dict()
for i in in_file1:
	sgram_dict[i.rstrip()] = sgrams(i.rstrip(), skips)

sgram_sort = dict() #Sgram_dict is a dictionary which has format word:jaccard
k = 10
#Loop in dictionary to calculate jaccards
for word in sgram_dict:
	values = sgram_dict[word]
	jaccard =  float(len(values.intersection(b_query))) / float(len(values.union(b_query)))
	if len(sgram_sort) < k:
		sgram_sort[word] = jaccard
	if len(sgram_sort) == k:
		if sgram_sort[min(sgram_sort, key=sgram_sort.get)] < jaccard:
			del sgram_sort[min(sgram_sort, key=sgram_sort.get)]
			sgram_sort[word] = jaccard

for w in sorted(sgram_sort, key=sgram_sort.get, reverse=True):
  print w, sgram_sort[w]
