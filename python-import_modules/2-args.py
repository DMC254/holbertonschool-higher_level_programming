#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Excluding the script name from the arguments
    arg_count = len(argv)

    if arg_count == 0:
        print("Number of argument(s): 0.")
    else:
        print(f"Number of argument(s): {arg_count} argument{'s' if arg_count > 1 else ''}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")