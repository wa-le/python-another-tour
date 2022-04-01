# Print a string n times
print("This is a separator", "-"*20)
print("wiggle "*5)
print()

# split a string
the_string = "This is not a surprise"
the_string2 = the_string.split()
print(the_string2)
the_string3 = " ".join(the_string2)
print(the_string3)
print()

# flatten a list
list_of_list = [["a", "b", "c"], [6, 9, 12], ["$", "#", "£"]]
flattened_list = [j for i in list_of_list for j in i]
print(flattened_list)

# Reverse the flattened  list
flattened_list.reverse()
rev_flattened_list = [i for i in flattened_list]
print(rev_flattened_list)
print()