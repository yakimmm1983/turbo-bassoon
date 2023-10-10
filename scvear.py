

from random import randint
array = []
for i in range(100):
    array.append(randint(1,20))

def mnog():
    mno = set(array)
    array1 = list(mno)
    return array1

def summ():
    summ = len(mnog())
    return summ
