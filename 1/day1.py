import itertools

def solve(numbers,length):
	for p in itertools.permutations(numbers,length):
		if sum(p) == 2020:
			ans = p[0]
			for i in range(1,length):
				ans = ans * p[i]
			return ans

test = [1721, 979, 366, 299, 675, 1456]

numbers = []

with open('input.txt','r') as infile:
	for row in infile:
		row = row.strip()
		numbers.append(int(row))

print(solve(numbers,2))
print(solve(numbers,3))

