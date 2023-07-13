def duplicate_encode(word):
    word = word.lower()
    res = ''
    for i in word:
        if word.count(i) >= 2:
            res += ')'
        else:
            res += '('
    return res


'''
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
'''