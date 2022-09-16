def sum_l(l):
    res = 0
    for i in l:
        if type(i) != int or float:
            raise Exception("not a number")
        else:
            res += i
    return res