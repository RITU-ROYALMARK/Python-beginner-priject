# FIND RUNNER UP SCORE OF THE LIST

# APEEND THE NUMBER INTO THE LIST
l = []
for _ in range(7):
    li = int(input("enter: "))
    l.append(li)


count = 0
for i in range(len(l)): # CREATE FOR TO FIND THE LEN OF L
    if i < max(l):      # AND FIND IF THE I IS LESS THAN MAX OF L
        count = i       # KEEP THE COUNT OF ITS WILL GIVE THE LAST NUMBER OF I LIKE IF THE MAX IS 7 THE COUNT WILL BE 6
print(f"THE LIST OF NUMBER ARE: {l}")
print(f"THE RUNNER UP SCORE IS: {count}")