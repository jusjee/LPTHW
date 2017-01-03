print "How old are you?",
age = raw_input()
age2 = int(age)
print "How tall are you?",
height = raw_input()
ht2 = int(height)
print "How much do you weigh?",
weight = raw_input()
wt2 = int(weight)

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "So, you're %s old, %s tall and %s heavy. %d %d %d" % (
	age, height, weight, age2, ht2, wt2)
