a = []

def stop():
    print("Дякуємо за те що використали мого бота")
    return
def remove():
 object = input('Напишіть назву продукту:')
 for i in range(len(a)):
    if a[i][0]== object :
     del a[i]
     checker()
    else:
     print('Не знайшло')
     checker()


def add():
    object = input('Напишіть назву продукту:')
    parameter = input('Напишіть ціну продукту:')
    a.append([object, parameter])
    checker()


def list():
    if len(a) == 0:
        print("Список пустий")
    else:
      print(a)
     checker()
def checker():
    command = input(
        'Що робити далі ? Напишіть add що добавити або remove щоб видалити елемент або stop або list щоб переглянути список:')
    if "add" in command:
        add()
    elif "remove" in command:
        remove()
    elif "list" in command:
        list()
    elif "stop" in command:
        stop()
    else
        checker()
add()
