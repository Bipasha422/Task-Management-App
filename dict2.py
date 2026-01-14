sale = {
    "january":15000,
    "february":2000,
    "March":3000,

}
item=sale.popitem()
print("popped item:",item)
sale.pop("March")
print(sale)
print(sale)
sale.clear()
print(sale)