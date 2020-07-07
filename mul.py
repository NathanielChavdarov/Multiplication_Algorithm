# mulPeasant multiplies two integers using Peasant multiplication
# https://en.wikipedia.org/wiki/Multiplication_algorithm#Binary_or_Peasant_multiplication
global a
global b


def mulPeasant(a: int, b: int) -> int:
    result: int = 0

    # TO BE IMPLEMENTED
    BList = []
    Total = []
    Add = []
    counter = 0

    Total.append(a)

    for i in range(100):
        a = int(a >> 1)
        if (a % 2 != 0):
            Total.append(a)
            counter += 1
        if (a % 2 == 0):
            Total.append(a)
            counter += 1
        if a == 1:
            counter += 1
            break

    BList.append(b)

    for x in range(counter-1):
        b = b + b
        BList.append(b)

    for l in range(counter):
        if (int(Total[l]) % 2 != 0):
            Add.append(BList[l])
        if (int(Total[l]) % 2 == 0):
            None

    print(sum(Add))

    print(BList)
    print(Total)




mulPeasant(25, 25)
