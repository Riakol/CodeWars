def scramble(s1, s2):
    for i in set(s2):
        if s2.count(i) <= s1.count(i):
            continue
        else:
            return False
    else:
        return True


'''
https://www.codewars.com/kata/55c04b4cc56a697bb0000048
'''