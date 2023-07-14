def duplicate_count(text):
    total = 0
    txt = text.lower()
    for i in txt:
        if txt.count(i) > 1:
            total += 1
            txt = txt.replace(i, '')
    return total


'''
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
'''