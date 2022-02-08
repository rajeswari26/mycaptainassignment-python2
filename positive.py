
list_1 = [12, -7, 5, 64, -14]
list_2 = [12, 14, -95, 3]
my_list = list_1 + list_2
n = 0
while(n < len(my_list)):
	if my_list[n] >= 0 :
		print(my_list[n], end = " ")
	n += 1
	
