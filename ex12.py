age = raw_input("How old are you? ")
age2 = int(age)
height = raw_input("How tall are you? ")
ht2 = int(height)
weight = raw_input("How much do you weigh? ")
wt2 = int(weight)

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're %s old, %s tall and %s heavy. %d %d %d" % (
	age, height, weight, age2, ht2, wt2)
