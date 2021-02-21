price = 1000000
is_good_credit = False

if is_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(down_payment)