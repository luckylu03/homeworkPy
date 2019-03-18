# Given a string, you have to return a string in which each character
# (case-sensitive) is repeated once.

def double_char(s):
    return ''.join(s[i]+s[i] for i in range(len(s)))