#this is the first project of python course

#how to read and print a txt file
f = open('liverpoolhistory.txt' , 'r')
content = f.read()
#print(content)

list_of_words = content.split()
#print(list_of_words)
#print(len(list_of_words))


#sorting the list based on length of element
sorted_list = sorted(list_of_words , key=len)
#sorting the list based on length of element and removing the doplicates
sorted_list_no_doplicate = sorted(set(list_of_words), key =len)
#print(sorted_list)
#print(str(sorted_list_no_doplicate))


#seperating top 20 word in txt file based on length
nodoplicate_list = list(sorted_list_no_doplicate)
final_list = nodoplicate_list[-20:]
print(final_list)

