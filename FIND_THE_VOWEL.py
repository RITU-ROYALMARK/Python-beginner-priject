# python project to find the vowels in the word and how many vowels are there


def find_vowel(vowel):
    global end_function
    number_of_vowel = 0  #"""to count number of vowel in the word input"""
    while True:
        word = input("enter the word: ")
        for i in vowel:
            if i in word:
                number_of_vowel += 1 #add one alwaya when there is vowel in the word
        go_again()
        if end_function:# if the end_function is true then break from the while loop
            break

        return number_of_vowel
def go_again():
    global end_function
    again = input("type y/n to go again: ")
    if again != "y":
        end_function = True


vowel = "AEIOUaeiou"
end_function = False

find = find_vowel(vowel)
print(find)