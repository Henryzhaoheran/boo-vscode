'''
user input a sentence and we calculate how many words are inputed

'''

'''
#check if key in 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)

print("brand" in car)
'''
# user input a sentence
s = input("Please input the sentence: ")
print(s)

#split the sentence with space " " and put in list
wordslist = s.split(" ")

#Calulate the list lengtha and print the total words in the sentence.
print("There are total %i words"%len(wordslist))


#Myself writing code for the dictionary
'''
mydict = dict()
i = 0  # use i get all values in ll list.
j = 1 # use j calculate word appear times.
while i < len(wordslist):
    if (wordslist[i] in mydict):
        mydict[wordslist[i]]= mydict[wordslist[i]] + 1
        i=i+1
    else:
        mydict[wordslist[i]] = 1
        i=i+1

print(mydict)
'''

#Lesson learn code for the dictionary
mydict = {}

for m in wordslist:
    if m not in mydict:
        mydict[m] = 1
    else:
        mydict[m] = mydict[m] + 1

print(mydict)

# User input the word he wants to search appear number
search_code = input("Please input the word you would like to search: ")

# if the word in the dictionary, then print the times, otherwise, print it's not there.

if search_code in mydict:
    print("the word %s appear %i times"%(search_code, mydict[search_code]))
else:
    print("Your searched word '%s' is not there"%search_code)
