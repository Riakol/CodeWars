def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


'''
https://www.codewars.com/kata/52c31f8e6605bcc646000082
'''
