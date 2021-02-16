wutang = list(input())
print([int(x) if x == wutang[0] else int(x) + (int(wutang[wutang.index(x) - 1]) for x in wutang[:x]) for x in wutang])
