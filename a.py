from datetime import datetime as dt


date_to = dt.today().strftime(f'%Y-%m-{dt.today().day+3}')
date_to = date_to.replace('-' , " ").split()
for x in date_to:
    x = int(x)
if date_to[-1]  > 31:
    date_to[1] += 1
    if date_to[1] > 12:
        date_to[0] += 1



print(date_to)