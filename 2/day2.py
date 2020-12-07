
test = []

def parse(inputfile):
	data = []
	with open(inputfile,'r') as inf:
		for row in inf:
			row = row.split(' ')
			min = int(row[0].split('-')[0])
			max = int(row[0].split('-')[1])
			letter = row[1].strip(':')
			pw = row[2].strip()
			data.append({'min': min, 'max': max, 'letter': letter, 'pw': pw})
	return data

def solve1(data):
	valid = 0
	for password in data:
		count = 0
		for letter in password['pw']:
			if letter == password['letter']:
				count = count + 1
		if count >= password['min'] and count <= password['max']:
			valid = valid + 1

	return valid

def solve2(data):
	valid = 0
	for password in data:
		v = 0
		if password['pw'][password['min']-1] == password['letter'] and password['pw'][password['max']-1] != password['letter']:
			v = v + 1
		if password['pw'][password['min']-1] != password['letter'] and password['pw'][password['max']-1] == password['letter']:
			v = v + 1
		if v == 1:
			valid = valid + 1
	return valid

print(solve1(parse('test.txt')))
print(solve1(parse('input.txt')))

print(solve2(parse('test.txt')))
print(solve2(parse('input.txt')))
