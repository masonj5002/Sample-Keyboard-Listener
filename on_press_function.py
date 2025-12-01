#!/usr/bin/env python3

from pynput import keyboard
from time import sleep


def on_press(key):
    """Handles key press events"""
    try:
        if key.char == "a":
            sleep(0.5)
            print("You Pressed a!")

        elif key.char == "b":
            sleep(0.5)
            print("You Pressed b!")

        elif key.char == "q":
            print("Quitting...")
            sleep(1)
            return False
    except AttributeError:
        # Handles shift, ctrl, etc
        pass


def main():
    print("Press 'a', 'b', or 'q' to quit.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
