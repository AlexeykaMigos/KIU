def count_lang(d):
    totalnum = max(d.values())
    def get_key(d, value):
         return [k for k, v in d.items() if v == value]
    name = list(get_key(d, totalnum))
    minnum = list(get_key(d, min(d.values())))
    if len(name) != 1:
        return(name[1:] + minnum)
    else:
        lis = list()
        lis.append("NO")
        return(lis + minnum)