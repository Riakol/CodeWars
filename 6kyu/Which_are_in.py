def in_array(array1, array2):
    res = []
    for i in array1:
        for j in array2:
            if i in j:
                res.append(i)
                break
    return sorted(set(res))


'''
https://www.codewars.com/kata/550554fd08b86f84fe000a58
'''
