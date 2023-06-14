def points(games):
    total = 0
    for i in games:
        if i.split(':')[0] > i.split(':')[1]:
            total += 3
        elif i.split(':')[0] < i.split(':')[1]:
            continue
        else:
            total += 1
    return total


'''
https://www.codewars.com/kata/5bb904724c47249b10000131
'''
