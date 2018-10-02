'''
Code only for testing andf trying out stuff

'''
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

ko = ['Chandigarh news', 'Chandigarh latest news', 'Chandigarh news live', 'Chandigarh news today', 'Today news Chandigarh', 'serpents', 'security gurad', 'Rat snake', 'python']

bz =()

from fuzzywuzzy import fuzz

for i in ko:
    print("out")
    print(ko)
    for j in ko:
        if(i != j):
            if(i in j):
                print("in")
                print(ko)
                ko.remove(j)

        

print(ko)


# test sites
# https://www.ndtv.com/india-news/ncp-chief-sharad-pawar-retracts-rafale-remark-amid-stir-would-never-support-prime-minister-narendra-1925222
# https://timesofindia.indiatimes.com/india/nirav-modi-sent-stepbrother-to-hong-kong-to-get-hold-of-diamonds/articleshow/66035825.cms