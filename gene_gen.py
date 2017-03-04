#Random genome sequence generator
import string
import random
random.seed(1)
size = 100
chars="atcg"

def gene_generator(size, chars):
	return ''.join(random.choice(chars) for _ in range(size))

def mutation(query, levels):
	mutation_pos_list = random.sample(xrange(0, size - 1), (levels * (levels + 1) / 2))
	mutated_strings = []
	count = 0
	for mutate in range(1, levels + 1):
		mutated_string = query
		for iterate in range(mutate):
			index = mutation_pos_list[count]
			choices = chars.replace(mutated_string[index], "")
			mutated_string = mutated_string[:index] + random.choice(choices) + mutated_string[index + 1:]
			count += 1
		mutated_strings.append(mutated_string)
	return mutated_strings

queries = open("queries.txt", "w+") # Simulated query list
data = open("data.txt", "w+") # This will contain the mutations and noise
qrels = open("qrels.txt", "w+") # Relevance based answers
globalcount = 0
for linecount in range(1000):
	query = gene_generator(size, chars) # Simulate a query string
	queries.write(query + "\n") # Write that into the query file
	strings = mutation(query, 10) # Create 10 mutations for that query
	for querycount in range(10):
		data.write(strings[querycount] + "\n") # Loop to your mutations and add the mutations in your file
		qrels.write(str(linecount) + " " + str(globalcount) + " " + str(10 - querycount) + "\n") # Write in this format : queryno datano levelno
		globalcount += 1
for noise in range(90000): #Add noise
	data.write(gene_generator(size, chars) + "\n")
