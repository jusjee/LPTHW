from sys import argv

script, user_name, real_name = argv
prompt = 'itmadick$'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
I know your name is %s
""" % (likes, lives, computer, real_name)
