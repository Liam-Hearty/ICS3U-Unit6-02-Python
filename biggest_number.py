#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program uses a list as a parameter

import random


def biggest_number(list_of_numbers):
    # this functions add up all the numbers in the list

    total = 0

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 9:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 8:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 7:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 6:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 5:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 4:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 3:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 2:
            total = list_of_numbers[0+counter]
            return total
        counter += 1

    counter = 0
    for counter in range(0, 9):
        if list_of_numbers[0+counter] > 1:
            total = list_of_numbers[0+counter]
            return total
        counter += 1


def main():
    # this function uses a list

    random_numbers = []
    big_num = 0

    # input
    print("The numbers are ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    big_num = biggest_number(random_numbers)

    print("The biggest number is: {0} ".format(big_num))


if __name__ == "__main__":
    main()
