import random

# list of desired password elements. both list can be updated
a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b_list = ["&", "#", "@", "€", "(", '!', '$', '%', ')', '*', '+']

the_password = []
pass_length = int(input("enter desired password length: "))

# randomly select half of pass_length from the first list and append to the_password list
for a in range(1, int((pass_length/2) + 1)):
    the_password += random.choice(a_list)

# randomly select half of pass_length from the second list and append to the_password list
for b in range(1, int((pass_length/2) + 1)):
    the_password += random.choice(b_list)

# shuffle the password
random.shuffle(the_password)
print(the_password)

# convert list 'the_password' to string with variable name 'password'
password = ""
for char in the_password:
    password+=char
print(f"your password is {password}")
    
