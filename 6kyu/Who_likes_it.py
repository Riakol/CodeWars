def likes(names):
    if names:
        if len(names) == 1:
            return f"{names[0]} likes this"
        if len(names) == 2:
            return f"{' and '.join(names)} like this"
        if len(names) == 3:
            return f"{', '.join(names[:2])} and {names[-1]} like this"
        if len(names) >= 4:
            return f"{', '.join(names[:2])} and {len(names[2:])} others like this"
    else:
        return "no one likes this"
    

'''
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python
'''