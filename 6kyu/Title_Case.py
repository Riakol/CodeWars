def title_case(title, minor_words=''):
    if title:
        res = [i.title() for i in title.lower().split()]
        minor_words = [i for i in minor_words.lower().split()]
        for i in range(1, len(res)):
            if res[i].lower() in minor_words:
                res[i] = res[i].lower()
        return ' '.join(res)
    return ''


'''
https://www.codewars.com/kata/5202ef17a402dd033c000009
'''
