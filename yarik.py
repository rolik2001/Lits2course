import time

u_str = input('Type a string to search in\n')
sub = input('Type word to search\n')
sublen = len(sub) - 1

def process(string, sub):

    if string[sublen] != sub[sublen]:
        if string[sublen] in sub:
            position = findStep(string, sub)
            drag(string, position)
        else:
            drag(string, len(sub))
    else:
        isMatch = compare(string[:sublen + 1], sub)
        if isMatch == True:
            print('Found')
        else:
            drag(string, len(sub))


def findStep(string, sub):
    stopChar = string[sublen]
    for i in range(sublen + 1):
        if sub[i] == stopChar:
            step = (len(sub) - i) - 1
            return step

def drag(string, step):
    process(string[step:], sub)

def compare(string, sub):
    if string == sub:
        return True
    else:
        return False

t0 = time.time()
process(u_str, sub)
t1 = time.time()

print(t1 - t0)