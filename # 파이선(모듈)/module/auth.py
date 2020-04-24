def auth (check)
	for member in members :
		if member == check:
			print(input_id,"승인")
			import sys
			sys.exit()
	print ("Try again")
