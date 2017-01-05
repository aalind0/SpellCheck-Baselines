query = "toiilet"
skips = [0, 1]

in_file1 = open("wordlist.txt", "r+")

def sgrams(entry, skips):
        result = set()
        for skip in skips:
                for i in range(0, len(entry) - skip - 1):
                        result.add(entry[i] + entry[i + skip + 1])
        if len(entry) < 2:
                result.add(entry)
        return result

b_query = sgrams(query, skips)

in_file = open("wordlist_sgrams.txt", "r+")

sgram_dict = dict()

for i in in_file1:
    sgram_dict[i.rstrip()] = sgrams(i.rstrip(), skips)
    #sgram_dict = {i : sgrams(i.rstrip(), skips)}
    
print sgram_dict['toilet']

maxkey = 0

for line in in_file:
    values = set(line.split())
    jaccard =  float(len(values.intersection(b_query))) / float(len(values.union(b_query)))
    if jaccard > maxkey:
        maxkey = jaccard
        print line
