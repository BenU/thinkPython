coverPr = 24.95
bkStrDis = 0.40
shippingFirst = 3.0
shippingAdditn = 0.75
totalCopies = 60

bookCost = coverPr * bkStrDis * totalCopies
shipping = shippingFirst + (totalCopies-1)*shippingAdditn

totalWCost = bookCost + shipping
print totalWCost