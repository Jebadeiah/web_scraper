with open('salary.txt') as sal, open('salary_year.txt', 'w') as sal_year:
    for monthly in sal:
        sal_year.write(str(int(monthly) * 12) + '\n')
