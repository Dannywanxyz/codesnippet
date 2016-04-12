# a = {
#     1:1,
#     2:2,
#     3:3
# }
# print ','.join(map(str, a.keys()))
# b = '123456'
# c = [b[i] for i in range(len(b)) if i&1 == 1]
# print ''.join(c)
# print b[0::2]
# for num in range(1, 100+1):
#     count = 0
#     for n in range(1, num+1):
#         if num % n == 0:
#             count += 1
#     if count == 2:
#         print num,
# print
# a = [1, 2, 5, 6, 4, 3]
# def middle(L):
#     l = len(L)
#     L.sort()
#     if l%2 == 1:
#         print L[(l-1)/2]
#     else:
#         print float(L[l/2] + L[(l-1)/2])/2
# middle(a)
# def gcd(a, b):
#     if a > b:
#         if b==0:
#             return a
#         return gcd(b, a%b)
#     return gcd(a, b%a)
# a = 54
# b = 42
# print gcd(a, b)
# L = [2, 3, 500, 8]
# sum = 1
# for i in L:
#     sum *= i
# a = str(sum)
# count = 0
# for j in a[::-1]:
#     if j == '0':
#         count += 1
#     else:
#         break
# print count
a = '123456'
new = reversed(a)
for i in new:
    print ''.join(i),
