#THIS IS A PROJECT IN WHICH YOU GIVE AN INPUT OF 3/3 MATRIX LIST AND FIND OUT IF THE KEY ARE REPEATED OR NOT

nested_list = []
# CREATING A NESTED LIST
num_of_nested_list = int(input("enter the number of nested list: ")) #TAKING INPUT OF HOW MANY NUMBER OF NESTED LIST YOU WANT

for _ in range(num_of_nested_list):# ITERATING THROUGH RANGE OF NUMBER OF LIST
    inner_list = []

    number_of_items = int(input("enter the number of items enter i: "))# TAKING INPUT FOR HOW MANY NUMBER OF ITEMS DO YOU WANT ENTER IN THE NESTED LIST

    # ITERATING THROUGH THE NUMBER OF ITEMS
    for _ in range(number_of_items):
        items = input("enter the items: ")#CREATE AN INPUT TO ENTER WHAT ARE THE ITEMS INSIDE THE LIST

        inner_list.append(items)# append the the items in the inner list

    nested_list.append(inner_list)# append the inner list into the nested_list

temp = 0
# print(nested_list)
nested_dict = {}# convert the nested list into dict by which you can compare the value & key that any of them are repeated or not

for items in nested_list:
    key = items[0]
    value = items[1]
    nested_dict[key] = value

for key,value in nested_dict.items():# using for loop for to loop through the dict
    temp = value# its going to store the value

    for skey,svalue in nested_dict.items():# usign for loop to iterate through the dict

        if key != skey:# compare the key is equal to key if yes then we dont want it
            if temp == svalue:
                print(f"{key}:{value}")


        if key == skey:# if the key are equal then we start from first
            continue
