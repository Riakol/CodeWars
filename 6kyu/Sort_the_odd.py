def sort_array(source_array):
    odds = sorted(list(filter(lambda x: x % 2 == 1, source_array)))
    total = []
    x = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            total.append(source_array[i])
        else:
            total.append(odds[x])
            x += 1
    return total


'''
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
'''
