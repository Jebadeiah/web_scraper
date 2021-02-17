def cumulative_sum(num_list):
    wutang = []
    bobby = 0
    for digital in num_list:
        bobby += digital
        wutang.append(bobby)
    return wutang

print(cumulative_sum([int(x) for x in input()]))
