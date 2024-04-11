class Raag:
    def __init__(self) -> None:
        self.allowed=list()
        self.not_allowed=list()

class operation:
    pass

swars=['s','r','R','g','G','m','M','P','d','D','n','N','S'," "]
sarang = Raag()

sarang.allowed=['s',' ','R'    ,'M','P' 
                ,'N','S']
sarang.not_allowed=['g','G','d','D']


sargam=[]


# for i in sarang.allowed:
#     for j in sarang.allowed:
#         for k in sarang.allowed:
#             for z in sarang.allowed:
#                 str_combination = [i, j, k,z]
#                 sargam.append(str_combination)

str_combination = [(i, j, k, l) for i in sarang.allowed for j in sarang.allowed for k in sarang.allowed for l in sarang.allowed]


print(len(str_combination))
import random

random_combinations = random.sample(str_combination, 10)
for combination in random_combinations:
    print(combination)
