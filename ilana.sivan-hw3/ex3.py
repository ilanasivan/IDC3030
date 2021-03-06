# Write a function which receives as an input argument a string which represents a 9 digit number, and checks whether it is a valid Israeli ID number. Your program should print only a single word: valid or invalid at the end of the process.

# To validate an ID number:

# Multiply each digit by 1 or 2 in an alternating fashion. Left-most digit by 1, next digit by 2, then by 1, then by 2, and so on.
# For every multiplication result from the previous step, if it's greater than 9, sum the digits of that number to get a single digit number.
# Sum up all the numbers from the previous step.
# If the result is a multiply of 10, we can conclude that the ID number is valid. Otherwise, it's invalid.

def validate_israeli_id(id_number):
    sum = 0
    id = [int(x) for x in str(id_number)]

    for i in range(len(id)):
        id[i] *= (i % 2) + 1

        if (id[i] > 9):
            id[i] -= 9
        sum += id[i]

    if (sum % 10 == 0):
        print("valid")
    else:
        print("invalid")
