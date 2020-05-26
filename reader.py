import os
def bool_find(word, my_map):
    if word in my_map:
        return True
    return False
def and_recovery_map(list1,list2):
    return_list = []
    for x in list1:
        if x in list2:
            return_list.append(x)
    return return_list
def or_recovery_map(list1,list2):
    return_list = []
    for x in list1:
        return_list.append(x)
    for x in list2:
        if x not in return_list:
            return_list.append(x)
    return return_list

def not_in(word, files, my_map):
    to_return = []
    for x in files:
        
        if x not in my_map[word]:
            to_return.append(x)
    return to_return

counter = 0
files = []
common_words = []

r_index = {}
# r_index = {("word" , [1,2,4]), ()}
for line in open("common.txt"):
    new = line.strip('\n')
    r_index[new] = set()
#print(r_index)
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

#frodo gandalf anillo
print( or_recovery_map(and_recovery_map(r_index["frodo"], r_index["gandalf"]), r_index["anillo"]))
print(not_in("orthanc", files, r_index))
print(and_recovery_map(r_index["muerte"], r_index["llamado"]))
print(and_recovery_map(and_recovery_map(r_index["muerte"], r_index["llamado"]),r_index["deciden"]))