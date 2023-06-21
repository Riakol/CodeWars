from functools import reduce

def persistence(n):
    result = list(''.join(str(n)))
    temp = 0
    x = 0
    while len(str(result)) != 1:
        temp = reduce(lambda x, y: int(x) * int(y), result, 1)
        result = str(temp)
        x += 1
    return x


'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
'''