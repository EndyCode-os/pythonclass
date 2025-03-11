def findTotal(a):
    for i in a:  # This line need to be removed if a is not a list of lists but a simple list of elements
     print(sum(i)*2)

#findTotal([[2,3], [3,4]]) <-- Test value