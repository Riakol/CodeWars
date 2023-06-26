def is_valid_walk(walk):
    my_dict = {'n': 's',
            's': 'n',
            'e': 'w',
            'w': 'e'}
    return len(walk) == 10 and all(map(lambda x: walk.count(x) == walk.count(my_dict[x]), list(set(walk))))


'''
https://www.codewars.com/kata/54da539698b8a2ad76000228
'''
