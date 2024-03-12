# sort a list using merge sort algorithms

def merge(num1,num2):
    merger = []
    i,j = 0, 0
    while i < len(num1) and j < len(num1):
        if num1[i] < num2[j]:
            merger.append(num1[i])
            i+=1
        else:
            merger.append(num2[j])
            j+=1

    num1_tail = num1[i:]
    num2_tail = num2[j:]

    return merger+num1_tail+num2_tail


print(merge([2,4,6],[1,5,9]))
