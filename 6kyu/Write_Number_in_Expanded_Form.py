def expanded_form(num):
    num = str(num)
    return ' + '.join([num[i] + ('0' * len(num[i + 1:])) for i in range(len(num)) if num[i].isdigit() and int(num[i]) > 0])


'''
https://www.codewars.com/kata/5842df8ccbd22792a4000245
'''