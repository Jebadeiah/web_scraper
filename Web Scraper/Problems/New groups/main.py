groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
kid_counts = []
num_of_groups = int(input())
for _g in range(num_of_groups):
    kid_counts.append(int(input()))

empty_classes = len(groups) - num_of_groups

for _e in range(empty_classes):
    kid_counts.append(None)

wutang = dict(zip(groups, kid_counts))
print(wutang)
