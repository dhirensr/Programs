t = int(input().strip())
a={}
loss = 0
for i in range(t):
    no_of_recipes = int(input().strip())
    for j in range(no_of_recipes):
        a[j]= input()
    for k in range(no_of_recipes):
        a[k] = [int(n) for n in a[k].split()]
    for k in range(no_of_recipes):
        [price,units,percent_discount] = a[k]
        discount_price = price + price*percent_discount/100
        total_discount = discount_price - discount_price*percent_discount/100
        loss_per_unit = price - total_discount
        loss+= loss_per_unit* units
        width = 11- len(str(int(loss)))
        print(width)
print('%.*f' % (width, totalLoss))
