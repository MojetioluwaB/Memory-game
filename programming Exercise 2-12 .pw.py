COMMISION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 40.0

amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommision = amountPaidForStock * COMMISION_RATE
totalPaid = amountPaidForStock + purchaseCommision

stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommision = stockSoldFor * COMMISION_RATE
totalReceived = stockSoldFor - sellingCommision

profitOrLoss = totalReceived - totalPaid


print ("Amount paid for the stock: $", format(amountPaidForStock, '.2f'))
print ("Commission paid on the purchase: $",format(purchaseCommision, '.2f'))
print ("Amount the stock sold for: $", format(stockSoldFor, '.2f'))
print ("Commision paid on the sale: $", format(sellingCommision, '.2f'))
print ("Profit (or loss if negative) $", format(profitOrLoss, '.2f'))
