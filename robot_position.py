
def robot_positon(position: int):
    """
This function can be called to determine the robot's current position. It will print and return a given position.
    :param position: integer to determine the current position.
    :return: Can return None or a string showing the position.
    """

    # Home position:
    if position == 1:
        print("Robot is at the home position")
        return "at_home"

    # Bin position:
    elif position == 2:
        print("Robot is at the bin position")
        return "at_bin"

    # Kit position:
    elif position == 3:
        print("Robot is at the kit tray position")
        return "at_tray"

    # Error case:
    else:
        print("Robot was not found")
        return