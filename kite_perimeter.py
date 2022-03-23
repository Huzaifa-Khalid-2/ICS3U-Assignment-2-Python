#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2020
# This program calcualtes the perimeter of a kite
# with user input


def main():
    # this function calculates the perimeter
    print("This program will calcualte the perimeter of a kite")

    # input
    print("")
    side_a = int(input("Enter the value for side a (cm): "))
    side_b = int(input("Enter the value for side b (cm): "))

    # process
    perimeter = 2 * (side_a + side_b)

    # output
    print("")
    print("Therefore the perimeter is {} cm ".format(perimeter))
    print("\nDone.")


if __name__ == "__main__":
    main()
