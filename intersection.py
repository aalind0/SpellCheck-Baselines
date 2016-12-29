# This program is for intersection of wordlist and frequency list

int2 = open("freq.txt", "r+")
out = open("final-int.txt", "w+")
for line in int2:
	values = line.split()
	key = values[0].lower()
	int1 = open("wordlist.txt", "r+")
	for search in int1:
		if search.rstrip() == key:
			out.write(search.rstrip() + "\t" + values[1] + "\n")
			break
	int1.close()

out.close()
int2.close()
