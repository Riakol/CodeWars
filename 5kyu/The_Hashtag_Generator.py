def generate_hashtag(s):
    result = '#'
    for i in s.lower().split():
        result += i.title()
    return result if s and len(result) < 140 else False

'''
https://www.codewars.com/kata/52449b062fb80683ec000024
'''
