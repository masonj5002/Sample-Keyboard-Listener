#!/usr/bin/env python3

'''
Testing to see if an infinite `while` loop is a good idea.
'''

from time import sleep
from pynput import keyboard


def on_press(key):
    """Handles key press events"""
    try:
        if key.char == "a":
            print("You Pressed a!")
        elif key.char == "b":
            print("You Pressed b!")
        elif key.char == "q":
            print("Quitting...")
            return False
    except AttributeError:
        # Handles shift, ctrl, etc
        pass


def main():
    while True:
        print('hello')
        sleep(1)


if __name__ == "__main__":
    main()
