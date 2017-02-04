import time


text = input("Введіть текст:")
list = input("Введіть слово:")
a = 0
result=[]
def checker(q):
    i = q
    if i <= (len(text)-1):
       q = len(list) - 1
       if text[i] == list[q]:
           check(q,i,i)
       else:
           i = i + 1
           checker(i)
    else:
        print("I didnt find sorry")
        return
def check(x,y,r):
    # if x >= 0:
        if text[y] == list[x]:
           i = y
           y = y - 1
           x = x - 1
           if x == -1:
              result.append([text[i], i])
              print("I found")
              print(result)
              return
           else:
              check(x,y,r)
        else:
            r = r + 1
            checker(r)
    # else:
    #     r = r + 1
    #     checker(r)


t0 = time.time()
checker(a)
t1 = time.time()

total = t1-t0
print(total)


