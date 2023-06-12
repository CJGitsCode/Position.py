val = '***0***'
item = '*******'
idx = 0
running = False
fix = '*'
index = 0
digits = []
def CreateDigits():
    cleaned = ''
    for i in range(len(val)):
        digits.append('*')
        cleaned = f"{cleaned}*"
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
        if val == cleaned:
            runnning = False
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
