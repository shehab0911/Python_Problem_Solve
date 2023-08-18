#String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
import  random
import  string

def getStringLenth(length):

    result=' '.join(random.choice(string.ascii_letters) for i in range(length))
    print(result)

getStringLenth(8)


