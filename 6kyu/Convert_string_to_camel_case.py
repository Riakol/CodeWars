def to_camel_case(text):
    if text:
        for i in text:
            if not i.isalpha():
                text = text.replace(i, ' ')
        f, *others = text.split()
    return  f + ''.join([i.title() for i in others]) if text else ""


'''
https://www.codewars.com/kata/517abf86da9663f1d2000003/python
'''
