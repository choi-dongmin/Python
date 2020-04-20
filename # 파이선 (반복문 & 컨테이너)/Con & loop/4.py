input_id = input("아이디 입력 : ")
members = ['egoing','megoing']

for member in members :
	if member == input_id:
		print(input_id,"승인")
		import sys
		sys.exit()
print ("Try again")
