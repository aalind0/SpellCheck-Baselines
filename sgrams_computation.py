query = "toiilet"
skips = [0, 1]


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

maxkey = 0
for line in in_file:
    values = set(line.split())
    jaccard =  float(len(values.intersection(b_query))) / float(len(values.union(b_query)))
    if jaccard > maxkey:
        maxkey = jaccard
        print line
