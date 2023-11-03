# Write your code here
# HINT: create a dictionary from flowers.txt
flower_dic = {}
def create_filedic(filename):
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower()
            print(letter)
            flower = line.split(": ")[1].strip()
            flower_dic[letter] = flower
           
    return flower_dic

create_filedic("flowers.txt")
# HINT: create a function to ask for user's first and last name
def main(): 
    flower_d = create_filedic('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    if len(full_name) == 0:
        print("Please enter a valid name.")
        return  # Exit the function
    first_name = full_name[0].lower()
    first_letter = first_name[0]
## print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()

# print the desired output

