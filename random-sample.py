import random
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
