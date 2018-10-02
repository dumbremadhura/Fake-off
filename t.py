from itertools import *
  
# Get all permutations of [1, 2, 3] 
shapes = ['Nirav Modi', 'Nirav', 'Money laundering', 'Hong Kong', 'enforcement directorate', 'Dubai']

result = combinations(shapes, 3)

ls =[]

query = ""

for each in result:
    ls.append(list(each))


print(ls)
print("+=++++++++++++++++++++++++++++++++++++")
for i in range(len(ls)):
    ls[i].insert(1," AND ")
    ls[i].insert(3," AND ")

print(" jh ".join(ls[0]))



