# Python3 code to demonstrate
# to combine two sorted list
# using sorted()

# initializing lists
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using sorted()
# to combine two sorted lists
res = sorted(test_list1 + test_list2)

# printing result
print("The combined sorted list is : " + str(res))
