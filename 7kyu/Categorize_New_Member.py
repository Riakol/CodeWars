def open_or_senior(data):
    return list(map(lambda x: ['Open', 'Senior'][x[0] >= 55 and x[1] > 7], data))


'''
https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
'''
