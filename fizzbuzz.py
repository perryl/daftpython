count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print "fizzbuzz"
    elif count % 5 == 0:
        print "buzz"
    elif count % 3 == 0:
        print "fizz"
    else:
        print count
    count += 1
