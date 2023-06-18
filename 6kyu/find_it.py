def find_it(seq):
    unique = list(set(seq))
    answer = [unique[i] for i in range(len(unique)) if seq.count(unique[i]) % 2 == 1]
    return answer[0]


'''
https://www.codewars.com/kata/54da5a58ea159efa38000836
'''
