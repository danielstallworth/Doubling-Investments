
""" Figures out how long it would take for your money to double at a certain nominal interest rate
	You have 2 choices:
		1. Find out how long it would take for a number of doublings entered based on the principal investment (ex. enter 3 to see how long it would take for your investment to double 3 times). Also gives you the final amount after the doublings.
		2. Find out how long it takes for the final amount to reach a certain number. (ex. enter 1000000 to see when your investment will reach 1M at the specified interest rate)

A = P(1+r/n)^nt
A -> Final Amount
P -> Initial Principal
r -> Nominal Interest
n -> Number of times interest compounded
t -> Number of years

"""

# Imports
from math import log

# Enter the choice 
choice = int(raw_input("""Which one? 
			Enter 1 - How long will it take for doubling of my investment?
			Enter 2 - How long will it take for my investment to reach a certain amount? """))

if choice == 1:
	
	P = float(raw_input("How much do you have to start out with? "))
	
	r = float(raw_input("What is the decimal interest rate? "))
	
	x = float(raw_input("How many doublings do you want? "))
	
	n = float(raw_input("How many times is interest compounded per year? "))

	
	t = (x/n)*((log(2))/(log(1+(r/n))))
	A = P*2**x
	
	# Print out time taken and final amount 
	print "It will take %.2f years for your money to double %.2f times, after which you will have $%.2f." %(t,x,A)


elif choice == 2:
	
	P = float(raw_input("How much do you have to start out with? "))
	
	r = float(raw_input("What is the decimal interest rate? "))
	
	A = float(raw_input("What is the final amount you want? "))
	
	n = float(raw_input("How many times is interest compounded per year? "))

	
	t = (1/n)*((log(A/P))/(log(1+(r/n))))
	
	# Print out time taken and final amount 
	print "It will take %.2f years for your investment to reach $%.2f." %(t,A)


