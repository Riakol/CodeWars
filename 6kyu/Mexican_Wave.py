def wave(people):
    res = [i.lower() for i in people]
    finish = []
    for i in range(len(people)):
        if people[i].isalpha():
            res[i] = res[i].upper()
            finish.append(''.join(res))
            res[i] = res[i].lower()
    return finish



'''
https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
'''
