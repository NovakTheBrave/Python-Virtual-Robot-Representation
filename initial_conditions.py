
# Create a blank dictionary that will be filled and returned.
return_dict = {}

# Create a value EMPTY (True) to represent when a gripper is empty.
EMPTY = True

def first_pos():
    """
This function will be used to reset the robot back to a home position. Initial variables will be
collected from the user.
    """

    # Reference the Empty state and return dictionary.
    global EMPTY
    global return_dict

    # Add gripper statuses to the return dictionary to set them to Empty.
    return_dict["gripper1"] = EMPTY
    return_dict["gripper2"] = EMPTY

    # Set the location to home.
    return_dict["robot_loc"] = 1

    # Print instructions to the user.
    print("To declare a part amount, please input the number of each color followed by enter.")

    # Prompt the user to input the red bin count:
    return_dict["first_redbin_count"] = int(input("How many parts are there in the red / green / blue bins?\n Red: "))

    # Catch statement for if the input arguments are illegal.
    while return_dict["first_redbin_count"] > 10:
        return_dict["first_redbin_count"] = int(input("\n That number is too large. Enter a value less than 11: "))

    # Prompt the user to input the green bin count:
    return_dict["first_greenbin_count"] = int(input("\n Green: "))

    # Catch statement for if the input arguments are illegal.
    while return_dict["first_greenbin_count"] > 10:
        return_dict["first_greenbin_count"] = int(input("\n That number is too large. Enter a value less than 11: "))

    # Prompt the user to input the blue bin count:
    return_dict["first_bluebin_count"] = int(input("\n Blue: "))

    # Catch statement for if the input arguments are illegal.
    while return_dict["first_bluebin_count"] > 10:
        return_dict["first_bluebin_count"] = int(input("\n That number is too large. Enter a value less than 11: "))

    # Prompt user for kit tray numbers:
    return_dict["first_redkit_count"] = int(input("How many parts are already in the red / green / blue kits?\n Red: "))
    return_dict["first_greenkit_count"] = int(input("\n Green: "))
    return_dict["first_bluekit_count"] = int(input("\n Blue: "))

    # Prompt the user for the part amounts needed to place in each kit:
    return_dict["red_parts_to_place"] = int(input("How many parts need to be placed in the red / green / blue kits?\n Red: "))
    return_dict["green_parts_to_place"] = int(input("\n Green: "))
    return_dict["blue_parts_to_place"] = int(input("\n Blue: "))

    # Create a boolean to represent an exit case for the program.
    is_num_illegal = False

    # Catch statements for if the amount of needed parts exceeds the amount in the bins.
    # They will set the exit case to True.
    # These catches terminate the program, as opposed to re-prompting the user, as with the bin count catches.
    if return_dict["red_parts_to_place"] > return_dict["first_redbin_count"]:
        print(f"Not enough red parts for kiting. {return_dict['red_parts_to_place']} needed, {return_dict['first_redbin_count']} available")
        is_num_illegal = True
    if return_dict['green_parts_to_place'] > return_dict['first_greenbin_count']:
        print(f"Not enough green parts for kiting. {return_dict['green_parts_to_place']} needed, {return_dict['first_greenbin_count']} available")
        is_num_illegal = True
    if return_dict['blue_parts_to_place'] > return_dict['first_bluebin_count']:
        print(f"Not enough blue parts for kiting. {return_dict['blue_parts_to_place']} needed, {return_dict['first_bluebin_count']} available")
        is_num_illegal = True

    # Exit detection for illegal arguments. This will terminate this program
    if is_num_illegal:
        print("Exiting...")
        pass

    # If the inputs are legal, the robot "Generates a plan" and then returns the dictionary containing all user inputs.
    print("Generating a plan....\n\n\n")
    return return_dict

