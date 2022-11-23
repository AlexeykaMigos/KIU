
def summa (numbers: list):
    if len(numbers) != 4:
        return "error"
    for num in numbers:
        if not isinstance(num, int):
            return "error"
    return [float(numbers[0] + numbers[2]), float(numbers[1] + numbers[3])]




def raznost(numbers: list):
    if len(numbers) != 4:
        return "error"
    for num in numbers:
        if not isinstance(num, int):
            return "error"
    return [float(numbers[0] - numbers[2]), float(numbers[1] - numbers[3])]


def multi(numbers: list):
    if len(numbers) != 4:
        return "error"
    for num in numbers:
        if not isinstance(num, int):
            return "error"
    return [float((numbers[0] * numbers[2]) - (numbers[1]*numbers[3])),float((numbers[0]*numbers[3]) + (numbers[1]*numbers[2]) ) ]


def divide(numbers: list):
    if len(numbers) != 4:
        return "error"
    for num in numbers:
        if not isinstance(num, int):
            return "error"
    if (numbers[2] * numbers[2]) + (numbers[3] * numbers[3]) == 0:
        return "error"
    return [round(float(((numbers[0]*numbers[2])+(numbers[1]*numbers[3])) / ((numbers[2] * numbers[2]) + (numbers[3] * numbers[3]))),4), round(float(((numbers[2]*numbers[1])-(numbers[0]*numbers[3])) / ((numbers[2] * numbers[2]) + (numbers[3] * numbers[3]))),4)]


