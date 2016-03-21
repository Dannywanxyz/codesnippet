import re
# m = 'abcdef'
# pattern = re.compile(r'abcdef')
# a = re.match(r'abcdefg', 'abcdefghij')
# print a.group()


def check_pwd(pwd):
    if len(pwd)<=8:
        print 'your password is too short'
    pattern = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,8}$')
    match = pattern.findall(pwd)
    if match:
        print 'Your password is safe.'
    else:
        print 'Your password is illegal!'
check_pwd('ABC12abc')

def abc(pwd):
    pattern = re.compile(r'^[a-zA-z]+$')
    match = pattern.findall(pwd)
    if match:
        return True
    else:
        return False
print 'this is fun!'
print