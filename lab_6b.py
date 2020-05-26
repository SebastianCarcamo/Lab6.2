# TODO: 100 terminos mas frecuentes: haz un indice invertido y haz un sort?
from collections import Counter
import os

def reader():
    files = []
    common_words = []

    r_index = {}
    # r_index = {("word" , [1,2,4]), ()}
    for line in open("common.txt"):
        new = line.strip('\n')
        r_index[new] = set()
    print(r_index)
    for i in os.listdir("./Libros"):
        if i.endswith('.txt'):
            files.append("./Libros/" + i)
            
    for x in files:
        with open(x) as file:
            for line in file:
                for word in line.split():
                    newWord = word.strip(".,:;«»()\" \' º")
                    newWord = newWord.lower()  
                    if newWord in r_index:
                        r_index[newWord].add(x)
    file_out = open("index.txt", "w+")
    for iter in r_index: 
        file_out.write(iter + ":" + str(r_index[iter]) + '\n') 
        

def findWord(word, x):
    with open(x) as file:
        for line in file:
            for fileWord in line.split():
                newWord = fileWord.strip(".,:;«»()\" \' º")
                newWord = newWord.lower()
                if word == newWord:
                    return True

def makeCommon():
    files = []
    stopwords = []
    wordList = []
    wordcount = Counter()
    IncidenceMatrix = {}

    for i in os.listdir("./Libros"):
        if i.endswith('.txt'):
            files.append("./Libros/" + i)

    with open('stoplist.txt', encoding="latin-1") as file:
        for line in file:
            for word in line.split():
                stopwords.append(word)

    for x in files:
        with open(x) as file:
            for line in file:
                for word in line.split():
                    
                    newWord = word.strip(".,:;«»()\" \' º")
                    newWord = newWord.lower()
                    if newWord not in stopwords:
                        print(newWord)
                        wordcount.update({newWord: 1})
    words = wordcount.most_common(100)
    file_out = open("common.txt", "w+")
    for single_word in words:
        file_out.write(str(single_word[0])+'\n')
    # QUERY ("frodo", "gandalf", "anillo")


