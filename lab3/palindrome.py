word = raw_input("enter in a string\n")
x = 0
for i in range (len(word) / 2):
	if(word[x]) == (word[len(word)-x-1]):
		x += 1
	if x == (len(word)/2):
		print "True"
	else:
		print "False"
		