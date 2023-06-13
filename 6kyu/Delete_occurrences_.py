def delete_nth(order,max_e):
    filtered = []
    for i in order:
        if filtered.count(i) < max_e:
            filtered.append(i)
    return filtered


'''
https://www.codewars.com/kata/554ca54ffa7d91b236000023
'''