# Quest 15: The Nested Riddle
# Ask user to choose left or right
# If left, ask if they swim or wait
# Print the outcome based on their choices

direction = input("Do you go left or right: ")

if direction == "left":
    action = input("Enter choice: swim/wait? ")
    
    if action == "swim":
        print("Congratulations! You found the hidden treasure!")
    else:
        print("Sorry! No treasure for you.")
else:
    print("No moves left!")
