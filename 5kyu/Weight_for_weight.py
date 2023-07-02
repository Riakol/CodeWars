def order_weight(strng):
    return ' '.join((sorted(sorted(strng.split()), key=lambda x: sum([int(i) for i in x]))))


'''
https://www.codewars.com/kata/55c6126177c9441a570000cc
'''
