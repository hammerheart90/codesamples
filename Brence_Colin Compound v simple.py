#declare principle, rate, and time based on user inpit
principle= int(input("Enter the amount of the principle"))
rate= float(input('Enter annual percentage rate'))
time= int(input('Enter the amount of years of deposit'))
 
#calculate and display amounts using simple interest 
total_simple = (principle*rate*time)/100
print('\nTotal amount with simple interest = %f' %total_simple)

#calculate and display amounts using compound interest    
total_compound = principle * (((1+(rate/(100)))**time))
print('\nTotal Amount with compound interest = %f' %total_compound)

#declare difference between compound interest and simple interest total amounts
difference= total_compound- total_simple

#display total difference between using simple interest and compound interest
print('\nTotal dollars more with compound interest=%f' %difference)
