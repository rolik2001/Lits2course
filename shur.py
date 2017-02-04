

list = [["a", "1"], ["b", "2"], ["c", "3"], ["d", "4"], ["e", "5"], ["f", "6"], ["g", "7"], ["h", "8"], ["i", "9"],
        ["j", "10"], ["k", "11"], ["l", "12"], ["m", "13"], ["n", "14"], ["o", "15"], ["p", "16"], ["q", "17"],
        ["r", "18"], ["s", "19"], ["t", "20"], ["u", "21"], ["v", "22"], ["w", "23"], ["x", "24"], ["y", "25"],
        ["z", "26"], [" ", "27"]]

exit = []


def coding():
    text = input("Введіть текст on English :")
    user = ""
    y = 0
    for i in range(len(text)):
        text = text.lower()
        for z in range(len(list)):
            if list[z][0] == text[i]:
                exit.append("#")
                exit.append(list[z][1])
    user = user.join(exit)
    print(user)

coding()


def antcoding():
    text = input("Введіть текст on English :")
    user = ""
    all = []
    m = []
    for i in range(len(text)):
        if exit[i] == "#":
           m.append(i)
           if len(m) != 1:
               n = i - 1
               if int(m[i]) - int(m[n]) != 0:
                  b = float(m[i]) - float(m[n])
                  print(m[i])
#             for z in range(len(list)):
    #                 if text[i] == list[z]:
    #                    all.append(list[z][1])
    # user = user.join(all)
    print(b)

antcoding()