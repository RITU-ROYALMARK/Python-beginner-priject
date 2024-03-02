#INIZITALSE THE LIST HOW MANY NUMBER OF INNER LIST


nested_list = []
num_in_list = int(input("enter the number of inner list: "))
# THE NUM_IN_LIST IS USED FOR THE NUMBER OF INNER LIST

for _ in range(num_in_list):
    # THE FOR LOOP THE TAKE THE NUMBER OF INNER LIST
    inner_list = [] # THE EMPTY LIST WHERE YOU WILL STORE THE NUMBER OF INNER ITEMS
    inner_items = int(input("enter the number items in the inner list: "))
    for _ in range(inner_items):
        # THIS FOR LOOP IS TO GIVE THE INPUT WRITE THE ITEMS
        items = input("enter the items in the list: ")
        inner_list.append(items)# APPEND THE ITEMS INT HE INNER_LIST
    nested_list.append(inner_list)# AND THAT INNER_LIST APPEND IT TO THE NESTED_LIST

#AND PRINT THE NESTED LIST

print(f"NESTED LIST: {nested_list}")
