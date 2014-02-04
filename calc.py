while True:
	try:
		x = int(raw_input('Enter a value: '))
		break
	except:
		print "Integer values only, please!"
		continue
while True:
	try:
		y = int(raw_input('Enter a second value: '))
		break
	except:
		print "Integer values only, please!"
		continue
add = x+y
dif = abs(x-y)
mul = x*y
quo = x/y
rem = x%y
print 'The sum of ',x,' and ',y,' is ',add
print 'The difference between ',x,' and ',y,' is ',dif
print 'The product of ',x,' and ',y,' is ',mul
if rem == 0:
	print 'The quotient of ',x,' and ',y,' is ',quo
else:
	fquo = float(x)/y
	print 'The quotient of ',x,' and ',y,' is ',quo,' with a remainder of ',rem,' , '
	print '		or when expressed as a decimal, ',fquo
if add % 2 == 0:
	av1 = add/2
	print 'Finally, the average of ',x,' and ',y,' is ',av1
else:
	av2 = float(add)/2
	print 'Finally, the average of ',x,' and ',y,' is ',av2
