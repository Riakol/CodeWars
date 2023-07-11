def solution(s):
    res = []
    for i in range(0, len(s), 2):
        if len(s[i:i + 2]) % 2 == 0:
            res.append(s[i:i + 2])
        else:
            res.append(f"{s[i:i + 2]}_")
    return res


'''
https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
'''