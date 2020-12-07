
def parse(inputname):
	map = []
	with open(inputname,'r') as infile:
		for row in infile:
			map.append(row.strip())
	return map

def getCell(x,y,map):
	xrange = len(map[0])
	yrange = len(map)
	xnew = x % xrange
	return map[y][xnew]

def solve1(down, over, map):
	bottom = int(len(map) / down)
	trees = 0
	for i in range(1,bottom):
		if getCell(i*over, i*down, map) == '#':
			trees = trees + 1
	return trees

def solve2(slopes,map):
	trees = [solve1(slope[0],slope[1],map) for slope in slopes]
	res = trees[0]
	for i in range(1,len(trees)):
		res = res * trees[i]
	return res

print(solve1(1,3,parse('test.txt')))
print(solve1(1,3,parse('input.txt')))

slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)]

print(solve2(slopes,parse('test.txt')))
print(solve2(slopes,parse('input.txt')))
