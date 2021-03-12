lst = [1, 2, 3]
last = blackbox(lst)
if lst is last:
    print("modifies")
else:
    print("new")
