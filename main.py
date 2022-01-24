#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Min Num

from random import randint


def main():
    # main function for min number

    # create array with 10 random numbers/process
    arr = [randint(1, 100) for rand in range(10)]

    # define smallest variable
    smallest = 101
    arr = [randint(1, 100) for rand in range(10)]

    # get smallest/process
    for num in arr:
        print(f"The random number is: {num}")
        if num < smallest:
            smallest = num

    # output
    print(f"\nSmallest number is {smallest}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
