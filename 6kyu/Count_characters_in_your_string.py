def count(s):
    letters = dict()
    for i in s:
        letters[i] = letters.get(i, 0) + 1
    return letters


'''
https://www.codewars.com/kata/52efefcbcdf57161d4000091
'''