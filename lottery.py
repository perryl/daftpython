import random
numbers = random.sample(xrange(1,50),5)
lucky = random.sample(xrange(1,11),2)
numbers.sort()
lucky.sort()
print "Chosen numbers are ",numbers[0],",",numbers[1],",",numbers[2],",",numbers[3],"and",numbers[4]
print "Lucky stars are ",lucky[0],"and",lucky[1]
