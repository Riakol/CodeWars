def is_pangram(s):
    return len(set(list(map(lambda x: x, filter(lambda x: x.isalpha(), [i.lower().strip(',.! 0123456789') for i in s]))))) == 26


'''
https://www.codewars.com/kata/545cedaa9943f7fe7b000048
'''
