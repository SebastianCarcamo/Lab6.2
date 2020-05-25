def readBooks(lines):
	books = lines[1].split('|')
	return books

def findWordIncidence(word, lines):
	newWord = word.lower()
	for i in range(2,len(lines)):
			if lines[i].split('|')[0] == newWord:
				return lines[i].split('|')[1]

def operate_and(x,y):
	result = []
	for i in range(len(x)):
		result.append(x[i]&y[i])
	return result

def operate_or(x,y):
	result = []
	for i in range(len(x)):
		result.append(x[i]|y[i])
	return result

def operate_neg(x):
	result = []
	for i in range(len(x)):
		if(x[i] == 0):
			result.append(1)
		else:
			result.append(0)
	return result

def transform(x):
	result = []
	for i in range(len(x)-1):
		result.append(int(x[i]))
	return result

def locate_book(list,lines):
	books = readBooks(lines)

	for i in range(len(list)):
		if list[i] == 1:
			print(books[i] + "|", end = "")
	print()

f = open("incidence.txt")
lines = f.readlines()
x = transform(findWordIncidence("Comienza",lines))
y = transform(findWordIncidence("noticia",lines))

frodo = transform(findWordIncidence("Frodo",lines))
gandalf = transform(findWordIncidence("Gandalf",lines))
sam = transform(findWordIncidence("Sam",lines))
denethor = transform(findWordIncidence("denethor",lines))
Lothlorien = transform(findWordIncidence("Lothlórien",lines))
elfo = transform(findWordIncidence("Elfo",lines))
elfos = transform(findWordIncidence("Elfos",lines))
legolas = transform(findWordIncidence("Legolas",lines))


locate_book(operate_and(operate_and(frodo,gandalf),operate_neg(sam)),lines)
locate_book(operate_or(denethor,Lothlorien),lines)
locate_book(operate_and(operate_and(operate_neg(elfo),operate_neg(elfos)),operate_neg(legolas)),lines)