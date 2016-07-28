import argparse
import random

def euro_lotto():
    numbers = random.sample(xrange(1,50),5)
    lucky = random.sample(xrange(1,11),2)
    numbers.sort()
    lucky.sort()
    print "Chosen numbers are %s, %s, %s, %s and %s" % (
        numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
    print "Lucky stars are %s and %s" % (lucky[0], lucky[1])

def lotto():
    number = random.sample(xrange(1,49),6)
    bonus = number[5]
    number.pop(5)
    number.sort()
    print "Chosen numbers are %s, %s, %s, %s and %s with bonus ball %s" % (
        numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], bonus)

def main():
    parser = argparse.ArgumentParser(description='Option selector.\n'
        '1. Euromillions generator\n2. Lotto generator')
    parser.add_argument('--choice', type=int, help='Option (1 or 2)')
    args = parser.parse_args()
    i = args.choice
    print i
    if i == 1:
        print "Running Euromillions generator..."
        euro_lotto()
    elif i == 2:
        print "Running Lotto generator..."
        lotto()
    else:
        raise Exception('Please set choice as 1, 2 or 3')

if __name__ == "main":
    main()
