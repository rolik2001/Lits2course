number = 321
def recursiv(number):
    t = number % 10
    s = number // 10
    if s == 0:
        print(t)
        return
    else:
        print(t);
        recursiv(s)



recursiv(number)