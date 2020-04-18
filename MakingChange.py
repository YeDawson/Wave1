print("insert amount of money paid in cents:")
paid = int(input())
print("Insert Cost of Purchase in cents:")
purchase = int(input())
change = paid - purchase

#NT stands for number of Toonies, the rest will correspond with similar naming
NT = change // 200
change %= 200
NL = change // 100
change %= 100
NQ = change // 25
change %= 25
ND = change // 10
change %= 10
NN = change // 5
change %= 5
NP = change

print("Number of Toonies due:" , NT)
print("Number of Loonies due:" , NL)
print("Number of Quarters due:" , NQ)
print("Number of Dimes due:" , ND)
print("Number of Nickels due:" , NN)
print("Number of Pennies due:" , NP)