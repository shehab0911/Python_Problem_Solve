# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random

list =[]
for x in range(100):
    list.append(random.randrange(1000000000,9999999999))
winner=random.sample(list,2)
print(winner)
