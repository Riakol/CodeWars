def tribonacci(signature, n):
    x = 0
    tribonacci = signature
    for _ in range(n):
        tribonacci.append(sum(tribonacci[x:]))
        x += 1
    return tribonacci[:n]


'''
https://www.codewars.com/kata/556deca17c58da83c00002db
'''
