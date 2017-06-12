#!/usr/bin/python3.5

brand = "Apple"
exchangeRate = 1.23445823942
message = "The price of this {0:s} laptop is ${1:d} and the exchange rate is $ {2:4.4f}".format(brand, 1599, exchangeRate)

print(message)
