#Larry and Earl are two workers looking to open two retirement accounts. Earl plans to deposit for the first fifteen years, then let interest accrue
#Larry 

#declare variables for deposit and initial value
earlDeposit = int(0)
larryDeposit = int(0)

#declare initial integer value for Larry and Earl's balances	
balanceLarry=int(0)	
balanceEarl= int(0)

#enter loops for calculating the deposits made by Larry and Earl, as well as their final balance

#calculate the deposits for Larry
for year in range(0,33): 
	larryDeposit = year * 5000
	year += 1
	
#calculate the deposits for Earl
for year in range(0,15): 
	earlDeposit = year * 5000
	year += 1

#calculate Earl's balance for the first 15 years with deposits of $5,000
for year in range(0,15): 
	balanceEarl = balanceEarl + (5000 + (balanceEarl * 0.04))
	year += 1
	
#calculate Earl's balance for the total of 33 years, this time with just the interest and not the deposits
for year in range(0,33): 
	balanceEarl += (balanceEarl * 0.04)
	year += 1

#calculate the  total balance for Larry
for year in range(0,33): 
	balanceLarry += (balanceLarry * 0.04) + 5000
	year += 1

print("\nEarl's total balance is equal to =%f" %balanceEarl)		
print("\nLarry's total balance is equal to =%f" %balanceLarry)
print("\nEarl's total deposits are equal to =%f" %earlDeposit)		
print("\nLarry's total deposits are equal to =%f" %larryDeposit)
