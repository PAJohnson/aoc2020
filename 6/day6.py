def parse1(inputfile):
	groups = []
	with open(inputfile,'r') as infile:
		group = []
		for row in infile:
			if row == '\n':
				groups.append(group)
				group = []
			else:
				for c in row.strip():
					if c not in group:
						group.append(c)
		groups.append(group)
	return groups

def solve1(data):
	count = 0
	for d in data:
		count = count + len(d)
	return count

def parse2(inputfile):
	groups = []
	with open(inputfile,'r') as infile:
		group = []
		for row in infile:
			if row == '\n':
				groups.append(group)
				group = []
			else:
				group.append(row.strip())
		groups.append(group)
	return groups

def solve2(infile):
	charSets = parse1(infile)
	groups = parse2(infile)

	def matchAll(char,group):
		match = True
		for g in group:
			if char not in g:
				match = False
		return match

	countTotal = 0
	for i in range(len(charSets)):
		count = 0
		for c in charSets[i]:
			if matchAll(c,groups[i]):
				count = count + 1
		countTotal = countTotal + count
	return countTotal

print(solve1(parse1('test.txt')))
print(solve1(parse1('input.txt')))

print(solve2('test.txt'))
print(solve2('input.txt'))
