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

s = input("Please input the sentence: ")
print(s)
ll = s.split(" ")
print("There are total %i words"%len(ll))



mydict = dict()
i = 0  # use i get all values in ll list.
j = 1 # use j calculate word appear times.
while i < len(ll):
    if (ll[i] in mydict):
        mydict[ll[i]]= mydict[ll[i]] + 1
        i=i+1
    else:
        mydict[ll[i]] = 1
        i=i+1

print(mydict)