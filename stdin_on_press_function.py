#!/usr/bin/env python3

from sys import stdin
import termios
from tty import setcbreak
from time import sleep


def get_key():
    """Read a single keypress from stdin"""
    fd = stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        setcbreak(fd)
        cha = stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return cha


def main():
    print("Press 'a', 'b', or 'q' to quit.")

    while True:
        key = get_key()

        if key == "a":
            print("You pressed 'a'!")

        elif key == "b":
            print("You pressed 'b'!")

        elif key == "c":
            print("You pressed 'c'!")

        elif key == "q":
            print("Goodbye!")
            sleep(0.5)
            break


if __name__ == "__main__":
    main()
