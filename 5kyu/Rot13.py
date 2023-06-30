def upper_case(upper):
    return chr(upper) if upper in range(65, 91) else chr((upper % 90) + 64)

def lower_case(lower):
    return chr(lower) if lower in range(97, 123) else chr((lower % 122) + 96)

def rot13(message):
    encrypted = ''
    for i in message:
        if i.isalpha():
            sym = ord(i) + 13
            if i == i.upper():
                encrypted += upper_case(sym)
            else:
                encrypted += lower_case(sym)
        else:
            encrypted += i
    return encrypted


'''
https://www.codewars.com/kata/530e15517bc88ac656000716
'''
