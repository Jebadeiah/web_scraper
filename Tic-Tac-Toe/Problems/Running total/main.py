wutang = [int(x) for x in input()]
wutang_clan = [sum(wutang[:y] for (x, y) in enumerate(wutang)) for x in wutang]
print(wutang_clan)
