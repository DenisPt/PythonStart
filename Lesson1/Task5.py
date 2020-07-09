# Task5
rev = int(input('Input your revenue: '))
costs = int(input('Input your costs: '))
prof = rev - costs
if rev == costs:
    print('Your rev = costs')
elif rev > costs:
    print(f'Your profit = {prof}')
    print(f'Your profitability = {(prof / rev) * 100:.0f}%')
    emp = int(input('Input your number of employees: '))
    print(f'Your profit per employee = {prof / emp:.1f}')
else:
    print(f'Your loss = {-prof}')
