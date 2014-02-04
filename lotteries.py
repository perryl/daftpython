import random
print "Please choose which generator to use from the list shown below:"
print "		1. Euromillions"
print "		2. Lotto"
print "		3. Simple random number generator"
while True:
	try:
		choice = int(raw_input())
		if choice == 1:
			print "Running Euromillions generator..."
			numbers = random.sample(xrange(1,50),5)
			lucky = random.sample(xrange(1,11),2)
			numbers.sort()
			lucky.sort()
			print "Chosen numbers are ",numbers[0],",",numbers[1],",",numbers[2],",",numbers[3],"and",numbers[4]
			print "Lucky stars are ",lucky[0],"and",lucky[1]
			break

		elif choice == 2: 
			print "Running Lotto generator..."
			number = random.sample(xrange(1,49),6)
			bonus = number[5]
			number.sort()
			print "Chosen numbers are ",number[0],",",number[1],",",number[2],",",number[3]," and ",number[4]," and a bonus ball of ",bonus
			break

		elif choice == 3:
			print "Running random number generator..."
			while True:
				try:
					x = int(raw_input("Enter lower limit of range: "))
					break
				except:
					print "Please enter value as an integer!"
			while True:
				try:
					y = int(raw_input("Enter upper limit of range: "))
					if y <= x:
						print "Upper limit cannot be less than/equal to lower limit!"
						continue
				except:
					print "Please enter value as an integer!"
				else:
					break
			while True:
				try:
					z = int(raw_input("And enter amount of random numbers to be generated: "))
					if z > y-x:
						print "Can't have more numbers than what is in the range!"
						continue
				except:
					print "Please enter value as an integer!"
				else:
					break
			numbers = random.sample(xrange(x,y),z)
			numbers.sort()
			print numbers
			break

		else:
			print "Please enter either 1, 2 or 3!"
			continue
	except:
		print "Please enter either 1, 2 or 3 as an integer!"
		continue
