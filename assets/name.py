def contains_invalid_characters(input_str):
    invalid_chars = set(" !@#$%^&*()")
    return any(char in invalid_chars for char in input_str)

name = input("What is your name? ")
surname = input("What is your surname? ")

# Check if name contains any digits
if any(char.isdigit() for char in name):
    print("Please give letters in name!")

# Check if surname contains any digits
elif any(char.isdigit() for char in surname):
    print("Please give letters in surname!")

# Check if name contains any invalid characters
elif contains_invalid_characters(name):
    print("Name contains invalid characters!")
    
# Check if surname contains any invalid characters
elif contains_invalid_characters(surname):
    print("Surname contains invalid characters!")
else:
    print(name, surname)

# Checks if given name and surname has valid characters and prints it
