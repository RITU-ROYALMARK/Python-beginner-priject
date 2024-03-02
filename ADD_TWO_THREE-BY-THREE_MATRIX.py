# create two,  3/3 matrix in list and add each elements

list = [[1,10,5],
        [2,20,10],# the first 3by3 matrix list
        [3,30,15]]

list1 = [[1,10,5],
         [2,20,10],# the second 3/3 matrix list
         [3,30,15]]

result = [[0,0,0],
         [0,0,0],# empty 3/3 matrix list to append all of the added output in the result
         [0,0,0]]

# the i in range is for the outer list which will be 1,2,3
for i in range(len(list)):
    # the j is for the inner elements
    for j in range(len(list)):
        result[i][j] = list[i][j] + list1[i][j]# and you add the list first elements for the list2 element

# this re in range if for the output to be vertical that all if dont use the for the output will be horizontal
for re in range(len(result)):
    print(result[re])