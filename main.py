#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Min Num

from random import randint


def find_smallest(arr):
    # define smallest number
    smallest = 101

    # get smallest/process
    for num in arr:
        print(f"The random number is: {num}")
        if num < smallest:
            smallest = num

    # return smallest
    return smallest


def main():
    # main function for min number

    # create array with 10 random numbers/process
    arr = [randint(1, 100) for rand in range(10)]

    # output/calling function
    print(f"\nSmallest number is {find_smallest(arr)}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
