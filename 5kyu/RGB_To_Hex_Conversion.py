def custom_hex(rgb):
    hexadecimal = {'10': 'A',
                '11': 'B',
                '12': 'C',
                '13': 'D',
                '14': 'E',
                '15': 'F'}

    result = ''

    if rgb in range(10):
        return '0' + str(rgb)

    if rgb in range(10, 256):
        while rgb > 0:
            prcnt_div = (rgb % 16)
            rgb = rgb // 16
            if prcnt_div in range(10):
                result = str(prcnt_div) + result
            else:
                result = hexadecimal[str(prcnt_div)] + result
        return '0' + result if len(result) < 2 else result
    else:
        return 'FF'


def rgb(r, g, b):
    res = ''
    for i in [r, g, b]:
        if i < 0:
            res += '00'
        else:
            res += str(custom_hex(i))
    return res


'''
https://www.codewars.com/kata/513e08acc600c94f01000001
'''
