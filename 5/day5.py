def parse(inputfile):
	data = []
	with open(inputfile, 'r') as infile:
		for row in infile:
			data.append(row.strip())
	return data

def rowCol(boardpass):
	row = 0
	col = 0
	rowChars = boardpass[0:7].replace('F','0')
	rowChars = rowChars.replace('B','1')
	row = int(rowChars,2)
	colChars = boardpass[7:10].replace('L','0')
	colChars = colChars.replace('R','1')
	col = int(colChars,2)
	return (row,col)

def seatId(rowcol):
	return rowcol[0]*8 + rowcol[1]

def solve1(data):
	id = 0
	for boardpass in data:
		if seatId(rowCol(boardpass)) > id:
			id = seatId(rowCol(boardpass))

	return id

def solve2(data):
	seats = [False for i in range(8*128)]
	for d in data:
		seats[seatId(rowCol(d))] = True
	for i in range(len(seats)):
		if seats[i] == False:
			print(i)

#messy!

print(solve1(parse('input.txt')))
solve2(parse('input.txt'))
