def spin_words(sentence):
    res = ' '.join(list(map(lambda x: [x, x[::-1]][len(x) >= 5], [i for i in sentence.split()])))
    return res


'''
https://www.codewars.com/kata/5264d2b162488dc400000001
'''
