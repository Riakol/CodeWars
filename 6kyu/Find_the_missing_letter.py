import string

def find_missing_letter(chars):
    low = string.ascii_lowercase
    f_indx = low[low.index(sorted(chars)[0].lower()):]

    for mine, orig in zip(f_indx, sorted(chars)):
        if mine != orig.lower():
            return mine.upper() if chars[0] == chars[0].upper() else mine


'''
https://www.codewars.com/kata/5839edaa6754d6fec10000a2

'''
