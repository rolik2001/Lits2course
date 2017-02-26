import math

roma = [4,2,190,19,38,7,5,3]
str = []

def schitalochka(m,b):
    if m >= 2:
        y = math.floor(m/2)
        str.append(m)
        x = b + 1
        schitalochka(y,x)
    else:
        str.append(m)
        print(str)
        arr(1)


def arr(f):
    m = len(str) - f
    if f >= len(str):
       return
    else:
         check(str[m],0,f)


def check(a,i,f):
    if i < len(roma)-1:
        for t in range(a):
            if i+t <= len(roma)-1:
               if roma[i] > roma[i+t]:
                  roma[i] = roma[i]+roma[i+t]
                  roma[i+t] = roma[i] - roma[i+t]
                  roma[i] = roma[i] - roma[i+t]
                  print(roma)
        m = i + 1
        check(a,m,f)
    else:
        f = f + 1
        arr(f)


schitalochka(len(roma),0)
