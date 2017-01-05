out = open("wordlist_sgrams.txt", "w+")
in_file = open("wordlist.txt", "r+")

entry = "abcd"
skips = [0, 1]

def sgrams(entry, skips):
        result = set()
        for skip in skips:
                for i in range(0, len(entry) - skip - 1):
                        result.add(entry[i] + entry[i + skip + 1])
        if len(entry) < 2:
                result.add(entry)
        return result

'''print sgrams(entry, skips)'''
for line in in_file:
        answer = sgrams(line.rstrip(), skips)
        for a in answer:
                out.write(a + ' ')
        out.write('\n')

out.close()
in_file.close()
