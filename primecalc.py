while True:
	try:
		x = int(raw_input("Enter a lower limit: "))
		if x < 2:
			print "Set a lower limit of 2 or greater, please!"
			continue
	except:
		print "Please enter your value as an integer..."
		continue
	else:
		break

while True:
	try:
		y = int(raw_input("Enter an upper limit: "))
		if y <= x:
			print "Upper limit cannot be less than/equal to lower limit!"
			continue
	except:
		print "Please enter your value as an integer..."
		continue
	else:
		break

for n in range(x,y):
	for z in range(2,n):
		if n % z == 0:
			break
	else:
		print n,"is a prime number."
