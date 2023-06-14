def odd_or_even(arr):
    if not arr:
        return [0]
    else:
        return ['even', 'odd'][sum(arr) % 2 != 0]


'''
https://www.codewars.com/kata/5949481f86420f59480000e7
'''
