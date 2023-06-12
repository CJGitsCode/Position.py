val = '***0***'
item = '*******'
idx = 0
running = False
fix = '*'
index = 0
digits = []
def CreateDigits():
    global item
    global idx
    idx = 0
    for i in range(len(item)):
        digits.append(item[idx])
        idx += 1
def Swap(first, second):
    global fix
    digits[first] = second
def CreateItem():
    global item
    global index
    length = len(item)
    item = ''
    index = 0
    for i in range(length):
        item = f'{item}{digits[index]}'
        index += 1
def FindPosition():
    global idx
    global running
    global item
    global val
    running = True
    idx = 0
    while running:
        Swap(idx, '0')
        CreateItem()
        if val == item:
            idx += 1
            running = False
            print(idx)
        else:
            Swap(idx, '*')
        idx += 1
CreateDigits()
FindPosition()
