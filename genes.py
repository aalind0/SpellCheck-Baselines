#Random genome sequence generator
import string
import random
random.seed(1)
size = 100
chars="atgc"

def gene_generator(size, chars):
	return ''.join(random.choice(chars) for _ in range(size))

x = gene_generator(10, chars)
print x
answer = []
answer.append(x[0])
for i in range(len(x) - 1):
	answer.append(x[i] + x[i + 1])
answer.append(x[-1])
print answer

anchor = [1, (1+len(answer)) / 2, len(answer)]
print anchor

anchor_one = []
anchor_two = []
anchor_three = []

for i in range(1, len(answer) + 1):
	anchor_one.append(abs(i - anchor[0]))
	anchor_two.append(abs(i - anchor[1]))
	anchor_three.append(abs(i - anchor[2]))

print anchor_one
print anchor_two
print anchor_three
