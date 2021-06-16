# Display 9x9 calculation

'''
#version 1
for a in range(1,10):
    for b in range(1,10):
        if a >= b:
            print("%i x %i = %i "%(b, a, a*b), end="\t")
    print("")
'''
'''
# improve. 
# variable name changes to row and column

'''
row = 1
while row <= 9:
    column = 1
    while row >= column: #and column <= 9:
        print("%i x %i = %i"%(column, row, column*row), end="\t")
        column = column + 1
    print("")
    row = row + 1
   

