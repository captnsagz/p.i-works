string = "The weather is so sunny nowadays"
new_string = ""

temp_list = string.split()[::-1]

for i in temp_list:
	new_string = new_string + " " + i

print(new_string)

