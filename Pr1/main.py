"""Ask for a user's name and age, then display a personalized greeting."""

# Ask the user for their name.
name = input("What is your name? ").strip()

# Keep asking until the user enters a whole number for their age.
while True:
    age_text = input("How old are you? ").strip()

    if age_text.isdigit():
        age = int(age_text)
        break

    print("Please enter your age as a whole number, such as 12.")

# Display a personalized greeting.
print(f"Hello, {name}! You are {age} years old. Nice to meet you!")
