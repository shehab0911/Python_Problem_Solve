import random
num1=[1,2,3,4,5,6]

for i in range(5):
    random.seed(14)
    print(random.choice(num1))
