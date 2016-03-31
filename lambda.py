# coding=utf-8
# filter函数用法
def is_even(x):
    return x % 2 != 0
# filter函数接收两个参数，第一个参数为函数名，第二个参数为所接收的可迭代序列
ls = filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8])
for a in ls:
    print a,
print

lt = [1, 2, 3, 4, 5]
def add(x):
    return x + 3
# map函数用法，接收两个参数，第一个参数是一个函数，第二个参数是可迭代序列，map将func函数应用到可迭代序列的每个元素中
# 然后以可迭代序列返回
rs = map(add, lt)
print rs

# reduce函数用法，同样接收两个参数，其第一参数必须为二元操作函数，效果是对参数序列中元素进行累积，
def multi(x, y):
    return x*y
res = reduce(multi, lt)
print res