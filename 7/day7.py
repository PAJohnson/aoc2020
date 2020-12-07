import time
def parse(inputfile):
	rules = {}
	with open(inputfile,'r') as infile:
		for row in infile:
			row = row.strip('.\n')
			lhs = row.split(' contain ')[0]
			lhs = lhs.split(' bags')[0]
			rhs = row.split(' contain ')[1]
			lcolor = lhs.split(' bags')[0]
			contains = {}
			if "no other bags" in rhs:
				rules.update({lhs: contains})
			else:
				count = rhs.count(',')
				if count == 0:
					rhs = rhs.split(' bag')[0]
					qty = int(rhs.split(' ')[0])
					type = ' '.join(rhs.split(' ')[1:])
					rules.update({lhs: {type:qty}})
				else:
					children = rhs.split(', ')
					for child in children:
						r = child.split(' bag')[0]
						qty = int(child.split(' ')[0])
						type = ' '.join(r.split(' ')[1:])
						contains.update({type:qty})
					rules.update({lhs: contains})
	return rules


def solve1(rules,type):
	validBags = []
	candidates = []
	for rule,contents in rules.items():
		if type in contents:
			validBags.append(rule)
			candidates.append(rule)

	while len(candidates) != 0:
		newCandidates = []
		for candidate in candidates:
			for rule,contents in rules.items():
				if candidate in contents:
					if rule not in validBags:
						validBags.append(rule)
					newCandidates.append(rule)
		candidates = newCandidates

	return validBags

def solve2(rules,type):
	bags = 1
	candidates = rules[type]
	while len(candidates) != 0:
		for c,v in candidates:
			pass

print(len(solve1(parse('test.txt'),'shiny gold')))
print(len(solve1(parse('input.txt'),'shiny gold')))
