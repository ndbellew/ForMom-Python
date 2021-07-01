import sys
from Address import *
from Customer import *

lines = sys.stdin.readlines()
#inputStr = "Conrad Hitzman|86 street Rd|Alhambra|CA|80768"
AllCustomers = []
for line in lines:
    inputStrings = line.split('|')

    Cust = Customer(inputStrings[0], Address(inputStrings[1],inputStrings[2],inputStrings[3],inputStrings[4]))
    AllCustomers.append(Cust)

AllCustomers = sorted(AllCustomers, key=lambda x: x.name, reverse=True)

for cust in AllCustomers:
    print(str(cust))