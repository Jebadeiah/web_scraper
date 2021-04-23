top_cafe = ['', 0]

while True:
    wutang = input()
    wu_tang = wutang.split()
    if wutang == 'MEOW':
        break
    elif int(top_cafe[1]) < int(wu_tang[1]):
        top_cafe = wu_tang

print(top_cafe[0])
