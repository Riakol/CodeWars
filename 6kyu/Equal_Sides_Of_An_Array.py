def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[1:]) == 0:
            return i
        elif sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    else: 
        return -1


'''
https://www.codewars.com/kata/5679aa472b8f57fb8c000047
'''