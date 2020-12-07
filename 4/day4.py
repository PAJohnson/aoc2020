def parse(inputfile):
	passports = []
	with open(inputfile,'r') as infile:
		passport = {}
		for row in infile:
			if row == '\n':
				passports.append(passport)
				passport = {}
			else:
				vals = row.split(' ')
				for val in vals:
					key = val.split(':')[0]
					value = val.split(':')[1].strip()
					passport.update({key:value})
		passports.append(passport)
	return passports

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isHex(x):
	ret = True
	for c in x:
		if c not in '0123456789abcdef':
			ret = False
	return ret

def hgtRule(x):
	ret = True
	if 'cm' in x:
		num = x[0:x.index('c')]
		if not (int(num) >= 150 and int(num) <= 193):
			ret = False
	elif 'in' in x:
		num = x[0:x.index('i')]
		if not (int(num) >= 59 and int(num) <= 76):
			ret = False
	else:
		ret = False
	return ret

rules = {
	'byr': lambda x : len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
	'iyr': lambda x : len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
	'eyr': lambda x : len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
	'hgt': lambda x : hgtRule(x),
	'hcl': lambda x : x[0] == '#' and len(x) == 7 and isHex(x[1:]),
	'ecl': lambda x : x in ['amb','blu','brn','gry','grn','hzl','oth'],
	'pid': lambda x : len(x.strip()) == 9
}

def solve1(fields, optional, passports):
	validCount = 0
	for pp in passports:
		valid = True
		for field in fields:
			if field not in pp and field != optional:
				valid = False
		if valid:
			validCount = validCount + 1
	return validCount

def solve2(fields, optional, rules, passports):
	validCount = 0
	for pp in passports:
		valid = True
		for field in fields:
			if field not in pp and field != optional:
				valid = False
		if valid:
			for rule in rules:
				# print('rule = ' + str(rule) + ' input = ' + str(pp[rule]) + ' res is ' + str(rules[rule](pp[rule])))
				if not rules[rule](pp[rule]):
					valid = False
		if valid:
			validCount = validCount + 1
	return validCount

print(solve1(fields, 'cid', parse('test.txt')))
print(solve1(fields, 'cid', parse('input.txt')))

print(solve2(fields, 'cid', rules, parse('textValid.txt')))
print(solve2(fields, 'cid', rules, parse('textInvalid.txt')))
print(solve2(fields, 'cid', rules, parse('input.txt')))
