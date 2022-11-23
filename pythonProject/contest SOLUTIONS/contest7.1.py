def sort_two_list(spisok1,spisok2):
    inter = set(spisok1).intersection(spisok2)
    return sorted(inter)