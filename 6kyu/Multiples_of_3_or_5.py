def solution(number):
    if number > 0:        
        res = filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1, number)])
        return sum(res)
    else:
        return 0


'''
https://www.codewars.com/kata/514b92a657cdc65150000006
'''
