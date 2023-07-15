def longest_consec(strarr, k):
    if strarr and k < len(strarr) and k > 0:
        for elem in range(len(strarr)):
            strarr[elem] = ''.join(strarr[elem: k + elem])
        return max(strarr, key=len)
    else:
        return ""


'''
https://www.codewars.com/kata/56a5d994ac971f1ac500003e
'''
