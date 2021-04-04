# the list "meals" is already defined
# your code here
daily_cal = 0
for food in meals:
    daily_cal += food["kcal"]
print(daily_cal)
