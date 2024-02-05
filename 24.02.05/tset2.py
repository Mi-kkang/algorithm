# s1 = 'abc'
# s2 = 'abc'
#
# print(s1 == s2)
# print(s1 is s2)
#
# s3 = s1[:2] + 'c'
# print(s3)
# print(s1 == s3)
# print(s1 is s3)


def itoa(a) :
    s = ''

    while a > 0 :
        s = chr(a % 10 + ord('0')) + s
        a //= 10

    return s

ans = itoa(123)
print(ans)