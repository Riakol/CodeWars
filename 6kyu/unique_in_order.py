def unique_in_order(sequence):
    if sequence:
        res = []
        res.append(sequence[0])
        for i in sequence:
            if not i in res or i != res[-1]:
                res.append(i)
            else:
                continue
        return res
    else:
        return []


'''
https://www.codewars.com/kata/54e6533c92449cc251001667
'''
