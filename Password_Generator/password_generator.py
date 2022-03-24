import random

numbers = "0123456789"
symbols = "!@#$().%*"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# concatenate numbers, symbols, lower and upper
concat_all = lower + upper + numbers + symbols
# length of password
length = 13
# or let user type desired length of password
# length = int(input("what is your desired password length: "))

# selects randomly from the variable concat_all and the join method makes it a string
the_password = "".join(random.sample(concat_all, length))

print(f"-> {the_password} <- is your Password")
