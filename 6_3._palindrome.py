def is_palindrome(s):
    l = s.split(" ")
    s2 = "".join(l)
    return s2 == s2[::-1]

