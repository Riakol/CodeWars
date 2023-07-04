def counter_len(n):
    return [n, '0' + str(n)][n in range(10)]

def make_readable(seconds):
    hours = ((seconds // 3600) % 100)
    minutes = (seconds // 60) % 60
    secs = (seconds - ((23 * 3600) + (59 * 60))) % 60
    return f"{counter_len(hours)}:{counter_len(minutes)}:{counter_len(secs)}"


'''
https://www.codewars.com/kata/52685f7382004e774f0001f7
'''