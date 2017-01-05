entry = "abcd"
skips = [1, 2]

def sgrams(entry, skips):
	result = set()
	for skip in skips:
		for i in range(0, len(entry) - skip - 1):
			result.add(entry[i] + entry[i + skip + 1])
	return result

print sgrams(entry, skips)
