import math


arr = [1,12,5,26,7,14,3,7,2]


def schitalochka(m):
    y = math.floor(m/2)
    sort(y,0,0)


def sort(i,t,m):
    r = len(arr) - 1
    if t < i:
        n = r - m
        if arr[t] > arr[n]:
           arr[t] = arr[t] + arr[n]
           arr[n] = arr[t] - arr[n]
           arr[t] = arr[t] - arr[n]
           t = t + 1
           m = m + 1
           sort(i,t,m)
        else:
            t = t + 1
            sort(i,t,m)шрншнкпкпракаиаиитптптатпату4ек4кртеииаиапипат счмапивариси ваитаент
    else:
        print(arr)
        return

schitalochka(len(arr))
