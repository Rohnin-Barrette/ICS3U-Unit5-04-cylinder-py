#!/usr/bin/env python3

# Created by: Rohnin. B
# Created on: Sep 2021
# this program calculates the volume of a cylinder

import math
import constants


def cylinder_volume(radius, height):
    # this functon calculates volume

    volume = constants.PI * (radius * radius) * height
    return volume


def main():
    # this function gets radius and height

    # input
    radius_value = input("Enter the radius of the cylinder: ")
    height_value = input("Enter the height of the cylinder: ")

    # process
    try:
        radius_value_int = float(radius_value)
        height_value_int = float(height_value)
        volume_value = cylinder_volume(radius=radius_value_int, height=height_value_int)
        if radius_value_int < 0:
            print("Radius is lower than 0, please enter a positive number.")
        elif height_value_int < 0:
            print("Height is lower than 0, please enter a positive number.")
        else:
            print("The volume of the cylinder is {}³".format(volume_value))
    except Exception:
        print("Invalid input")
    print("\nDone")


if __name__ == "__main__":
    main()
