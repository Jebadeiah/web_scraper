let_ya_feet_stomp = dict()
wutang = input().lower()
da_front = wutang.split()
for clan in da_front:
    if clan in let_ya_feet_stomp:
        let_ya_feet_stomp[clan] += 1
    else:
        let_ya_feet_stomp[clan] = 1
for key, value in let_ya_feet_stomp.items():
    print(f"{key} {value}")
