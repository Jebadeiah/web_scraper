seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
minutes = [int(x / 60) for x in seconds]
hours = [int(x / 3600) for x in seconds]
days = [int(x / 86400) for x in seconds]
print(days)
