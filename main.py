import utils.from_rwf
import utils.from_usd

currency=input("Currency 1:USD, 2:RWF: ")
amount = float(input("Enter the amount: "))
if currency=="2":
    utils.from_rwf.convert_currency(amount)
elif currency=="1":
    utils.from_usd.convert_currency(amount)
else:
    print("Invalid input")