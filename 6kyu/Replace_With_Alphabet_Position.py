def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for x in text.lower():
        if x in alphabet:
            result += str(alphabet.index(x) + 1) + ' '
    return result[:-1]


'''
https://www.codewars.com/kata/546f922b54af40e1e90001da
'''