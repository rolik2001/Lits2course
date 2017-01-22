a = []

def stop():
    print("Дякуємо за те що використали мого бота")
    return
def remove():
 object = input('Напишіть назву продукту:')
 for i in range(len(a)):
    if a[i][0]== object :
     del a[i][0]
     del a[i][0]
     command = input('Що робити далі ? Напишіть add що добавити або remove щоб видалити елемент або stop :')
     if "add" in command:
       add()
     elif "remove" in command:
       remove()
     elif "list" in command:
         list()
     elif "stop" in command:
         stop()
def add():
    object = input('Напишіть назву продукту:')
    parameter = input('Напишіть ціну продукту:')
    a.append([object, parameter])
    command = input('Що робити далі ? Напишіть add що добавити або remove щоб видалити елемент або stop або list щоб переглянути список:')
    if "add" in command:
        add()
    elif "remove" in command:
        remove()
    elif "list" in command:
        list()
    elif "stop" in command:
        stop()
def list():
    if len(a) == 0:
        print("Список пустий")
    else:
      print(a)
      command = input('Що робити далі ? Напишіть add що добавити або remove щоб видалити елемент або stop або list щоб переглянути список:')
      if "add" in command:
       add()
      elif "remove" in command:
       remove()
      elif "list" in command:
       list()
      elif "stop" in command:
        stop()

add()
