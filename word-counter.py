#this is the first project of python course

#how to read and print a txt file
f = open('liverpoolhistory.txt' , 'r')
content = f.read()
#print(content)

list_of_words = content.split()
print(list_of_words)
#print(len(list_of_words))

sorted_list = sorted(list_of_words , key=len)
print(sorted_list)
