def digital_root(n):
    while len(str(n)) != 1:
        res = sum([int(i) for i in ' '.join(str(n)).split()])
        n = str(res)
    return n


'''
https://www.codewars.com/kata/541c8630095125aba6000c00
'''
