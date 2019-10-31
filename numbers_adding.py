#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program uses a continue statement


def process():
    while True:
        try:
            total_numbers = []

            input_number = int(input("How many numbers are to ADD(+): "))
            print()

            for addition in range(input_number):
                input_number = int(input("Enter a number to add: "))

                if input_number < 0:
                    continue

                total_numbers.append(input_number)

            print()
            print("Total of the positive numbers are: ", sum(total_numbers))

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    process()
