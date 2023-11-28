#!/usr/bin/python3
def fizzbuzz():
    for l in range(1, 101):
        if l % 3 == 0:
            print("Fizz", end=" ")
            continue
        if l % 5 == 0:
            print("Buzz", end=" ")
            continue
        print(l, end=" ")
