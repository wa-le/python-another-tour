# Print a string n times
print(1)
print("This is a separator", "-"*20)
print("wiggle "*5)
print()

print(2)
# split a string
the_string = "This is not a surprise"
the_string2 = the_string.split()
print(the_string2)
the_string3 = " ".join(the_string2)
print(the_string3)
print()

print(3, 4)
# flatten a list
list_of_list = [["a", "b", "c"], [6, 9, 12], ["$", "#", "£"]]
flattened_list = [j for i in list_of_list for j in i]
print(flattened_list)

# Reverse the flattened  list
flattened_list.reverse()
rev_flattened_list = [i for i in flattened_list]
print(rev_flattened_list)
print()

print(5)
# Merge 2 lists into a dictionary
list1 = ["x", "y", "z"]
list2 = [1, 2, 3]
merge2_dict = dict(zip(list1, list2))
print(merge2_dict)
print()

print(6)
# Sort a list of dictionaries by Key
students = [
    {"name": 'Ridwan', "age": 34},
    {"name": 'Waris', "age": 19},
    {"name": 'Shayne', "age": 50}
]
print(students)
students_sorted = sorted(students, key=lambda the_key: the_key['age'])
print(students_sorted)
print()

print(7)
# Sorting a list based on another list -sort list_a using list_b-
list_a = ["a", "b", "c", "d"]
list_b = [2, 3, 0, 1]
list_a_sorted = [list_a[g] for g in list_b]
print(list_a_sorted)
print()

print(8)
# Get most frequent value from a list
the_list = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'b', 'a', 'b', 'c', 'b', 'b', 'c', 'a', 'b', 'c']
print(max(set(the_list), key=the_list.count), 'is the Most frequent value:')
print()

print(9)
# Palindrome
palindrome_string = "racecar"
is_palindrome = palindrome_string == palindrome_string[::-1]
print("Is a palindrome:", is_palindrome)