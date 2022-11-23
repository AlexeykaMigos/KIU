
def summa(a):
    counter = sum(1 for _ in a)
    if counter != 4:
        return "error"
    for i in range(len(a)):
        if isinstance(i,int) == False:
            return "error"
    if type(a[0]) == str or type(a[1]) == str or type(a[2]) == str or type(a[3]) == str:
        return "error"
    a1 = a[0]
    a2 = a[2]
    b1 = a[1]
    b2 = a[3]
    z1 = a1 + a2
    z2 = b1 + b2
    return [z1, z2]




def raznost(a):
    counter = sum(1 for _ in a)
    if counter != 4:
        return "error"
    for i in range(len(a)):
        if isinstance(i,int) == False:
            return "error"
    if type(a[0]) == str or type(a[1]) == str or type(a[2]) == str or type(a[3]) == str:
        return "error"
    a1 = a[0]
    a2 = a[2]
    b1 = a[1]
    b2 = a[3]
    z1 = a1 - a2
    z2 = b1 - b2
    return [z1, z2]


def multi(a):
    counter = sum(1 for _ in a)
    if counter != 4:
        return "error"
    for i in range(len(a)):
        if isinstance(i,int) == False:
            return "error"
    if type(a[0]) == str or type(a[1]) == str or type(a[2]) == str or type(a[3]) == str:
        return "error"
    a1 = a[0]
    a2 = a[2]
    b1 = a[1]
    b2 = a[3]
    z1 = (a1 * a2) - (b1 * b2)
    z2 = (a1 * b2) + (b1 * a2)
    return [z1, z2]


def divide(a):
    counter = sum(1 for _ in a)
    if counter != 4:
        return "error"
    for i in range(len(a)):
        if isinstance(i,int) == False:
            return "error"
    if type(a[0]) == str or type(a[1]) == str or type(a[2]) == str or type(a[3]) == str:
        return "error"
    a1 = a[0]
    a2 = a[2]
    b1 = a[1]
    b2 = a[3]
    if (a2*a2)+(b2*b2) == 0:
        return "error"
    z1 = ((a1 * a2) + (b1*b2)) / ((a2*a2)+(b2*b2))
    z2 = ((a2 * b1) - (a1*b2)) / ((a2*a2)+(b2*b2))

    return [round(z1,4), round(z2,4)]



