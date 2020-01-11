x = 0

while x < 5:
	print('THE CURRENT VALUE OF X IS {}'.format(x))
	x = x + 1    # This is the same as Javva,   x += 1
else:
	print('x is not less than 5')

x = [1,2,4]

for item in x:
	pass

print('end of my script')

myString = 'Sammy'

for letter in myString:
	if letter =='a':
		continue
		#break
		#pass
	print(letter)

x = 0

while x < 5: 
	if x == 2:
		break
	print(x)
	x += 1