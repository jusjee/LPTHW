# defines the function with arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints how many cheeses with first arg
	print "You have %d cheeses!" % cheese_count
# prints how many crackers with second arg
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


# uses integers as args for fx
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# defines variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# uses those defined vars as args for fx
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# does math to define args
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# does math with variables to define args
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


print "Not how many you have? Tell me then:"
incheese = raw_input("How much cheese? ")
incrack = raw_input("How many crackers? ")

cheese_and_crackers(int(incheese), int(incrack))
