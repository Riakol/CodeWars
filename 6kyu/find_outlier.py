def find_outlier(integers):
    if len([i for i in integers if i % 2 == 0]) == 1:
        return [i for i in integers if i % 2 == 0][0]
    else:
        return [i for i in integers if i % 2 != 0][0]


'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
'''