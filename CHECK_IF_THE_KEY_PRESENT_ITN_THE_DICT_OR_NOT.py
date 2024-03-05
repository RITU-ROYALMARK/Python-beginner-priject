#python programme to check if key is alerady present in the dictinaory

#FIRST CREATE A DICT AND APPEDN THE KEY AND VALUE IN DICT
def create_dict():
    dict = {}
    how_many_keys = int(input("enter the number of key do you want enter: "))
    for _ in range(how_many_keys):
        name = input("enter the name AS key: ")
        marks = input("enter the age as value: ")
        dict[name] = int(marks)
    return dict

# CHECK IF THE KEY IS IN THE DICT
def check_if_key_in_the_dict(dict):
    check = input("enter the key which you wanno check: ")
    for key,value in dict.items():
        if check in key:
            print("YES")
            break
        if check != dict:
            print("NO")
            create_dict()


dict = create_dict()
check_if_key_in_the_dict(dict)