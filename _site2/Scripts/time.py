from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%Y/%m/%d %H:%M:%S")
print("d1 =", d1)
