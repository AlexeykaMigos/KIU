abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def max_distance(string):
    max_dist_word = ""
    max_dist = 0
    for word in string.split():
        max_let = max(list(set(word) & set(abc)))
        min_let = min(list(set(word) & set(abc)))
        if abc.index(max_let) - abc.index(min_let) > max_dist:
            max_dist = abc.index(max_let) - abc.index(min_let)
            max_dist_word = word
    return max_dist_word