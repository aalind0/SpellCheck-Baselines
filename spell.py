import re
from collections import Counter
import timeit

spells = dict()
def words(text): return re.findall(r'\w+', text.lower())


def P(word, N=sum(spells.values())):
	"Probability of `word`."
	return spells[word] / (N + 1.0)

def correction(word):
	"Most probable spelling correction for word."
	return max(candidates(word), key=P)

def candidates(word):
	"Generate possible spelling corrections for word."
	return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
	"The subset of `words` that appear in the dictionary of WORDS."
	# return set(w for w in words if w in WORDS)
	return set(w for w in words if w in spells)

def edits1(word):
	"All edits that are one edit away from `word`."
	letters    = 'abcdefghijklmnopqrstuvwxyz'
	splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
	deletes    = [L + R[1:]               for L, R in splits if R]
	transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
	replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
	inserts    = [L + c + R               for L, R in splits for c in letters]
	return set(deletes + transposes + replaces + inserts)

def edits2(word):
	"All edits that are two edits away from `word`."
	return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Use a for loop to insert "name-freq" in a dictionary
item = open("final-int.txt", "r+")
for line in item:
	values = line.split()
	spells[values[0]] = int(values[1].rstrip())
item.close()
print spells["swastikas"]
tic = timeit.default_timer()
print correction("toliet")
tac = timeit.default_timer()
print tac-tic
