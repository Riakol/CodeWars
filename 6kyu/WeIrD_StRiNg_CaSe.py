def to_weird_case(words):
    res = [i for i in words]
    counter = 0
    for i in range(len(words)):
        if words[i].isalpha():
            if counter % 2 == 0:
                res[i] = words[i].upper()
                counter += 1
            else:
                res[i] = words[i].lower()
                counter += 1
        else:
            counter = 0
    return ''.join(res)


'''
https://www.codewars.com/kata/52b757663a95b11b3d00062d
'''
