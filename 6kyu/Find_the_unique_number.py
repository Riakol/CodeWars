def find_uniq(arr):
    unique = list(set(arr))
    s = [unique[i] for i in range(len(unique)) if arr.count(unique[i]) == 1]
    return s[0]


'''
https://www.codewars.com/kata/585d7d5adb20cf33cb000235
'''
