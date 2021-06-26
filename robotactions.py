# Call in first_pos as fp, and robot_position as robpos.
from initial_conditions import first_pos as fp
from robot_position import robot_positon as robpos


# Two boolean variables used to represent the status of the grippers.
# EMPTY (True) represents an empty status. HOLDING (False) represents the gripper holding a part
EMPTY = True
HOLDING = False

# Call fp (from the initial_conditions file) to return a dictionary with all the inputs. This is represented as
# init_vals
init_vals = fp()

# Unpack the red variables from the dictionary.
redbin_num = init_vals["first_redbin_count"]
redkit_num = init_vals["first_redkit_count"]
redpart_num = init_vals["red_parts_to_place"]

# Unpack the green variables from the dictionary.
greenbin_num = init_vals["first_greenbin_count"]
greenkit_num = init_vals["first_greenkit_count"]
greenpart_num = init_vals["green_parts_to_place"]

# Unpack the blue variables from the dictionary.
bluebin_num = init_vals["first_bluebin_count"]
bluekit_num = init_vals["first_bluekit_count"]
bluepart_num = init_vals["blue_parts_to_place"]

# Calculate the remaining_num to be the sum of all parts needing placing.
remaining_num = redpart_num + greenpart_num + bluepart_num

def move_rob(rob_loc: int, desired_mov: int):
    """
This function will move the robot from its current position to the desired position.
    :param rob_loc: integer representing the current position (home = 1, bin = 2, kit = 3).
    :param desired_mov: integer representing where the robot will move next.
    :return: the updated location is returned.
    """
    print("Start: ")

    # Call robpos to print the current position.
    robpos(rob_loc)

    # "Move" the robot to the next position.
    rob_loc = desired_mov
    print("\nMoving...\n\nEnd:")

    # Call robpos again to print the ending position.
    robpos(rob_loc)

    # Return the updated position
    return rob_loc


def part_picking(remaining_red: int, remaining_green: int, remaining_blue:int):
    """
This function will grab parts from the bin. It will do so by detecting first if there are any red parts that still need
to be assembled, then any green parts, and, finally, any blue parts. After picking a part, it will return count
variables for the amount of parts left in each bin, as well as the color and amount picked by the robot.
    :param remaining_red: integer representing the remaining red parts to be placed.
    :param remaining_green: integer representing the remaining green parts to be placed.
    :param remaining_blue: integer representing the remaining blue parts to be placed.
    :return: this function returns the three input variables after they are modified, and two integers representing the
    color picked (1, 2, or 3) and the number picked (1 or 2).
    """

    # Set integers and call global variables for use in the function.
    num_pick = 0
    color_pick = 0
    global redbin_num
    global greenbin_num
    global bluebin_num

    if remaining_red > 0:

        # Set color_pick to notify that red was picked.
        color_pick = 1

        # Detect if more than one red part needs grabbing. If so, two are grabbed by the left and right arms.
        # Then, the count variables are modified accordingly.
        if remaining_red != 1:
            print("Picked red part with left arm.\nPicked red part with right arm.\n")
            grip1 = HOLDING
            grip2 = HOLDING
            remaining_red -= 2
            redbin_num -= 2
            num_pick = 2

        # Otherwise, the left arm grips one red part. The counts are modified accordingly.
        else:
            print("Picked red part with left arm.\n")
            grip1 = HOLDING
            remaining_red -= 1
            redbin_num -= 1
            num_pick = 1
        # Return statement for if only one part was grabbed.
        return remaining_red, remaining_blue, remaining_green, num_pick, color_pick

    elif remaining_green > 0:

        # Set color_pick to notify that green was picked.
        color_pick = 2

        # Detect if more than one green part needs grabbing. If so, two are grabbed by the left and right arms.
        # Then, the count variables are modified accordingly.
        if remaining_green != 1:
            print("Picked green part with left arm.\nPicked green part with right arm.\n")
            grip1 = HOLDING
            grip2 = HOLDING
            remaining_green -= 2
            greenbin_num -= 2
            num_pick = 2

        # Otherwise, the left arm grips one green part. The counts are modified accordingly.
        else:
            print("Picked green part with left arm.\n")
            grip1 = HOLDING
            remaining_green -= 1
            greenbin_num -= 1
            num_pick = 1

        # Return statement for if only one part was grabbed.
        return remaining_red, remaining_blue, remaining_green, num_pick, color_pick

    elif remaining_blue > 0:

        # Set color_pick to notify that blue was picked.
        color_pick = 3

        # Detect if more than one blue part needs grabbing. If so, two are grabbed by the left and right arms.
        # Then, the count variables are modified accordingly.
        if remaining_blue != 1:
            print("Picked blue part with left arm.\nPicked blue part with right arm.\n")
            grip1 = HOLDING
            grip2 = HOLDING
            remaining_blue -= 2
            bluebin_num -= 2
            num_pick = 2

        # Otherwise, the left arm grips one blue part. The counts are modified accordingly.
        else:
            print("Picked blue part with left arm.\n")
            grip1 = HOLDING
            remaining_blue -= 1
            bluebin_num -= 1
            num_pick = 1
        # Return statement for if only one part was grabbed.
        return remaining_red, remaining_blue, remaining_green, num_pick, color_pick

    # Error case for if there are no parts left, or any other oddball cases.
    else:
        print("No parts found to pick.\n")
        pass


def assemble_kits(gripped: int, color: int):
    """
This function will perform the assembling of the kits. It will determine how many parts need to be placed based on the
current statues of the grippers.
    :param gripped: integer representing how many grippers are holding parts.
    :param color: integer representing the three different colors. Red is 1, green is 2, blue is 3.
    :return: the function will return the remaining number of parts to be assembled after placing the current parts.
    """

    # References to global varaibles
    global redkit_num
    global greenkit_num
    global bluekit_num
    global robot_pos
    global remaining_num

    # Detection for what the color is. This will dictate which will be placed.
    if color == 1:
        color_name = "red"
    elif color == 2:
        color_name = "green"
    elif color == 3:
        color_name = "blue"
    else: color_name = "error"

    # Detection for if two parts are being held.
    if gripped == 2:

        # Print statement representing the action of the robot placing the parts.
        print(f"Placed {color_name} part with left arm.\nPlaced {color_name} part with right arm.\n")

        # Modifications to the global count variables for if the color held is red.
        if color == 1:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 2
            redkit_num += 2

        # Modifications to the global count variables for if the color held is green.
        elif color == 2:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 2
            greenkit_num += 2

        # Modifications to the global count variables for if the color held is blue.
        elif color == 3:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 2
            bluekit_num += 2

        # Else statement for error cases. It will return the robot home if reached. This will not stop the program,
        # however.
        else:
            print("Something went wrong with the placement action. Returning to home.")

            robot_pos = 1
            return remaining_num

        # If all goes right, the remaining number of total parts is returned for use in the robot running.
        return remaining_num

    # Detection for if only one part is held.
    elif gripped == 1:

        # Print statement representing the action of the robot placing one part, from the left arm.
        print(f"Placed {color_name} part with left arm.\n")

        # Modifications to the global count variables for if the color held is red.
        if color == 1:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 1
            redkit_num += 1

        # Modifications to the global count variables for if the color held is green.
        elif color == 2:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 1
            greenkit_num += 1

        # Modifications to the global count variables for if the color held is blue.
        elif color == 3:
            grip1 = EMPTY
            grip2 = EMPTY

            remaining_num -= 1
            bluekit_num += 1

        # Otherwise, this else statement will reset the robot if an error case occurs.
        else:
            print("Something went wrong with the placement action. Returning to home.")

            robot_pos = 1
            return

    # Return statement for the total remaining number of parts.
    return remaining_num


def run_bot_1():
    """
This program represents the robot running through it actions. it will run until the global total count of parts to be
placed is 0.
    """
    # References to global variables
    global redpart_num, greenpart_num, bluepart_num
    global redkit_num, greenkit_num, bluekit_num
    global redbin_num, greenbin_num, bluebin_num
    global remaining_num
    global init_vals

    # Pre-declare operating positions as integers for ease of calling
    bin_pos = 2
    kit_pos = 3

    # Call the current position from the initial setup
    current_pos = init_vals['robot_loc']

    # Calculate the remaining number of parts to be placed
    remaining_num = redpart_num + greenpart_num + bluepart_num

    # Create temporary variables for part number storage
    tmp_redpart = redpart_num
    tmp_greenpart = greenpart_num
    tmp_bluepart = bluepart_num

    # While loop that executes while there are still parts that need to be placed. This is represented by remaining_num.
    while remaining_num > 0:
        print("\n========================================\n")

        # Move the robot from the previous position to the bins.
        current_pos = move_rob(current_pos, bin_pos)

        # Activate the part picking function after moving to the bins.
        rp1, bp1, gp1, hold_num, color_num = part_picking(tmp_redpart, tmp_greenpart, tmp_bluepart)

        # Modify the temporary variables accordingly.
        tmp_redpart = rp1
        tmp_greenpart = gp1
        tmp_bluepart = bp1

        print("\n========================================\n")

        # Move the robot to the kits from the current position.
        current_pos = move_rob(current_pos, kit_pos)

        # Activate assembly function to assemble the kits and modify the remaining parts.
        remaining_num = assemble_kits(hold_num, color_num)

    # Call move_rob to move the robot home.
    current_pos = move_rob(current_pos, 1)
    print("\n========================================\n")

    # Print the ending position
    print("\nFinal position:")
    robpos(current_pos)

    # Print the summary showing the end results of the kit and bin numbers.
    print(f"\n\nSummary:\n\n"
          f"The kit tray has {redkit_num} red parts. The red bin has {redbin_num} parts left.\n")
    print(f"The kit tray has {greenkit_num} green parts. The green bin has {greenbin_num} parts left.\n")
    print(f"The kit tray has {bluekit_num} blue parts. The blue bin has {bluebin_num} parts left.\n")
    print("\n========================================\n")


#Run the robot through the course
run_bot_1()
