#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for char in range(97, 123):
    if chr(char) == 'q' or chr(char) == 'e':
        continue
    else:
        print("{}".format(chr(char)), end="")
