def longest_consec(strarr, k):
    for elem in range(len(strarr)):
        strarr[elem] = ''.join(strarr[elem: k + elem])
    return max(strarr, key=len) if strarr and k < len(strarr) and k > 0 else ""


'''
https://www.codewars.com/kata/56a5d994ac971f1ac500003e
'''
