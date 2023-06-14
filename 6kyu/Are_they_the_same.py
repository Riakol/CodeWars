def comp(array1, array2):
    if type(array1) == list and type(array2) == list:
        main_array = sorted([i*i for i in array1]) 
        alternate = sorted(array2)
        return main_array == alternate
    else:
        return False

'''
https://www.codewars.com/kata/550498447451fbbd7600041c
'''