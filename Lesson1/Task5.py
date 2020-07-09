# Task5
rev = int(input('Input your revenue: '))
costs = int(input('Input your costs: '))
prof = rev - costs
if rev = costs:
    print('Your rev = costs')
elif rev > costs:
    print(f'Your profit = {prof}')
    print(f'Your profitability = {prof / rev}')
    emp = int(input('Input your number of employees: '))
    print(f'Your profit per employee = {emp / prof}')
else:
    print(f'Your loss = {-prof}')
