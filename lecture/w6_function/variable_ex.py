def calculate(x, y):
	print "Test: ", total
	print "In Function"
	print "a:", str(a), "b:", str(b), "a+b:", str(a+b) 
	print "total :", str(total)
	return total

a = 5
b = 7
total = 0
print "In Program - 1"
print "a:", str(a), "b:", str(b), "a+b:", str(a+b) 

sum = calculate (a,b)
print "After Calculation"
print "Total :", str(total), " Sum:", str(sum)
