import random
import time

def getRandomDate(startDate,EndDate):

    randomgenerator = random.random()
    dateFormat="%d/%m/%Y"

    startTime=time.mktime(time.strptime(startDate,dateFormat))
    EndTime=time.mktime(time.strptime(EndDate,dateFormat))

    randomTime = startTime + randomgenerator*(EndTime-startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate

print('random date = ', getRandomDate("1/1/2016", "12/12/2018"))





