import os
from prettytable import PrettyTable

def findWord(word, x):
	with open("../Libros/" + x) as file: 
		for line in file:
			for fileWord in line.split():
				newWord = fileWord.strip(".,:;«»()\" \' º")
				newWord = newWord.lower()
				if word == newWord:
					return True


files = []
stopwords = []
wordList = set([])
IncidenceMatrix = {}

for i in os.listdir("../Libros"):
	if i.endswith('.txt'):
		files.append(i)

with open('../stoplist.txt',encoding="latin-1") as file:
	for line in file:
		for word in line.split():
			stopwords.append(word)

for x in files:
	with open("../Libros/" + x) as file:
		for line in file:
			for word in line.split():
				newWord = word.strip(".,:;«»()\" \' º")
				newWord = newWord.lower()
				if newWord not in stopwords:
					wordList.add(newWord);

for word in wordList:
	IncidenceMatrix[word] = []
	for file in files:

		if findWord(word,file):	
			IncidenceMatrix[word].append("1")
		else:
			IncidenceMatrix[word].append("0")

t = PrettyTable(["Words"]+files)
f = open("incidence.txt","w")

f.write("Lista de libros: \n")

for i in files:
	f.writelines(i + "|" )
f.writelines("\n")

for x in IncidenceMatrix:
	t.add_row([x] + IncidenceMatrix[x])
	f.writelines([x, "|"] + IncidenceMatrix[x] + ["\n"])	

print(t)