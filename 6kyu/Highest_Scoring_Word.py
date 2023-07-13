import string

def high(x):
    alphabet = string.ascii_lowercase
    my_dict = {}
    for i in x.split():
        my_dict[i] = sum([alphabet.index(x) + 1 for x in i])
    return max(my_dict.items(), key=lambda x: (x[1]))[0]


'''
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
'''